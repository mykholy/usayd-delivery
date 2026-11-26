# Implementation gates for Codex

Build module by module. Each gate must be green before the next one starts. Never hand Codex “build 169 screens” as one task.

| Gate | Scope | Blocking approvals | Exit criteria |
|---|---|---|---|
| G0 Foundations | Design tokens v0.4, `usayd-ui.css` → component library, local fonts, RTL/LTR, light/dark, 44 px targets | None | Component stories for all 33+ components in AR/EN × light/dark; axe 0 serious |
| G1 Identity & consent | `UX-AUTH-*`, `UX-GLOB-001..004`, `UX-JR-02` | **O-01**, **O-04** | Minor limited mode enforced server-side; consent per purpose; guardian journey E2E incl. decline/expiry |
| G2 Public & booking | `UX-PUBLIC-*`, `UX-GLOB-002/003/005`, `UX-JR-01/03` | **O-02** (prices/“free”), owner content (photos, bios, legal) | No placeholder text in production; booking idempotent; DST gap/overlap tests |
| G3 Payments | `UX-GLOB-006/007`, `UX-LEARNER-029`, `UX-JR-04` | **O-01**, **O-02**, PSP per market | Immutable quote + expiry; webhook-only confirmation; no double charge |
| G4 Learning core | Learner today/plan/memory/study/revision, teacher day/briefing/report, `UX-JR-05/06` | **O-03** (video vendor), **O-06** (Quran source) | Licensed Quran text only; report autosave + conflict; provider fallback |
| G5 Supervision & admin ops | `UX-SUP-*`, admin ops, `UX-JR-08` | Scope model sign-off | 403 non-revealing; no self-approval; audit trail on every decision |
| G6 Mobile | `UX-MOBILE-*`, `UX-JR-09` | Draft retention period, batch sync contract | Offline queue, conflict UI, re-login keeps queue |
| G7 Competitions & AI | Competitions, appeals `UX-JR-07`, AI companion | **O-05**, **O-07** | Appeals across separate sessions; AI suggestions require teacher approval |
| G8 Finance & VPC advanced | Payroll, pay runs, VPC routing | **O-08** | Dual approval, dry run, rollback, audit evidence |

Before any gate: the endpoints it needs from `07_api/API_GAPS.md` are approved and added to OpenAPI, or the feature is behind a flag.

Every gate also needs: AR/EN × light/dark visual regression at 360/390/768/1024/1440, keyboard pass, and a manual TalkBack + VoiceOver pass on the gate’s critical journey.

---
## Gate additions (2026-11-23 remediation)
- **Gate A — contract approval:** a PROPOSED operation from `openapi.proposed.yaml` is merged into `openapi.yaml` only after tech-lead approval; record the approval in `DECISION_LOG.md`.
- **Gate B — owner decisions:** modules listed under “BLOCKS …” in `DECISION_REQUIRED_FROM_OWNER.md` stay behind their feature flag (`10_roadmap/FEATURE_FLAGS.csv`) until the named owner signs.
- **Gate C — evidence:** a module is “done” only with passing contract tests, the journey’s Gherkin scenarios, negative permission tests from `PERMISSIONS_MATRIX.md`, and AR/EN visual comparison. Static-design PASS is not module PASS.
