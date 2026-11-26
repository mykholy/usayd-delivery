# Source-level blockers and release gates

The source states **CONDITIONAL GO** for backend foundations; NOT an unrestricted GO for all business features. Source references: `DECISION_REQUIRED_FROM_OWNER.md`, `11_qa/HANDOFF_READINESS_REPORT_AR.md`, `10_roadmap/FEATURE_FLAGS.csv`, `08_data_model/STATE_ALIGNMENT.md`.

- O-01 legal entity/markets: keep markets off, waitlist only until signed.
- O-02 pricing/refund: no paid checkout/renewals until signed.
- O-03 video provider: external links may be piloted, in-app recording/provider routing requires approved PoC, DPA and capability matrix.
- O-04 guardian verification: minors limited, no paid/live sensitive actions before verified consent.
- O-05 recording/AI processing: off by default; purpose-specific consent and retention.
- O-06 Quran source license: no Quran text rendering from memory/generation or unapproved datasets.
- O-07 prizes: no monetary/physical prizes without policy.
- O-08 teacher contracts/payroll: payroll disabled until legal approval.
- O-09 support commitments / O-10 funding: prelaunch readiness decisions.
- D-42: approve separation of admin/teacher namespaces and guest security per endpoint before scaffolding public/auth APIs.
- D-24/35/36/37/39 and further D-series: maintain explicit decision log.

All `openapi.proposed.yaml` operations require *technical* review before being promoted to baseline. Check guest endpoints individually to avoid accidentally inheriting global bearer requirements. Resolve 8 state alignment mismatches first.

Go/no-go must be evaluated for EACH module independently; backend foundation may proceed while monetization, Quran content, and minor verification stay off.
