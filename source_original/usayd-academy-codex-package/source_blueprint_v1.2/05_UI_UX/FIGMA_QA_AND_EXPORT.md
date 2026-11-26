# Figma deliverables and QA signoff

## File structure
00 Brand & semantic variables; 01 Components variants; 02 Public; 03 Learner; 04 Teacher; 05 Admin/Academic; 06 AI & Contests; 07 Flutter Mobile; 08 Prototype flows; 09 Dev handoff; 10 QA evidence.

## Component quality
Buttons, field controls, OTP, phone input, dropdown, date/time timezone selector, data table/card, status, permissions, Quran viewer text container, audio/video stage, study plan, revision stacks, competition progress, judge rubric, appeals, payroll calculator, notifications. Tokens must be actual Figma variables/styles: semantic surfaces, type, spacing, radius, light/dark, RTL/LTR icon mirroring. Variants include loading/disabled/focus/error/permission/no-consent/offline.

## Screen QA
- Each of 119 UX IDs mapped to frame and owner. Critical P0 (at least 25 frames) first, then remaining without empty placeholders.
- Interactive connections represent real state changes; mocked data explicitly fictional and stable across screens.
- Manual RTL review on Arabic labels; Quran script not mirrored; choose readable Quran font with licensed verified sample, not generative invented verses.
- Responsive constraints, 360px minimum, 200% zoom, touch targets, color contrast and focus states verified.
- Marketing pages accessible and honest, no fake reviews/certifications. Student screens clear and encouraging rather than punitive.
- Mobile Flutter handoff includes platform-specific camera/mic permissions, back navigation, media pause/resume, backgrounding/reconnect and push states.

## Handoff metadata per frame
`UX ID | Jira ID | FR IDs | Figma URL/frame ID | breakpoints | variants | API operationIds | analytics events | localizations | empty/error content | A11y notes | interactions | reviewed by | status`.

## Deliverability proof
Actual Figma link, project permission, component library docs, local variables exports, design screenshots, prototype test on compact screen and desktop, screen traceability, commented change log. If Figma access lacking, file is not created and cannot be marked 'Completed'.
