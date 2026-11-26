#!/usr/bin/env python3
"""Blueprint spec-audit only: does not claim application functionality."""
from pathlib import Path
from collections import Counter
import argparse,csv,re,yaml,json,sys
ROOT=Path(__file__).resolve().parents[1]
def csvrows(p):
 with (ROOT/p).open(encoding='utf-8-sig', newline='') as f:return list(csv.DictReader(f))
def audit():
 issues=[];stats={}
 def require(ok,message):
  if not ok:issues.append(message)
 req=csvrows('02_REQUIREMENTS/functional_requirements.csv');jira=csvrows('06_DELIVERY_JIRA/Jira_Import.csv');test=csvrows('07_QUALITY_SECURITY/test_cases.csv');screens=csvrows('05_UI_UX/screen_inventory.csv')
 spec=yaml.safe_load((ROOT/'04_ENGINEERING/openapi.yaml').read_text(encoding='utf-8'))
 counts={name:len(rows) for name,rows in [('requirements',req),('jira',jira),('test_registry',test),('screens',screens)]};stats.update(counts)
 ids={item['ID'] for item in req};jids={item['Issue ID'] for item in jira};uids={item['Screen ID'] for item in screens};tids={item['Test ID'] for item in test}
 for label,col,rows in [('FR','ID',req),('Jira','Issue ID',jira),('UX','Screen ID',screens),('Test','Test ID',test)]:require(len({x[col] for x in rows})==len(rows),f'duplicate {label} IDs')
 parents={j['Issue ID']:j for j in jira};require(len(parents)==len(jira),'duplicate issue IDs')
 for j in jira:
  if j['Parent ID']:
   require(j['Parent ID'] in parents, f"orphan issue {j['Issue ID']}")
   if j['Parent ID'] in parents:require(parents[j['Parent ID']]['Issue Type']=='Epic',f"non-Epic parent {j['Issue ID']}")
  if j.get('Requirement ID'):require(j['Requirement ID'] in ids or j['Requirement ID'] in uids, f"unknown FR/UX on Jira {j['Issue ID']}")
 for x in test:
  rid=x['Requirement ID']; valid=rid in ids or rid.startswith('E2E-') or (rid.endswith('*') and any(v.startswith(rid[:-1]) for v in ids))
  require(valid,f"unbound test {x['Test ID']}: {rid}")
 stories={x['Requirement ID'] for x in jira if x['Issue Type']=='Story' and x.get('Requirement ID')};require(stories==ids,f'FR/story mismatch missing={len(ids-stories)} extra={len(stories-ids)}')
 registered={x['Requirement ID'] for x in test if x['Requirement ID'] in ids};require(registered==ids,'Some FRs lack test registry entry')
 allops=[];spec_paths=spec['paths'];schemas=spec['components']['schemas'];require(spec['servers'][0]['url'].rstrip('/').endswith('.invalid'),'server placeholder changed without review')
 for path,methods in spec_paths.items():
  require(path.startswith('/api/v1/'),f'non v1 path {path}')
  for method,op in methods.items():
   if method not in ('get','post','put','patch','delete'):continue
   allops.append(op);require('operationId' in op,f'operation missing operationId: {path} {method}')
   required=set(re.findall(r'\{([^}]+)\}',path)); declared={p['name'] for p in op.get('parameters',[]) if p['in']=='path'}
   require(required<=declared,f'undeclared path parameters {method} {path}: {required-declared}')
   req_rsp=op.get('responses',{});require(bool(req_rsp),f'no responses {path} {method}')
   for response in req_rsp.values():
    for representation in response.get('content',{}).values():
     require('GenericItem' not in str(representation) and 'GenericList' not in str(representation),f'generic response still used {path}')
 for path in ('/api/v1/auth/register','/api/v1/auth/login','/api/v1/auth/refresh','/api/v1/webhooks/payments/{provider}','/api/v1/webhooks/video/{provider}'):
  for op in spec_paths[path].values():
   if isinstance(op,dict) and 'responses' in op:require(op.get('security')==[],f'Public/signed webhook endpoint BearerAuth inherited: {path}')
 opids=[x.get('operationId') for x in allops];require(len(opids)==len(set(opids)),'duplicate operationIds')
 refs=set()
 def walk(node):
  if isinstance(node,dict):
   for k,v in node.items():
    if k=='$ref' and isinstance(v,str):refs.add(v)
    else:walk(v)
  elif isinstance(node,list):
   for v in node:walk(v)
 walk(spec)
 for ref in refs:
  if ref.startswith('#/components/schemas/'):
   require(ref.split('/')[-1] in schemas, f'unknown $ref {ref}')
 stats.update({'openapi_paths':len(spec_paths),'openapi_operations':len(allops),'openapi_schemas':len(schemas),'gherkin_scenarios':sum(txt.read_text().count('  Scenario:') for txt in (ROOT/'07_QUALITY_SECURITY/gherkin').glob('*.feature')),'additional_hardening_tasks':sum('hardening' in j['Labels'] for j in jira)})
 required_files=['AGENTS.md','CLAUDE.md','PROMPTS/CODEX_BUILD_MASTER.md','PROMPTS/CLAUDE_FIGMA_EXECUTION.md','07_QUALITY_SECURITY/RELEASE_EVIDENCE_TEMPLATE.md','05_UI_UX/INTERACTION_CONTRACTS_v1.1.md']
 for file in required_files:require((ROOT/file).is_file(),f'missing handoff {file}')
 return issues,stats
if __name__=='__main__':
 errors,stats=audit();print(json.dumps({'passed':not errors,'summary':stats,'issues':errors},ensure_ascii=False,indent=2));sys.exit(0 if not errors else 1)
