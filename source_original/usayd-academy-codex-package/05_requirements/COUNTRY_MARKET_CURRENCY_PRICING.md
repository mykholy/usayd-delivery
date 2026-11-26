# Multi-country business model, market availability and localized pricing

## 1. Definitions (do not conflate)
| Term | Storage | Usage |
|---|---|---|
| `country_detected` | nullable ISO 3166-1 alpha-2 | IP-derived initial **suggestion** only; not financial/legal identity |
| `country_selected` | ISO alpha-2 | user-selected storefront catalog, changeable |
| `billing_country` | validated ISO alpha-2 | PSP eligibility, invoices, applicable compliance/taxes; may differ from detected |
| `service_region` | configured enum | allowed teacher pools, lesson operations, data policies |
| `user_locale` | `ar` / `en` | translation language; never automatic proof of nationality |
| `user_timezone` | IANA ID | calendar conversion and notifications, independent of locale |
| `display_currency` | ISO 4217 | visible price, not necessarily charged |
| `charge_currency` | ISO 4217 | immutable customer checkout quote + PSP request |
| `settlement_currency` | ISO 4217 | merchant account PSP remittance currency |

## 2. Launch sequencing (recommendations, not legal approval)
| Tier | Countries | User currency suggestion | Primary IANA timezone suggestion | Status at plan date |
|---|---|---|---|---|
| Wave A pilot | EG Egypt | EGP | Africa/Cairo | Disabled until licensing/payment/operations signed off |
| Wave A pilot | SA Saudi Arabia | SAR | Asia/Riyadh | Disabled until cross-border PSP and compliance approved |
| Wave B | AE UAE | AED | Asia/Dubai | Waitlist/interest capture until approved |
| Wave B | KW Kuwait | KWD | Asia/Kuwait | Waitlist/interest capture until approved |
| Wave B | QA Qatar | QAR | Asia/Qatar | Waitlist/interest capture until approved |
| Wave B | BH Bahrain | BHD | Asia/Bahrain | Waitlist/interest capture until approved |
| Wave B | OM Oman | OMR | Asia/Muscat | Waitlist/interest capture until approved |
| Wave C | GB/US/CA + selected EU | GBP/USD/CAD/EUR | MUST ask city/timezone; countries have multiple zones | Research and licensing gates first |

**Important:** the country list is a proposed sales roadmap, not proof that the Egyptian merchant entity may legally sell and settle in every territory. Foreign-currency display does not guarantee merchant acceptance or settlement. Admin must explicitly enable a market only after legal/PSP checks.

## 3. Marketplace state machine
`draft -> compliance_review -> payment_testing -> active -> paused -> retired`; `retired` hides new acquisition but does not cancel legitimate prior obligations. Every status change has effective_at, actor, reason, audit evidence and rollback window. Regional manager proposes; legal/finance authorized approver activates, with two-person control.

## 4. Country determination UX
1. Initial page: accept browser locale for **language hint**; optional coarse IP country suggestion from server with notice.
2. If country hint low confidence, unknown, VPN/proxy, or unsupported, show market selector rather than assuming.
3. Explicit selector persists in user profile (signed in) or first-party preference (guest); user can change country any time before checkout.
4. Selected market determines **available** plans and market-specific catalogue prices, never an automatic exchange rate formula without an approved rule.
5. If market unavailable: communicate waitlist, no fake price, no payment capture. Existing memberships use a distinct entitlement policy.
6. On checkout, validate billing country, PSP methods, tax rules and merchant eligibility. Never infer billing residence purely from IP.
7. Returning visitor: selected country > saved preference > coarse IP suggestion > global selection. UI explains "Country: Saudi Arabia · Currency: SAR" with change action.
8. Market-selector modal accessible by keyboard/mobile/RTL; prevent self-changing a running paid invoice.

## 5. Price catalogue & administrative versioning
Normalized entities: `countries`, `markets`, `market_programs`, `price_books`, `price_book_items`, `promotions`, `coupon_rules`, `tax_profiles`, `quote_snapshots`, `exchange_rates`, `provider_merchant_accounts`.

Price row keys: `{market_id, program_id, package_id, currency_code, billing_cycle, effective_from, effective_to, audience_segment, promo_id?}`. No overlapping active intervals for same key. Prices are amount_minor integer; currencies carry correct ISO fractions: EGP/SAR/AED/QAR/OMR/USD/EUR/GBP have 2; KWD/BHD have **3**. No binary float for money; `Money` value object always carries currency and scale. Distinguish per-seat pricing and group capacity.

**Illustrative pricing entries — investor hypotheses, not market-validated or published:**
- EG EGP: `8 x 30min private = 799.00 EGP`, charge EGP only if supported.
- SA SAR: `8 x 30min private = 79.00 SAR`, charge SAR only after approved PSP profile.
- AE AED: `8 x 30min private = 85.00 AED` waitlist only until activated.
- KW KWD: `8 x 30min private = 7.500 KWD` waitlist only until activated.
These illustrative amounts are **not** derived from an official FX feed and must not be published without product/finance approval. Country prices must be A/B tested against teacher/payments/AI costs.

## 6. Admin market console — UX requirements
Screens: country table with active/pending state; country edit; price matrix; preview as guest in country+locale+timezone; bulk price copy in draft only; price change impact analysis; publication approval; provider eligibility; payment testing; tax profiles; rollback and audit history.

Actions: add country, set supported locales/currencies/timezones, bind pricing book and legal entity, schedule activation, pause sales, set waitlist; dry-run storefront preview and checkout validation; two-person publish.

Permissions: market manager can draft; finance may approve prices; compliance approves geographic launch; super-admin may assign roles but may not bypass two-person approval in production. Sensitive change requires MFA and audit.

## 7. Changes and renewals
- New price publication does not mutate existing invoice/quote; configurable grandfathering for active contracts.
- Renewals use explicitly selected pricing policy (grandfather/notice/new price), customer notice and jurisdictional consumer protection checks.
- Quotes have `expires_at`, version ID, tax breakdown, charged currency, legal merchant; final server-side revalidation before payment initiation.
- Refunds and credits use original charge currency and audited original transaction; never refund converted arbitrary display figure.
- Corporate/group prices use separate price books with approval; do not contaminate public plan price.

## 8. Product analytics
Events: `geo_hint_shown`, `market_selected`, `market_unavailable`, `price_viewed`, `quote_created`, `quote_expired`, `checkout_started`, `payment_success`, `renewal_charged`, `currency_mismatch`, all with country/market/currency at event time (no raw IP). Funnel and revenue segmented by *market + billed currency + acquisition cohort*; aggregates convert to reporting currency only with stored effective FX rates and rate date.

## 9. Non-negotiable negative scenarios
Unknown country; VPN; market paused after cart; KWD 3-decimal invoice; switch EG→SA at checkout; SA card rejected for EGP transaction; expired quote; VAT/tax change; duplicate PSP webhook; unavailable payout corridor; timezone different from country; refund after rate change; localization untranslated currency symbol; mixed-currency promotions.

## Sources / checks
- Unicode currency formatting: https://www.unicode.org/reports/tr35/tr35-numbers.html
- PayTabs regional merchant profiles: https://support.paytabs.com/en/support/solutions/articles/60000712880-how-to-switch-between-profiles-based-in-different-regions-within-your-integration-
- Paymob docs: https://developers.paymob.com/paymob-docs/getting-started/overview
- Stripe currency guidance (illustrative, not evidence of Egyptian account eligibility): https://docs.stripe.com/currencies
