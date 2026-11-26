# Threat model, privacy, minors and safeguarding specification

## Trust boundaries

1. Public website vs logged-in API; 2. learner vs teacher vs support vs academic vs finance admin; 3. API vs external vendor credentials; 4. lesson content and raw audio vs learning evidence; 5. public competition results vs identifiable minors; 6. AI model vs authoritative Quran source and immutable teacher decisions.

## Primary threats and mitigations

| Threat | Example | Design control | Verify |
|---|---|---|---|
| BOLA/IDOR | Student changes `learnerId` | policy checks on object, not client only | negative API tests |
| Teacher poaching | Spoken out-of-platform invitation | restricted chat/contact, contracts, service differentiation, consented reviewed AI alerts | human review no guarantee |
| Kid contact data exposure | Child name/phone shown in leaderboard | privacy-by-default pseudo/hidden and strict k-anonymity settings | UAT and pen test |
| Session intrusion | Shared conference link | ephemeral grants, host permissions, access gate; external provider limitations | SDK POC |
| Silent audio surveillance | Agent captures unconsented child | consent per purpose, listener disabled unless valid, visible notices and kill switch | end-to-end negative |
| AI false accusations | word WhatsApp in normal lesson | context, human adjudication, appeal, restricted disclosure | false positive evaluation |
| Quran text error | model invents verse | only verified licensed corpus; checksum/edition | tests and academic audit |
| Competition result manipulation | judge changes score for favored learner | immutable score versions, conflict declarations, double judges | score replay tests |
| Financial fraud | duplicate payment webhooks | signature, idempotency, ledger and dual approval | reconciliation tests |
| Prompt injection | transcript asks to reveal data | untrusted input isolation, structured output, least privilege | red-team dataset |
| Device/audio data leakage | recording URLs copied | signed TTL, private buckets, purpose-limited access, deletion | security tests |
| Denial of service | mass free trials or AI usage | bot detection, quotas, rate limits, spend ceilings | load/abuse tests |

## Data governance

Inventory purpose, legal basis/consent, processor, country of storage, retention, access role and deletion trigger for every data category. Store consent receipt with version, initiator, timestamp and allowed processing; user can withdraw optional purposes and no new audio analyses start. For minors follow applicable legal procedure and safer alternatives.

**Suggested retention categories pending counsel approval:** security logs 30–90d, support cases 6–12mo, optional session snippets 7–30d if appropriate and lawfully authorized, educational report for subscription duration + justified period, accounting records statutory retention per country. These are planning ranges, not legal authority. Never claim auto deletion from all vendor processors without verified API and DPA.

## Safeguarding

Identity vetting of teachers, verified references, teacher safeguarding policy, no private unsupervised messaging for minors, visible report action, trained response team, separation of children from public contest leaderboards and no public recordings. Report goes to role-authorized queue with time-sensitive escalation; don't ask child to gather evidence or publish personal details. Human staff decides disciplinary actions and follows appropriate reporting duties.

## Legal open items

Local business/education/religious licensing, data processing law and implementing rules, cross-border transfers (video/AI/cloud), minors' consent process by country, payments/consumer refunds/auto-renewal, contests and prize regulations, copyright of Quran media/tafsir/translation assets, employment contracts/minimum wage, teacher credential advertising claims. Obtain counsel sign-off, not inferred by engineering team.

## Security verification gate

Privacy/DPIA, access matrix, threat model signed; MFA and event audit, incident response, vendor DPA reviewed, pentest findings remediated, backups encrypted/restored, no secrets exposed in browser/mobile bundles, guardian and recording negative tests pass.
