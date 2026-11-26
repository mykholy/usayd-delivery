# Verified API PR state — 2026-11-26

Scope: API PRs #18–30 checked by GitHub. No independent human approval claimed. Mobile PRs not re-reviewed by this workflow.

| PR | State | Merge commit / head |
|---|---|---|
| [#18](https://github.com/mykholy/usayd-api/pull/18) USYD-T0032: enforce signed storage path ownership | Merged | `a405d88ab368375fa5f19abab2c82bfd86e6866a` |
| [#19](https://github.com/mykholy/usayd-api/pull/19) USYD-T0028: atomic identity and independent token families | Merged | `09f47074391866cc6cbc0a6653af86ede574ac8a` |
| [#20](https://github.com/mykholy/usayd-api/pull/20) USYD-T0030: thin feature flag controller and fail-safe targeting | Merged | `d19760803a20c0eb53796c741e2ce22072651e95` |
| [#21](https://github.com/mykholy/usayd-api/pull/21) USYD-T0026: secure queue metrics and truthful readiness | Merged | `97004f69715bb69236b0edb68ec046a9b2411966` |
| [#22](https://github.com/mykholy/usayd-api/pull/22) USYD-T0023: thin health controller and isolated readiness probes | Merged | `d53c2998151007cfc1752716306375b6ad53152c` |
| [#23](https://github.com/mykholy/usayd-api/pull/23) USYD-T0031: outbox relay consistency and atomic acknowledgment | Merged | `6650a31e23c75e39dd53442c3f2f8d780bfb460d` |
| [#24](https://github.com/mykholy/usayd-api/pull/24) USYD-T0025: atomic database idempotency and replay-safe responses | Merged | `9fe063506b51c5377a07f2fa94f2c8c50cb9bd8c` |
| [#25](https://github.com/mykholy/usayd-api/pull/25) USYD-T0022: enforce domain and application dependency boundaries | Merged | `421634aceaaed846a7628bee5530fb4c42a0fcd9` |
| [#26](https://github.com/mykholy/usayd-api/pull/26) USYD-T0032: harden private storage download content and caching | Merged | `cc36798780f57777b2319b152719e030e77172dd` |
| [#27](https://github.com/mykholy/usayd-api/pull/27) USYD-T0033: fail-closed API CI and real Redis integration | Merged | `4c36578dd25f2925623b81403d3f2f03f70d9d18` |
| [#28](https://github.com/mykholy/usayd-api/pull/28) USYD-T0032: fail-closed upload safety boundary and retention record | Merged | `4b2dac06d8f04460c558818f1bc25ffd31edfffa` |
| [#29](https://github.com/mykholy/usayd-api/pull/29) USYD-T0032: resolve private S3 adapter and verify storage integration | Merged | `8c88d7108eb212e764c3909c809a3b1a5d78cbd7` |
| [#30](https://github.com/mykholy/usayd-api/pull/30) USYD-T0034: staging release readiness and reversible migration protocol | Merged | `4dc2c69bcb4bcf8eebe2f849c9d77350cbe414f7` |

PR #30 exact-head API CI 45883983912 SUCCESS (178 tests, 1689 assertions, 10 readiness fixtures, 13 contract fixtures, 16 routes); automated review 45883983873 SUCCESS; both CodeRabbit threads resolved. No actual AWS deployment claimed.

PR #31: [USYD-T0036: secret scanning, locked dependency audit and SBOM](https://github.com/mykholy/usayd-api/pull/31) — open; head `46b817be1be6d5238b99ab8b64a1112a3025f884`; Supply chain security: success; Independent PR Code Quality Review: success; API CI: success. Security audit zero advisories; Gitleaks 82 commits, zero unignored findings; 3 exact reviewed fixture fingerprints; 117-component SBOM artifact 15148814537. Jira USYD-79 remains In Progress until verified merge and remaining activation checks.
