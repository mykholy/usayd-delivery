#!/usr/bin/env python3
"""Offline/safe read-only verifier; no Jira/GitHub writes."""
from pathlib import Path
from collections import Counter
import csv,sys,re,hashlib,json
from source_integrity import index_variants, verify_bytes
root=Path(__file__).resolve().parents[1]
def rows(p):
 with (root/p).open(encoding='utf-8-sig',newline='') as f:return list(csv.DictReader(f))
tasks=list((root/'planning/tasks').glob('USYD-T*.md'))
epics=rows('planning/EPICS.csv');backlog=rows('planning/MASTER_BACKLOG.csv')
report={'ticket_files':len(tasks),'epics':len(epics),'backlog_items':len(backlog),
 'source_files':len(rows('coverage/READY_SOURCE_SHA256.csv')),
 'sprints':len(list((root/'planning/sprints').glob('S*.md')))}
assert len(tasks)==707 and len(epics)==33 and len(backlog)==707,report
manifest=rows('coverage/READY_SOURCE_SHA256.csv')
original={row['Relative_Path']:row['SHA256'] for row in manifest}
assert len(manifest)==len(original)==1183
variants=index_variants(json.loads((root/'automation/SOURCE_CSV_LF_VARIANTS.json').read_text(encoding='utf-8')),original)
assert len(variants)==31
integrity=Counter()
for path,expected in original.items():
 p=root/'source_original/usayd-academy-codex-package'/path
 assert p.is_file(),p
 integrity[verify_bytes(path,p.read_bytes(),expected,variants)]+=1
report['source_integrity']=dict(integrity)
report['source_archive_note']='LF variant means exact known normalized CSV bytes, not original raw archive bytes.'
ids={p.stem for p in tasks}
assert len(ids)==707
for p in tasks:
 s=p.read_text(encoding='utf8')
 assert '## Production execution detail — reviewer checklist' in s,p
# forbid redistributed font binaries
assert not list((root/'source_original').rglob('*.woff2'))
print(json.dumps(report,ensure_ascii=False,indent=2))
