#!/usr/bin/env python3
"""Optional second-stage Jira Cloud synchronization after jira_sync.py.
Creates *future* sprints and places issues; links blockers. Not a substitute for sprint planning.
Requires JIRA_BASE_URL, JIRA_EMAIL, JIRA_API_TOKEN, JIRA_PROJECT_KEY, JIRA_BOARD_ID.
Use --dry-run to inspect; --create-sprints 2 for S00 and S01, --create-sprints all to populate all candidate sprint buckets.
No sprint is started/closed; does not change issue workflow status.
"""
import argparse,os,json,csv,sys,time,urllib.parse,urllib.request,urllib.error,base64
from pathlib import Path
ROOT=Path(__file__).resolve().parent
base=os.environ.get('JIRA_BASE_URL','').rstrip('/')
email=os.environ.get('JIRA_EMAIL','');token=os.environ.get('JIRA_API_TOKEN','')
board=os.environ.get('JIRA_BOARD_ID','')
state_path=ROOT/'.jira_sync_state.json'
sprint_path=ROOT/'.jira_sprint_state.json'

def request(method,path,payload=None):
    body=None if payload is None else json.dumps(payload,ensure_ascii=False).encode()
    hdr={'Authorization':'Basic '+base64.b64encode(f'{email}:{token}'.encode()).decode(), 'Accept':'application/json','Content-Type':'application/json'}
    req=urllib.request.Request(base+path,body,headers=hdr,method=method)
    for i in range(3):
        try:
            with urllib.request.urlopen(req,timeout=35) as f:
                data=f.read().decode();return json.loads(data) if data else {}
        except urllib.error.HTTPError as e:
            message=e.read().decode(errors='replace')
            if e.code in [429,502,503,504] and i<2:time.sleep(2**i+1);continue
            raise RuntimeError(f'Jira HTTP {e.code}: {message[:700]}')

def read_csv(p):
    with open(ROOT/p,encoding='utf-8-sig',newline='') as f:return list(csv.DictReader(f))

def existing_sprints():
    sprints={};offset=0
    while True:
        out=request('GET',f'/rest/agile/1.0/board/{board}/sprint?'+urllib.parse.urlencode({'startAt':offset,'maxResults':50}))
        for sprint in out.get('values',[]):sprints[sprint['name']]=sprint['id']
        if out.get('isLast',True):break
        offset+=len(out.get('values',[]))
        if not out.get('values'):break
    return sprints

def main():
    a=argparse.ArgumentParser()
    a.add_argument('--dry-run',action='store_true')
    a.add_argument('--create-sprints',default='2',help='number of candidate sprints or all; default 2')
    a.add_argument('--links',action='store_true',help='also create blocker links after issue import')
    opts=a.parse_args()
    if not all((base,email,token,board)):raise SystemExit('Configure Jira base/email/token/board ID securely')
    if not state_path.exists():raise SystemExit('First run jira_sync.py; issue state not present')
    issue_state=json.loads(state_path.read_text())
    rows=read_csv('../planning/SPRINT_CANDIDATES.csv')
    limit=len(rows) if opts.create_sprints=='all' else max(0,min(len(rows),int(opts.create_sprints)))
    sprints=existing_sprints()
    for row in rows[:limit]:
        sid=row['sprint'];name=f'Usayd {sid}'
        if name not in sprints:
            if opts.dry_run:sprints[name]='DRY';print('DRY create',name)
            else:
                result=request('POST','/rest/agile/1.0/sprint',{'name':name,'originBoardId':int(board),'goal':f'Candidate {sid}: {row["modules"][:400]}'})
                sprints[name]=result['id'];print('CREATED sprint',name,result['id'])
        if opts.dry_run:continue
        members=[r for r in read_csv('JIRA_IMPORT_WORK_ITEMS.csv') if r['Candidate_Sprint']==sid]
        keys=[issue_state.get(r['External_ID']) for r in members]
        if not all(keys):
            print('SKIP sprint assignment, missing issue keys:',sid);continue
        for i in range(0,len(keys),50):
            request('POST',f'/rest/agile/1.0/sprint/{sprints[name]}/issue',{'issues':keys[i:i+50]})
        print('Assigned',len(keys),name)
    if not opts.links:return
    # Blocker links are idempotent within this run via state. Jira may already have links from manual imports.
    linkstate_path=ROOT/'.jira_link_state.json'
    linkstate=set(json.loads(linkstate_path.read_text()) if linkstate_path.exists() else [])
    for row in read_csv('../planning/DEPENDENCIES.csv'):
        predecessor,successor=row['predecessor'],row['successor'];tokenid=f'{predecessor}>{successor}'
        if tokenid in linkstate:continue
        if predecessor not in issue_state or successor not in issue_state:continue
        if opts.dry_run:print('DRY link',tokenid);continue
        # 'Blocks' may have a different name on customized Jira instances; inspect issue link types first.
        request('POST','/rest/api/3/issueLink',{'type':{'name':'Blocks'},'inwardIssue':{'key':issue_state[successor]},'outwardIssue':{'key':issue_state[predecessor]}})
        linkstate.add(tokenid);linkstate_path.write_text(json.dumps(sorted(linkstate),indent=2))
    print('Synchronization completed; none of the sprints have been started or closed.')
if __name__=='__main__':main()
