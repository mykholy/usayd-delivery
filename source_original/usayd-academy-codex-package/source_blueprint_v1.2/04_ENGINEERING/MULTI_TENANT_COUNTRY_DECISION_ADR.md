# ADR-012 — Multi-country single academy vs multi-tenant, chosen approach
Decision: **single academy/legal entity aware markets** at first; do not introduce generic multi-tenant tenant_id across every table without actual separate customer organizations. Use `market_id`, `legal_entity_id`, regional permissions, ledgers and configuration. Future B2B white-label is an extension with organization scoping only after a funded business requirement.

Reasons: simplest data governance, payment reconciliation and learner continuity; each market can have independent catalog, pricing, PSP merchant profile, tutor pool, legal terms and data retention without segregating every part as separate SaaS tenants.

Consequences: implement market-aware ABAC and audit now; future subsidiaries/legal entities require per-merchant ledger and cross-entity access controls; market does not equal timezone or language; learner may travel, buy for a different market subject to verification. No country-based IP hard-blocking unless legally required.
