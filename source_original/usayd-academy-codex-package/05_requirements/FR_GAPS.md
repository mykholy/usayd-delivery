# FR gaps — revalidated (2026-11-23)

The 19 functional requirements without a mapped screen were re-checked against the current screens, `openapi.yaml` and `openapi.proposed.yaml`. FR IDs unchanged; every change has a reason.

| FR | Classification (2026-11-23) | Where | Reason |
|---|---|---|---|
| `FR-IAM-010` | screen enhancement | UX-GLOB-004, UX-SUP-011 | Translated validation/notification catalogues + policy text versions (getLegalDocument P-26). |
| `FR-CURR-004` | screen enhancement — BLOCKED O-06 | UX-TEACHER-011, UX-LEARNER-012 | Ayah-range picker bound to the licensed corpus. |
| `FR-CURR-005` | screen enhancement (was “new screen”) | UX-LEARNER-028 + listLibraryItems (P-18) | UX-LEARNER-028 now binds the library-items proposal (video/audio/document) — no new screen needed. |
| `FR-BOOK-007` | MAPPED (was “screen enhancement”) | UX-GLOB-005, UX-LEARNER-008, UX-ADMIN-015 + createSlotHold (P-30) | DST gap/overlap handled in J04 with dst_resolution. |
| `FR-BOOK-008` | backend-only | — | Provider binding per lesson; provider chip on lesson cards already designed. |
| `FR-PAY-008` | new screen — OWNER_DECISION_REQUIRED (O-02) | — | Wallet/credit ledger not designed: whether v1 sells credits is a commercial decision; no financial product invented. |
| `FR-ASMT-004` | screen enhancement | UX-LEARNER-008, UX-TEACHER-010 | Live oral exam = booking type + rubric result. |
| `FR-CONTEST-004` | deferred | UX-LEARNER-020 (coming soon) | Team fairness rules first (O-07). |
| `FR-MEDIA-003` | screen enhancement | UX-TEACHER-007, UX-LEARNER-031 + createUpload (P-43) | Scan states pending/clean/removed_by_scan. |
| `FR-CRM-006` | screen enhancement | UX-ADMIN-033/034 | Win-back with opt-out; adults only. |
| `FR-ADMIN-009` | MAPPED (confirm local policy fields) | UX-GLOB-010..013 | Covered by market + price-book screens. |
| `FR-SEC-002` | backend-only | — (+ P-43 signed uploads) | Private buckets, signed URL TTL, encryption. |
| `FR-SEC-003` | backend-only | — | UI shows 429 copy with retry time. |
| `FR-SEC-007` | backend-only | — | Monitoring/alerts/incident playbooks. |
| `FR-SEC-008` | backend-only | — | Threat model. |
| `FR-GEO-012` | screen enhancement | UX-GLOB-001, UX-GLOB-004 | City/IANA picker enforced when the country has >1 zone. |
| `FR-I18N-002` | backend-only / design-system rule | — | Logical properties + mirrored icons; verified by AR/EN regression renders. |
| `FR-VPC-007` | screen enhancement | UX-VPC-008 | Manual override for future lessons with invalidation preview + dual approval. |
| `FR-SUP-012` | screen enhancement (was “new screen”) — BLOCKED O-08 | UX-TEACHER-016 + existing getCompensationPreview | An operation already exists (`GET /teachers/me/compensation-preview`); the simulator is an enhancement of the pay-statement screen once contract rules are approved. |

Totals: screen enhancement 9 · backend-only 5 · MAPPED 2 · new screen 1 · deferred 1 · backend-only / design-system rule 1.
Changes vs 2026-11-22: FR-CURR-005 and FR-SUP-012 move from “new screen” to “screen enhancement” (an operation or screen already exists); FR-BOOK-007 and FR-ADMIN-009 are now mapped. Only FR-PAY-008 (wallet) remains a possible new screen, and it is an owner decision (O-02).
