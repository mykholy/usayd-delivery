#!/usr/bin/env python3
"""Offline/safe read-only verifier; no Jira/GitHub writes."""
from pathlib import Path
from collections import Counter
import csv,sys,re,hashlib,json
root=Path(__file__).resolve().parents[1]
def rows(p):
 with (root/p).open(encoding='utf-8-sig',newline='') as f:return list(csv.DictReader(f))
tasks=list((root/'planning/tasks').glob('USYD-T*.md'))
epics=rows('planning/EPICS.csv');backlog=rows('planning/MASTER_BACKLOG.csv')
report={'ticket_files':len(tasks),'epics':len(epics),'backlog_items':len(backlog),
 'source_files':len(rows('coverage/READY_SOURCE_SHA256.csv')),
 'sprints':len(list((root/'planning/sprints').glob('S*.md')))}
assert len(tasks)==707 and len(epics)==33 and len(backlog)==707,report
for row in rows('coverage/READY_SOURCE_SHA256.csv'):
 p=root/'source_original/usayd-academy-codex-package'/row['Relative_Path']
 assert p.is_file(),p
 assert hashlib.sha256(p.read_bytes()).hexdigest()==row['SHA256'],p
ids={p.stem for p in tasks}
assert len(ids)==707
for p in tasks:
 s=p.read_text(encoding='utf8')
 assert '## Production execution detail — reviewer checklist' in s,p
# forbid redistributed font binaries
assert not list((root/'source_original').rglob('*.woff2'))
print(json.dumps(report,ensure_ascii=False,indent=2))
