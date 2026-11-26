# Flutter mobile application technical/UX spec

## Scope

Flutter apps for iOS and Android share Laravel business APIs; the mobile app is not a webview of all admin screens. Learner flows: signup/OTP/consent, onboarding, schedule, classroom (provider-specific native adapter), Quran view, tasks, revision, exam, contest, library, AI assistant, billing, support, account. Teacher mobile: today/calendar, lesson prejoin, classroom, brief report and pay statements; full admin web-first.

## Architectural modules

`core/api`, `core/auth`, `core/localization`, `core/analytics`, `core/secure_storage`, `core/deep_link`, `core/video_provider`, `features/learning`, `features/booking`, `features/lessons`, `features/exams`, `features/competitions`, `features/teacher`, `features/settings`. Use typed API models generated from reviewed OpenAPI. No secret server keys in app binaries.

## Connectivity, interruption and state

- Network loss in lesson: show reconnect progress; app stays recoverable; attendance server reconciled.
- Phone call/background: handle audio focus, mic release, native provider lifecycle and session return.
- Exam: server authoritative attempt and timer; restore draft after crash; avoid offline final submission without server acknowledgement.
- Quran content: cache only source-licensed subsets; protect downloaded media and user notes.
- Push: opt-in/OS permissions, no religious guilt messages, quiet hours, deep link verifies auth/authorization after tap.
- Logout/revocation clears tokens, user cache, sensitive files and push registration.
- Screen reader: semantic labels, RTL focus order, >44px touch targets, dynamic text size, captioned tutorials.

## Quality matrix

Android budget phone 360×800 and mainstream 390/428; iPhone SE/standard; tablet; Arabic/English; Dark/Light; weak LTE/3G; permission denied; device camera missing; app suspended; timezone changed; auth revoked; invalid provider join; offline mid-submission. Native audio SDK support confirmed per vendor and platform via POC.

## Release gate

Security mobile review (deep links, token extraction, storage), app-store privacy disclosures and permission rationale, accessibility manual tests, vendor crash/connection load, store assets and verified support contact. Feature parity tracked by UX IDs, not assumed.
