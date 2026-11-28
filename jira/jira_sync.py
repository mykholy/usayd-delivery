#!/usr/bin/env python3
"""Idempotent Jira Cloud work-item import. Requires Python stdlib only; run locally with a Jira API token.
Usage: JIRA_BASE_URL=... JIRA_EMAIL=... JIRA_API_TOKEN=... JIRA_PROJECT_KEY=USAYD python jira/jira_sync.py --dry-run
Full-stack scope only; excludes Flutter epics/tasks. Inspect --plan-only offline first.
A real creation run requires --apply; existing projects must use live reconciliation instead.
Does not auto-start/close sprints or change status.
"""
import argparse,base64,csv,json,os,re,sys,time,urllib.request,urllib.parse,urllib.error
from pathlib import Path
ROOT=Path(__file__).resolve().parent
base=os.environ.get('JIRA_BASE_URL','').rstrip('/')
email=os.environ.get('JIRA_EMAIL','')
token=os.environ.get('JIRA_API_TOKEN','')
project=os.environ.get('JIRA_PROJECT_KEY','USAYD')
state_file=ROOT/'.jira_sync_state.json'
state=json.loads(state_file.read_text()) if state_file.exists() else {}
def api(method,path,payload=None):
    raw=(email+':'+token).encode();authorization='Basic '+base64.b64encode(raw).decode()
    u=base+path
    body=None if payload is None else json.dumps(payload,ensure_ascii=False).encode()
    request=urllib.request.Request(u,body,headers={'Accept':'application/json','Content-Type':'application/json','Authorization':authorization},method=method)
    for attempt in range(3):
        try:
            with urllib.request.urlopen(request,timeout=30) as response:
                text=response.read().decode()
                return json.loads(text) if text else {}
        except urllib.error.HTTPError as e:
            err=e.read().decode(errors='replace')
            if e.code in (429,502,503,504) and attempt<2:time.sleep(2**attempt+1);continue
            raise RuntimeError(f'{method} {path}: HTTP {e.code}: {err[:800]}')
    raise RuntimeError('exhausted')
def rows(path):
    with open(ROOT/path,encoding='utf-8-sig',newline='') as f:return list(csv.DictReader(f))
def adf(text):
    return {'type':'doc','version':1,'content':[{'type':'paragraph','content':[{'type':'text','text':s[:30000]}]} for s in (text or '').split('\n\n') if s.strip()] or [{'type':'paragraph','content':[{'type':'text','text':'See original source package'}]}]}
FULL_STACK_REPOSITORIES = frozenset({"api", "web", "qa", "docs", "ops"})
FLUTTER_EPIC = "USYD-E-FLUTTER"

def full_stack_items(epics, tasks):
    """Validate the complete import plan before any network request or write."""
    included, excluded, known = [], [], set()
    for row in [*epics, *tasks]:
        external = row["External_ID"]
        if not external or external in known:
            raise ValueError("Missing or duplicate external ID: " + external)
        known.add(external)
        repo = row["Repository"].strip().lower()
        labels = set(row["Labels"].lower().split())
        is_flutter = (external == FLUTTER_EPIC or row["Parent_External_ID"] == FLUTTER_EPIC
                      or repo == "flutter" or "flutter" in labels
                      or row["Summary"].strip().upper().startswith("[FLUTTER]"))
        if is_flutter:
            excluded.append(row)
            continue
        if row["Issue Type"] == "Epic":
            if repo or row["Parent_External_ID"]:
                raise ValueError("Unexpected epic scope: " + external)
        elif repo not in FULL_STACK_REPOSITORIES:
            raise ValueError("Unknown repository scope: " + external)
        included.append(row)
    allowed = {r["External_ID"] for r in included}
    preceding = set()
    for row in included:
        external = row["External_ID"]
        parent = row["Parent_External_ID"]
        if parent and parent not in allowed:
            raise ValueError("Parent outside full-stack import: " + external)
        # Preserve canonical CSV order. Every parent must already occur in the
        # plan, even when a local Jira cache happens to contain that parent.
        # This also rejects self-links and every directed parent cycle.
        if parent and parent not in preceding:
            raise ValueError("Parent must precede child (invalid order or cycle): " + external)
        preceding.add(external)
    return included, excluded

def ensure_issue(row,parent_key=None,dry=False):
    external=row['External_ID'];existing=state.get(external)
    if existing:return existing,'cached'
    jql=f'project = {project} AND summary ~ "{external}" ORDER BY created DESC'
    result=api('GET','/rest/api/3/search/jql?'+urllib.parse.urlencode({'jql':jql,'maxResults':50,'fields':'summary'}))
    candidates=[x for x in result.get('issues',[]) if external in x.get('fields',{}).get('summary','')]
    if candidates:
        key=candidates[0]['key'];state[external]=key;return key,'exists'
    if dry:return 'DRY-'+external,'dry'
    obj={'fields':{'project':{'key':project},'issuetype':{'name':row['Issue Type']},'summary':row['Summary'][:255], 'description':adf(row['Description']), 'labels':[x for x in row['Labels'].split() if re.fullmatch('[a-z0-9-]+',x)]}}
    if parent_key:obj['fields']['parent']={'key':parent_key}
    try:res=api('POST','/rest/api/3/issue',obj)
    except Exception as e:
        if parent_key and 'parent' in str(e).lower():
            obj['fields'].pop('parent',None);raise RuntimeError(f'Parent relationship rejected for {external}; STOP, configure project issue hierarchy before retry: {e}')
        raise
    key=res['key'];state[external]=key;state_file.write_text(json.dumps(state,indent=2));return key,'created'
def main():
    parser=argparse.ArgumentParser()
    mode=parser.add_mutually_exclusive_group(required=True)
    mode.add_argument('--plan-only',action='store_true',help='Offline scope validation; no credentials or Jira requests')
    mode.add_argument('--dry-run',action='store_true',help='Read-only Jira lookups')
    mode.add_argument('--apply',action='store_true',help='Explicit creation of missing full-stack issues')
    args=parser.parse_args()
    items,excluded=full_stack_items(rows('JIRA_IMPORT_EPICS.csv'),rows('JIRA_IMPORT_WORK_ITEMS.csv'))
    print(f'Full-stack import: {len(items)} included; {len(excluded)} Flutter rows excluded.')
    if args.plan_only:
        return
    if not base or not email or not token:raise SystemExit('Configure JIRA_BASE_URL/JIRA_EMAIL/JIRA_API_TOKEN securely (never commit them).')
    p=api('GET','/rest/api/3/project/'+urllib.parse.quote(project));print('Project',p.get('key'),p.get('name'))
    for r in items:
        parent=state.get(r['Parent_External_ID']) if r['Parent_External_ID'] else None
        if r['Parent_External_ID'] and not parent and not args.dry_run:raise RuntimeError('No parent map for '+r['External_ID'])
        key,status=ensure_issue(r,parent,args.dry_run);print(r['External_ID'],key,status)
    print('Done; created/verified issues only. Sprint creation, dependency links, assignees and workflow statuses still need review.')
if __name__=='__main__':main()
