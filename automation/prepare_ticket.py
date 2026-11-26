#!/usr/bin/env python3
"""Prepare one ticket context for Gemini/Codex. Offline and read-only; no Jira side-effects."""
import argparse,json,re,sys
from pathlib import Path
R=Path(__file__).resolve().parents[1]
parser=argparse.ArgumentParser();parser.add_argument('task_id',help='USYD-T####');parser.add_argument('--output',type=Path,default=None)
a=parser.parse_args()
if not re.fullmatch(r'USYD-T\d{4}',a.task_id):raise SystemExit('Bad task ID')
p=R/'planning/tasks'/f'{a.task_id}.md'
if not p.is_file():raise SystemExit('Unknown ticket')
s=p.read_text(encoding='utf8');master=(R/'USAYD_GEMINI_CODEX_AUTONOMOUS_MASTER_PROMPT.md').read_text(encoding='utf8')
text=master+'\n\n# THIS EXECUTION: ONE TICKET ONLY\n\n'+s+'\n\nRead every referenced source file in full. Verify real Jira and repo state. Never claim a task is Done before real merged PR and verification.\n'
if a.output:a.output.write_text(text,encoding='utf8')
else:sys.stdout.write(text)
