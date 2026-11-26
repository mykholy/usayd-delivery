# Smart Quran Academy — Final Specification Handoff v1.2 (21 November 2026)
**Status:** Specification complete enough for phased design and implementation; **not yet a deployed/production-certified product**. Previous v1.1 materials remain, with v1.2 authoritative for conflicting rules.

## Non-negotiable decisions
1. **All people enroll as learner**; no compulsory parent dashboard at registration. A minor needs legally sufficient guardian authorization and age-appropriate controls, without treating a minor's own checkbox as guardian consent.
2. **Global-aware:** country availability, display currency, charge currency, settlement currency, language and timezone are separate settings. IP geolocation suggests only; user controls country and timezone. Charge is an explicit verified checkout quote.
3. **Two languages:** complete Arabic RTL and English LTR UI, transactional notices, errors, validation, accessibility and design variants. Quranic content from vetted licensed corpus, never machine-translated.
4. **Admin Video Provider Console:** configure/test/switch providers at an effective time for new lessons; existing active session never silently migrates. Provider capabilities not interchangeable; recording/raw audio AI fail closed.
5. **Supervisors:** regional, academic, quality, safeguarding, contests, operations, finance, support, localization, security; effective scope + object ownership + assigned work + justified purpose. No self-approval of sensitive actions.
6. **Retention features:** challenges/competitions, AI-assisted review and mastery tracking, teacher continuity, explicit fair leaderboards, privacy-preserving minor participation.
7. **Teacher remuneration:** contract versioning with fixed monthly, per session, per teaching hour, per shift and hybrid rules, immutable calculation snapshots and auditable dispute/approval.
8. **API-first:** `/api/v1`, OpenAPI contracts for web and mobile, typed error codes, fully tested internationalization, monetary integer minor units, ISO and IANA identifiers.
9. **Human academic control:** AI drafts have provenance, confidence and limitations; teachers approve study plans and assessment; Quran content and contest rulings never made solely by AI.

## Priority execution order
**Sprint 0 (architecture/validation):** ADRs, regulatory gates by market, qualified academic lead, PSP/currency verification, providers PoC, Figma foundation, Jira import dry run.
**Foundation:** Learner identity/consent, markets, locale, pricing catalogue, time preferences, RBAC scopes + audit, versioned API.
**Education Core:** scheduling, lessons, checkout, teacher assignment and compensation, learning progress.
**Experience:** premium learner/teacher/supervisor/admin web; assessments; competition basic; notifications.
**Intelligence:** gated AI recommendations and permitted conversation review; data retention and evaluation.
**Scale:** Flutter, provider expansion, markets, sophisticated competitions and adaptive assessment.

## Acceptance requirements of every deliverable
Story ID + rationale + user flow + screen ID + API schema + permissions + audit event + validation/error/empty/offline/RTL/EN states + automated test evidence + reviewer; no "Done" based on screenshots or prose.

## Master document map
- `10_GLOBALIZATION/COUNTRY_MARKET_CURRENCY_PRICING.md`: geography and price model
- `10_GLOBALIZATION/TIMEZONE_SCHEDULING_DST.md`: temporal domain
- `10_GLOBALIZATION/LOCALIZATION_AR_EN.md`: RTL/LTR and copy policy
- `10_GLOBALIZATION/PAYMENTS_FX_TAX.md`: quoting and reconciliation
- `11_PLATFORM_ADMIN/VIDEO_PROVIDER_CONSOLE.md`: admin provider switching
- `11_PLATFORM_ADMIN/SUPERVISOR_RBAC_WORKFLOWS.md`: supervisor permissions
- `11_PLATFORM_ADMIN/CONFIGURATION_REGISTRY.md`: system settings and audits
- `12_USER_JOURNEYS/USER_STORIES_AND_ACCEPTANCE.md`: detailed stories and flows
- `12_USER_JOURNEYS/FLOW_MATRIX.md`: scenario-to-screen/API/test matrix
- `12_USER_JOURNEYS/diagrams/`: Mermaid source diagrams
- `13_PREMIUM_UX/DESIGN_DIRECTION_AND_UI_SPEC.md`: visual design and screen details
- `13_PREMIUM_UX/CLAUDE_FIGMA_FINAL_BRIEF.md`: executable prompt for Claude/Figma
- `14_RELEASE_QA/INTERNATIONALIZATION_TEST_PLAN.md`: 100+ geographic/locale/provider cases
- `14_RELEASE_QA/PRODUCTION_RELEASE_GATE.md`: release criteria
- `PROMPTS/CODEX_EXECUTION_FINAL_v1.2.md`: Codex delivery prompt
- `06_DELIVERY_JIRA/Jira_Import.csv`: expanded backlog
- `04_ENGINEERING/openapi.yaml`: extended API contract draft

## Source-of-truth precedence
Product and scope: this file + v1.2 global/console specs; API: OpenAPI; UI: screen inventory + premium UX; test: requirement CSV + test registry; Jira: import CSV. If conflict persists: create ADR, do not guess in security, legal, Quranic content or billing.
