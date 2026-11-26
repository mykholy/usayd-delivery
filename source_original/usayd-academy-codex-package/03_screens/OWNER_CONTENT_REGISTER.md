# Owner content register (CONTENT_REQUIRED)

`CONTENT_SLOTS.csv` has 40 CONTENT_REQUIRED slot instances on screens (earlier documents said 39 and 40; the measured number is used everywhere now). They group into the content items below, plus page-level owner content that has no inline slot.

| ID | Content | Screens | Owner | Source / rights | Safe state until supplied | Localization | Publish gate |
|---|---|---|---|---|---|---|---|
| OC-01 | Package prices per market (amount_minor + currency + tax flag) | UX-PUBLIC-001, UX-PUBLIC-003, UX-PUBLIC-004, UX-GLOB-002, UX-GLOB-006 | Commercial (O-02) | Approved price book version | Price area hidden; CTA “See prices” disabled with “Prices coming soon” — no number shown | AR/EN numerals per locale; currency exponent | Price book approved by finance + compliance (FR-GEO-010) |
| OC-02 | Legal entity name and registration details | UX-GLOB-006, UX-LEARNER-029 | Legal/CEO (O-01) | Company registration | Checkout disabled | Official AR + EN names | Legal sign-off |
| OC-03 | Renewal / price-change notice wording | UX-GLOB-007 | Pricing team (O-02) | Owner-written | Notice not sent; renewal requires explicit consent anyway | AR + EN reviewed | Commercial + legal review |
| OC-04 | Teacher display names, photos, bios, verified details | UX-PUBLIC-001, UX-PUBLIC-005, UX-PUBLIC-006, UX-LEARNER-006 | Each teacher + academic (FR-TCHR-002) | Teacher publication consent + verified credentials | Card shows initials avatar and “Profile coming soon”; no stock or generated faces | Bio in teacher’s language(s); no machine translation of religious claims | Teacher consent receipt + academic verification |
| OC-05 | Testimonials | UX-PUBLIC-001 | Marketing (D-26) | Real, consented, attributable | Section hidden | Original language + reviewed translation | Written consent of the author; minors never |
| OC-06 | Legal texts (terms, privacy, refunds, safeguarding, cookies) | UX-PUBLIC-012, UX-AUTH-001, UX-AUTH-002 | Legal (O-01) | Owner legal counsel | Sign-up blocked in that market (consent needs a versioned text) | AR + EN legally reviewed | Published version with effective date (P-26) |
| OC-07 | Quran text, ayah references, reciter audio | Every Quran block (UX-LEARNER-013/015/018/023, UX-TEACHER-010, UX-ADMIN-012/013) | Academic + legal (O-06) | Licensed corpus + riwayah | Reference placeholder only; never generated text | Arabic only for text; translation of meaning only from licensed source | Academic authority approval |
| OC-08 | About / academic standards / how it works copy | UX-PUBLIC-007, UX-PUBLIC-010 | Academic + marketing | Owner-written | Page shows structure without claims | AR + EN | Academic sign-off for any claim |
| OC-09 | Support hours, SLAs, contact channels | UX-PUBLIC-011, UX-LEARNER-031, UX-TEACHER-017 | Ops (O-09) | Staffing plan | No SLA promised; ticket form only | AR + EN | Ops sign-off |
| OC-10 | Competition prizes and terms | UX-PUBLIC-008, UX-LEARNER-021, UX-ADMIN-032 | Legal + academic (O-07) | Prize policy | Rewards section hidden; badges only | AR + EN | Legal review of material prizes (FR-CONTEST-010) |
| OC-11 | Kids badge catalogue and award rules | UX-MOBILE-K08, UX-LEARNER-026 | Academic (D-36) | Academic design | Empty state “Your stars will appear here” | AR + EN, child-friendly | Academic approval |
| OC-12 | Approved KPI definitions | UX-ADMIN-001, UX-ADMIN-039 | Owner (D-27) | Owner definitions | KPIs labelled “proposed definition” | AR + EN | Owner approval |

Nothing in this list may ship as sample text: production builds hide the slot and show the safe state.
