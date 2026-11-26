# Decisions required from the owner

Grouped by what they block. **Recommendations are proposals, not approvals.** Nothing below is marked accepted until the named owner signs it in `DECISION_LOG.md`.

## BLOCKS BACKEND FOUNDATIONS

### O-01 — Legal entity and eligible markets
- **Options:** Single entity for all markets · entity per region
- **Recommendation (not approved): one entity + per-market merchant profiles first**
- **Trade-offs:** Tax/VAT and refund law vary by entity
- **Depends on it:** Markets, checkout, legal pages, P-26, J05, J16
- **Safe temporary behaviour:** All markets off; waitlist only
- **Sign-off owner:** CEO + legal counsel
- **Accepted when:** Entity named; market list signed; legal texts published

### O-04 — Minors: who may enrol and how guardians are verified
- **Options:** Email/SMS OTP to guardian · ID document check · payment-card check · in-person/academy verification
- **Recommendation: decide per market; schema keeps `verification_method` open**
- **Trade-offs:** Stronger checks reduce fraud but add friction and data
- **Depends on it:** J02, P-02, P-32..P-34, P-50, UX-AUTH-002
- **Safe temporary behaviour:** Minors limited mode; no paid learning
- **Sign-off owner:** Legal/DPO
- **Accepted when:** Method per market + retention period recorded

### O-06 — Licensed Quran text source and academic authority
- **Options:** Licensed digital corpus · academic body’s own text
- **Recommendation: choose before any question bank or memory-map content**
- **Trade-offs:** Licence terms may restrict offline caching (FR-MOB-004)
- **Depends on it:** J08, J09, P-09, P-10, P-52, OC-07
- **Safe temporary behaviour:** References only; no text
- **Sign-off owner:** Academic lead + legal
- **Accepted when:** Licence + riwayah + approver recorded

### D-42 — Separate admin/teacher endpoints from public ones
- **Options:** Separate namespaces · shared endpoints with flags
- **Recommendation: separate (privacy by construction)**
- **Trade-offs:** More endpoints
- **Depends on it:** P-01, P-06, P-07, P-14, P-27, P-47
- **Safe temporary behaviour:** —
- **Sign-off owner:** Tech lead
- **Accepted when:** Approved in API review

## BLOCKS FEATURE IMPLEMENTATION

### O-03 — In-app video vendor (P0)
- **Options:** LiveKit · VideoSDK · Daily · external Meet/Zoom only
- **Recommendation: start with external links + one in-app vendor behind the adapter**
- **Trade-offs:** Capabilities (recording, region) differ
- **Depends on it:** J06, VPC screens
- **Safe temporary behaviour:** External meeting links
- **Sign-off owner:** CTO
- **Accepted when:** Vendor + regions + DPA signed

### O-05 — Recording and AI processing purposes/consent
- **Options:** Off by default · opt-in per purpose
- **Recommendation: off by default, opt-in per purpose with retention**
- **Trade-offs:** Less data for AI features
- **Depends on it:** J02, J06, J08, flags recording_v1 / ai_audio_analysis
- **Safe temporary behaviour:** Both off
- **Sign-off owner:** Legal/DPO
- **Accepted when:** Purpose texts + retention approved

### O-07 — Competition prizes
- **Options:** No material prizes · approved prize policy
- **Recommendation: no material prizes in pilot**
- **Trade-offs:** —
- **Depends on it:** J10, OC-10, G-12
- **Safe temporary behaviour:** Badges only
- **Sign-off owner:** Legal + academic
- **Accepted when:** Prize terms published

### O-08 — Payroll contract forms and minimum-wage rules
- **Options:** Per-lesson · hourly · salary · hybrid (FR-PAYROLL-001)
- **No recommendation — legal per jurisdiction**
- **Trade-offs:** Compliance risk
- **Depends on it:** J15, P-13, P-45, FR-SUP-012
- **Safe temporary behaviour:** Payroll off
- **Sign-off owner:** Finance + legal
- **Accepted when:** Contract templates approved per country

### D-24 — Duplicate routes → canonical implementations
- **Options:** Keep aliases as redirects · drop aliases
- **Recommendation: redirects /pricing → UX-GLOB-002, /admin/settings → UX-SUP-010**
- **Trade-offs:** —
- **Depends on it:** CANONICAL_ROUTES.csv
- **Safe temporary behaviour:** Build canonical only
- **Sign-off owner:** Tech lead
- **Accepted when:** Redirect list approved

### D-35 — Default age ranges for app styles
- **Options:** Kids 6–12 / Professional 13–59 / Simple 60+ · user choice only
- **Recommendation: defaults as proposed, always changeable**
- **Trade-offs:** —
- **Depends on it:** J17, kids_mode flag
- **Safe temporary behaviour:** Professional for all
- **Sign-off owner:** Product owner + academic
- **Accepted when:** Ranges approved

### D-39 — Break-glass access policy
- **Options:** —
- **Time-boxed, MFA, review ≤24 h**
- **Trade-offs:** Speed vs privacy
- **Depends on it:** P-41, UX-SUP-004, J14
- **Safe temporary behaviour:** Assigned officers only
- **Sign-off owner:** Safeguarding lead + security
- **Accepted when:** Policy approved

## BLOCKS PAID PILOT / RELEASE

### O-02 — Pricing, renewal and refund policy
- **Options:** Packages only · packages + credits (FR-PAY-008)
- **Recommendation: packages only for pilot; credits later**
- **Trade-offs:** Credits add wallet ledger work
- **Depends on it:** J05, P-23, P-31, P-40, OC-01, OC-03, FR-PAY-008
- **Safe temporary behaviour:** Prices hidden; checkout off
- **Sign-off owner:** Commercial lead
- **Accepted when:** Price books approved per market

### O-09 — Support hours and staffing
- **Options:** —
- **Publish real hours only**
- **Trade-offs:** —
- **Depends on it:** J14, OC-09
- **Safe temporary behaviour:** No SLA shown
- **Sign-off owner:** Ops
- **Accepted when:** Hours + escalation ladder

### D-44 — Brand tagline alluding to the narration about Usayd; any hadith text/reference on public pages
- **Options:** Keep tagline · change tagline
- **Recommendation: academic board approves exact wording before public launch**
- **Trade-offs:** Religious accuracy and tone
- **Depends on it:** UX-MOBILE-000, auth screens, footer, UX-PUBLIC-010 (OC-08)
- **Safe temporary behaviour:** Tagline kept in design; About story is an owner slot
- **Sign-off owner:** Academic board
- **Accepted when:** Wording + source approved

## CAN BE DEFERRED

### O-10 — Funding amount and tranche
- **Options:** —
- **—**
- **Trade-offs:** Scope of first release
- **Depends on it:** Roadmap
- **Safe temporary behaviour:** —
- **Sign-off owner:** Investors/CEO
- **Accepted when:** Release scope confirmed

### D-16 — Splash screen UX-MOBILE-000 (added)
- **Options:** Keep · remove
- **Keep (design ready)**
- **Trade-offs:** —
- **Depends on it:** UX-MOBILE-000
- **Safe temporary behaviour:** Native splash only
- **Sign-off owner:** Product owner
- **Accepted when:** Confirmed

### D-27 — KPI definitions on executive dashboard
- **Options:** —
- **Labelled proposals**
- **Trade-offs:** —
- **Depends on it:** UX-ADMIN-001, OC-12
- **Safe temporary behaviour:** Labelled “proposed”
- **Sign-off owner:** Owner
- **Accepted when:** Definitions signed

### D-36 — Kids badges catalogue
- **Options:** —
- **Private, non-monetary, teacher-awarded**
- **Trade-offs:** —
- **Depends on it:** UX-MOBILE-K08, OC-11, D-43
- **Safe temporary behaviour:** Empty state
- **Sign-off owner:** Academic
- **Accepted when:** Catalogue approved

### D-37 — Optional kids mascot with a face
- **Options:** No mascot · mascot
- **No mascot (current set has no faces)**
- **Trade-offs:** Brand/religious sensitivity
- **Depends on it:** Kids screens
- **Safe temporary behaviour:** Current faceless set
- **Sign-off owner:** Owner
- **Accepted when:** Decision recorded

### D-43 — Badges via existing achievements op
- **Options:** —
- **Use get__achievements**
- **Trade-offs:** —
- **Depends on it:** UX-MOBILE-K08
- **Safe temporary behaviour:** —
- **Sign-off owner:** Tech lead
- **Accepted when:** Approved

### Q-PIN — Kids guardian PIN: device-only or server
- **Options:** Device keychain only · server-verified
- **Recommendation: device-only (it gates settings, not data)**
- **Trade-offs:** Lost PIN recovery
- **Depends on it:** UX-MOBILE-K11
- **Safe temporary behaviour:** PIN feature hidden
- **Sign-off owner:** Product + security
- **Accepted when:** Decision recorded
