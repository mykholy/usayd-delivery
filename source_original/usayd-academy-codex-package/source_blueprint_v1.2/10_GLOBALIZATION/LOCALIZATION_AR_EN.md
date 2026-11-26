# Bilingual Arabic and English: i18n, RTL/LTR and semantic content

## Separation of preferences
- `locale` = `ar` or `en` (language); `country` market; `timezone_id`; `currency` selected from approved price book. Different fields and independent settings.
- Initial preference: stored signed-in locale > explicit guest selector > URL path (`/ar` `/en`) > browser Accept-Language hint > `ar` fallback.
- Persist locale in user profile; server API error codes stable (e.g. `MARKET_NOT_AVAILABLE`) and localized UI maps. Backend email/SMS templates choose recipient locale at send time.
- All native screens, Flutter, admin and embedded pre-join screens support RTL/LTR. Direction switches at document/screen root. Dates and money are formatted with ICU/CLDR, not string replacement.
- English URLs and Arabic URLs are language-specific with `hreflang`, canonical and translated metadata. Content CMS supports draft/publish per locale with explicit missing-translation fallback policy.

## Quranic content policy
- Quran text is canonical Arabic and never machine-translated in place. Approved translation/tafsir and narration labeled with source/license, language and edition; preserve verse indexing and diacritics.
- AI must not generate authoritative Quranic wording or corrected verse text; fetch verified dataset via secure content service and compare against approved text.
- Numeral shaping preference can be configured; use Unicode bidi isolation for phone, email, numeric invoice and Arabic mixed sentences.

## Component and UX acceptance
- Navigation mirrors, progress meter position and directional arrow icons mirror when semantic; play, logo, Quran text and brand marks do NOT mirror.
- Drawer enters on logical start side, not hardcoded left; breadcrumbs/collapse arrows respect direction. Table numbers align on same numeric column using bidi-safe formatting.
- Error messages and screen-reader labels fully translated; pluralization uses ICU MessageFormat (`one`, `two`, `few`, `many`, `other` where applicable).
- Number formatting examples: `Intl.NumberFormat('ar-EG',{style:'currency',currency:'EGP'})`; KWD uses 3 decimals; `ar-SA` and `en-SA` show same charge amount using locale-appropriate punctuation.
- Human translators review marketing claims, payment/refund legal language, teacher qualifications and AI disclaimers; no AI-only final legal text.
- Accessibility WCAG 2.2 AA target: contrast measured for actual combinations, proper focus indicators, keyboard operation, input errors, reduced-motion, responsive text zoom, captions where appropriate, touch targets, zoomed Arabic diacritics.

## Content localization workflow
`source draft -> translation draft -> linguistic review -> legal/academic review (if relevant) -> preview AR+EN -> publish -> versioned rollback`.
Roles: translator can draft not self-publish legal terms; academic reviewer authorizes Quran/pedagogical content; content admin publishes approved variants.

## Full string namespaces (required, not optional)
`auth.*`, `profile.*`, `market.*`, `pricing.*`, `payment.*`, `booking.*`, `timezone.*`, `video.*`, `teacher.*`, `learning.*`, `ai.*`, `assessment.*`, `competition.*`, `support.*`, `supervision.*`, `settings.*`, `errors.*`, `notifications.*`, `consent.*`, `privacy.*`, `reports.*`. Run CI lint comparing AR and EN key sets and placeholder/plural conformity.

## Test scenarios
- Full route and navigation screenshot on AR RTL and EN LTR at 360/390/768/1440 widths.
- Sidebar, calendars, tables, chart legends, graphs, icon arrows, phone format, program cards and course modal both directions.
- Currency output for EGP/SAR/AED/KWD/BHD; no localized display alters numeric value.
- Change language while payment modal open does not change amount/quote ID.
- Email and push templates in locale; accessibility names correct and no leaked translation keys.
- Quran content not modified on locale switch; approved translation panel only if selected.

Sources: https://cldr.unicode.org/ ; https://www.w3.org/TR/WCAG22/
