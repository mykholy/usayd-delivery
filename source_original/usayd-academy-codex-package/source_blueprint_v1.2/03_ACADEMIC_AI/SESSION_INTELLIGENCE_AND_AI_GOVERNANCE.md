# Session Intelligence and AI safety/quality governance

## Business reasons

1. Help teachers produce structured learning follow-up without long typing.
2. Detect *possible* out-of-platform solicitation or safeguarding concerns when lawfully processed.
3. Improve operations with attendance and quality metrics (mostly non-audio).
4. Produce grounded, privacy-safe learning recommendations.

## Privacy-first processing modes

| Mode | Default | Data | Legal/UX | Gate |
|---|---|---|---|---|
| M0 No-audio | ON | Join/leave, report forms, approvals | Standard notice | P0 |
| M1 Structured summary | ON when teacher submits data | Teacher-entered fields only | Standard educational processing | P1 |
| M2 Post-session transcript | OFF | Optional approved excerpts/transcript | Separate purpose/guardian if needed, retention | P1 pilot |
| M3 Live policy detection | OFF | Raw live audio/STT stream | Strong purpose/necessity/capability review | P2 pilot |
| M4 Recitation correction | OFF | Specialist ASR waveform for opted-in practice | Separate rigorous validation & consent | Research |

Do not equate absence of stored audio with absence of audio processing. Provider DSP/IP and processors need documented lawful basis, data flow, technical route and deletion policies.

## Detection taxonomy

- `OFF_PLATFORM_SOLICITATION` (explicit personal arrangement request).
- `PERSONAL_CONTACT_REQUEST` (private number/chat handle asked).
- `ABUSIVE_SPEECH` (human safeguarding triage).
- `EXCESSIVE_UNRELATED_CONTENT` (coaching quality suggestion, not misconduct).
- `MISLEADING_CERTIFICATION` (teacher claiming unverified credential).
- `RECORDING_POLICY_BREACH` (derived from platform recording event vs consent).

Rules use contextual snippets, speaker differentiation and policy version; language support for Egyptian/Gulf Arabic must be benchmarked separately from Quran recitation. Policy output stores claim + evidence location + limits; `flagged` is not `violation`. For ambiguous examples or prompt injection from transcript, ignore instruction-like content and prefer review/no decision.

## Pipeline

`Provider Media` → `Consent/Feature Gate` → `Ephemeral Worker` → `STT/Diarization` → `Recitation vs ordinary speech router` → `Policy classifier` → `Restricted case queue` → `Human reviewer` → `Decision + notification + appeal`.

When provider lacks necessary media access (external Google Meet/Zoom Meeting), no unsupported inference is silently claimed. Platform can still use metadata, teacher reports and consented post-call provider artifacts where legally and technically available.

## Information security

Mutual TLS/service identity to worker; encrypted transport and storage, no logs of full transcripts, least-privilege scoped access, DPA and cross-border transfer approval, deletion verification, AI prompt versioning. High severity safety flags can trigger *human triage*, not silent audio archive.

## Model evaluation

Create consented synthetic/volunteer audio tests: clear solicitation, benign discussion about platform contact rules, normal Quran discussion, mixed dialect, overlapping speech, weak network, speaker misattribution, accent variance. Blind double-label. Report precision/recall by class and false-positive counts; study review labor and cost per audio-minute. A 95% overall accuracy headline can hide dangerous false positives; report each class threshold agreed by safety owner.

## AI source-of-truth

- Lesson grade and mastery: authorized teacher.
- Quran text: verified licensed source and exact edition.
- Plan proposal: AI can draft but teacher signs.
- Student encouragement: no fabricated achievements.
- Policy violation: human reviewer with documented reasoning and appeal.
- Money/prizes: finance/judge approvals only.

## Kill switches

Feature flag global/region/teacher/learner, disable audio analysis immediately upon consent withdrawal, model budget exhaustion or incident; classroom still functions, no unrelated academic denial.
