# COPY TO CODEX — INDEPENDENT QUALITY RELEASE AUDIT

Act as skeptical independent QA lead. Check the actual implementation against `AGENTS.md`, `SRS.md`, every P0 Requirement ID, critical `UX` IDs, the OpenAPI, Gherkin scenarios and release gate. Do not implement new features before establishing defects and reproduction steps. Run install/build/lint/unit/integration/E2E/mobile tests and vendor sandbox smoke where credentials available; distinguish test not run from test passed.

Security focus: IDOR/BOLA, role escalation, missing guardian consent, unsafe voice processing, stale video join token, forged/replayed payment and video webhook, duplicate booking/credit, teacher payroll replay, exam timeout/retry, contest appeal integrity, leaderboard minors privacy, unsafe Quran text provenance, AI outputs bypass teacher, wrong timezone/DST, queue retry, backups and incident response. Include Arabic/English RTL, low bandwidth, Android/iOS permissions and WCAG 2.2 AA.

Output: machine-readable defect report (severity, reproduction, actual vs expected, affected requirement/UX/API, fix evidence), executed commands/results, coverage by requirement, unresolved blockers and GO/NO-GO. Never call a checklist execution without running it.
