# Cross-border pricing, FX, billing and tax — implementation/decision contract

## Critical distinction
Shown price is **not** automatically the final charge in a currency the payment provider cannot accept. Price-book amount, charged currency and settlement account are separately configured and validated. A resident of KSA can be shown a SAR quote **only after** the approved merchant profile supports SAR charging for that legal entity. Otherwise show clear alternative charge currency and obtain affirmative acceptance, or disable checkout.

## Required PSP configuration per market
`merchant_profile_id`, `country`, `legal_entity_id`, `supported_charge_currencies[]`, `supported_payment_methods[]`, `settlement_currency`, `fee_plan_version`, `refund_currencies[]`, `tax_profile_id`, `webhook_secret_ref`, `enabled`, `last_live_test_at`. Separate sandbox/live keys in secrets manager. Do not allow one country's profile to be used automatically for another country's merchant.

## Server checkout pipeline
1. Resolve user-selected market (not IP alone) and plan eligibility.
2. Validate country status active, target package and verified billing country.
3. Resolve approved price book row version; build quote with `amount_minor`, `currency`, `tax_minor`, `discount_minor`, `total_minor`, `expires_at`, service period, FX disclosure (if applicable), legal merchant.
4. Check active merchant profile supports charge currency; preflight payment method; return payment intent with idempotency key.
5. PSP handles card data; callback alone isn't payment success. Verify signed webhook + amount/currency/merchant/quote, unique event dedup, ledger transaction idempotency.
6. Generate invoice and entitlement only after authoritative confirmed settlement/authorization per payment policy. Reconcile daily.
7. Refund uses original transaction currency, provider refund rules and immutable adjustment entries; do not mutate paid ledger rows.

## FX model
- **Preferred:** fixed local price books approved by finance; change with effective-dated price version and customer notice.
- **Optional fallback:** show indicative FX only, labeled estimate; charge amount must be confirmed with PSP. FX source/rate/time/rounding stored, and policy defines acceptable staleness and spreads.
- No use of a volatile spot rate to update subscriptions silently; no multi-currency sum without conversion with rate-date provenance.
- Minor units: EGP=2, SAR=2, AED=2, QAR=2, KWD=3, BHD=3, USD=2, EUR=2. Encode currency precision in metadata and verify against updated ISO 4217.

## Tax/legal gates
No universal VAT assumption. Taxability and marketplace nexus depend on merchant entity, student residency and service classification. Finance/legal must approve tax profiles for each launched market before taking payments. Do not claim regulatory compliance from implementation alone.

## Fraud/risk and difficult cases
- Price overridden between quote and payment → honor valid quote if policy permits, otherwise reject with transparent re-quote (never surprise charge).
- Duplicate webhook, delayed webhook after order cancellation, forged webhook → no duplicate entitlement or invoice, verified reconcile.
- FX charge dispute and partial refund → original amount_minor/currency, explicit fee responsibility.
- Staff attempts unpublished discount → deny and audit; 4-eyes approval for promo above threshold.
- Charge currency not PSP-supported → checkout unavailable with no shadow conversion.
- User profile country differs from card country → verification flow, do not block legitimate travelers by IP.
- KWD/BHD 3 decimals; formatting, totals and payment callback exact equality.
- Teacher payroll currency separate from customer charge, with effective-dated FX and jurisdiction controls.

Sources: https://support.paytabs.com/en/support/solutions/articles/60000712880-how-to-switch-between-profiles-based-in-different-regions-within-your-integration- ; https://docs.stripe.com/currencies ; https://developers.paymob.com/paymob-docs/getting-started/overview
