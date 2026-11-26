# Global settings registry & admin governance

## Configuration domains
| Key / screen | Scope | Owner | Approval | Impact |
|---|---|---|---|---|
| `markets.*` | country | regional + compliance | dual for sales activation | catalogue/eligibility |
| `pricing.*` | country + program + plan | finance | financial dual approval | new quotes only |
| `localization.*` | locale + site | content admin | linguistic + academic/legal when needed | published web/app copy |
| `time.*` | user/teacher/region | user or ops | user update, scheduling audit | rendering/reminders |
| `video.*` | provider + environment + market | platform ops | dual approval live | new conference bindings |
| `payment.*` | merchant + country | finance/security | dual + PSP test | checkout eligibility |
| `teacher.compensation.*` | contract + location | finance/HR | dual approval | future pay snapshots |
| `supervision.*` | program + case type | platform admin | security | access policies |
| `ai.*` | program/model/version/purpose | academic+privacy | dual academic/privacy | recommendations & session AI |
| `competition.*` | market/cohort | contest+academic | academic and safeguarding | enrolment/rank/awards |
| `notifications.*` | locale+event+market | operations | content review | user communication |

## General settings forms
Every setting exposes current published value, inherited override, draft value, change rationale, field-level warnings, last editor, effective time, environment, test/preview, approve/publish and rollback. Config snapshots immutable with SHA256 and version. Unauthorized cross-region user sees redacted/nonexistent setting, not read-only secret.

## Configuration versioning
- Global default -> region/market -> program -> cohort -> teacher -> lesson override, with explicit precedence and conflict detection.
- Inherited UI shows "Inherited from global" and allows only permitted overrides.
- Sensitive settings require review; exception paths documented in ADR and bounded in time.
- All effectful changes are event-sourced into configuration audit/outbox and cached by version; invalidate stale requests safely.
- Admin UI preview can impersonate *context*, not impersonate a real learner identity (synthetic test fixtures only).

## Unknowns to resolve before launch
Legal registration/processor merchant profiles in each market; tax classification; approved Quran source; teacher employment relationship; data location/DPA; approved consent modes; admin break-glass procedures; acceptable provider feature degradation; official company bank account; domain/trademark; customer support hours.
