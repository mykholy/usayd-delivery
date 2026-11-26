#!/usr/bin/env python3
"""Release package source validation only; does not validate an implemented app."""
from pathlib import Path
import csv, json, re, sys, zipfile
import yaml
from collections import Counter
ROOT=Path(__file__).resolve().parents[1]
def rows(rel):
    with (ROOT/rel).open(encoding='utf-8-sig',newline='') as f:
        return list(csv.DictReader(f))
def validate():
    errors=[]; counts={}
    def check(ok,msg):
        if not ok: errors.append(msg)
    api=yaml.safe_load((ROOT/'04_ENGINEERING/openapi.yaml').read_text(encoding='utf-8'))
    operations={}
    for p,verbs in api['paths'].items():
        for m,op in verbs.items():
            if m.lower() in ('get','post','put','patch','delete'):
                operations[(m.upper(),p)]=op.get('operationId')
    cases=rows('14_RELEASE_QA/INTERNATIONAL_E2E_SCENARIOS.csv')
    screens=rows('05_UI_UX/screen_inventory.csv')
    frames=rows('13_PREMIUM_UX/FIGMA_FRAME_MANIFEST.csv')
    flows=list((ROOT/'12_USER_JOURNEYS/diagrams').glob('*.mmd'))
    graphs=list((ROOT/'12_USER_JOURNEYS/diagrams').glob('*.svg'))
    mappings=rows('13_PREMIUM_UX/SCREEN_TO_API_TRACE_v1.2.csv')
    # Every screen must be supported in the UX catalogue and the API contract.
    screen_ids={s['Screen ID'] for s in screens}
    check(len(screen_ids)==len(screens),'Duplicate screen ID')
    check(len(operations)==121,'OpenAPI operation count changed')
    check(len(api['paths'])==109,'OpenAPI path count changed')
    check(len(api['components']['schemas'])==194,'OpenAPI schema count changed')
    check(len(cases)==60,'E2E scenario count changed')
    check(len(frames)==640,'Figma frame manifest count changed')
    check(len(flows)==24,'Mermaid diagram count changed')
    check(len(graphs)==6,'SVG diagram count changed')
    check(len(mappings)>=27,'Insufficient screen-to-API evidence')
    # Inspect row structures to guard against misconfigured traceability.
    for i,m in enumerate(mappings,1):
        sid=m.get('Screen ID') or m.get('screen_id')
        check(sid in screen_ids,f'Unknown traced screen at {i}: {sid}')
        method=m.get('HTTP') or m.get('Method') or m.get('method')
        path=m.get('OpenAPI path') or m.get('API Path') or m.get('Path') or m.get('path')
        check((str(method).upper(),str(path)) in operations,f'Unknown traced API at row {i}: {method} {path}')
    for name in ['README_AR.md','AGENTS.md','CLAUDE.md','INDEX.html','13_PREMIUM_UX/PREMIUM_INTERACTIVE_REFERENCE.html','13_PREMIUM_UX/CLAUDE_FIGMA_FINAL_BRIEF.md','PROMPTS/CODEX_EXECUTION_FINAL_v1.2.md','14_RELEASE_QA/PRODUCTION_RELEASE_GATE.md','09_EXPORTS/Executive_Handoff_v1.2_AR.pdf']:
        check((ROOT/name).is_file(),f'Missing {name}')
    pdf=ROOT/'09_EXPORTS/Executive_Handoff_v1.2_AR.pdf'
    check(pdf.stat().st_size>15000,'Summary PDF empty')
    # Markdown relative-link existence for explicitly linked local paths; skip dynamic anchors.
    missing=[]
    rx=re.compile(r'(?<!!)\[[^\]]+\]\(([^)]+)\)')
    for f in ROOT.rglob('*.md'):
        for raw in rx.findall(f.read_text(encoding='utf-8-sig')):
            link=raw.split('#')[0].strip()
            if not link or link.startswith(('https://','http://','mailto:','#')): continue
            if ' ' in link: link=link.split(' ')[0]
            if not (f.parent/link).exists(): missing.append((str(f.relative_to(ROOT)),link))
    check(not missing,f'Missing local links: {missing[:12]}')
    counts.update(openapi_operations=len(operations),openapi_paths=len(api['paths']),openapi_schemas=len(api['components']['schemas']),e2e_scenarios=len(cases),figma_planned_frames=len(frames),mermaid_flows=len(flows),svg_diagrams=len(graphs),screen_api_trace=len(mappings),markdown_link_missing=len(missing))
    return errors,counts
if __name__=='__main__':
    errors,counts=validate()
    print(json.dumps({'passed':not errors,'counts':counts,'issues':errors},ensure_ascii=False,indent=2))
    sys.exit(0 if not errors else 1)
