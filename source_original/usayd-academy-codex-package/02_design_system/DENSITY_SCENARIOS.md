# Operational density scenarios (OPEN-01, D-40)

Applies to the 10 admin/supervisor screens flagged by the audit: UX-ADMIN-005, 007, 011, 015, 027, 031 and UX-SUP-008, 009, 010, 011.
The canvas shows the **normal** scenario with 6–8 sample rows. Every count, ID and time is labelled *Sample data*; names are runtime slots. No production data and no fabricated charts.

## Pattern
1. **Status summary strip** — 4 counts the list endpoint can return as facets (`status` counts). If the API does not return a facet, the tile is not shown (never computed from one page).
2. **Exception lane** (“Needs attention” / “Blocked until resolved”) — the rows that block a workflow (MFA off, DST gap, independence conflict, placeholder mismatch …), each with one action that leads to a real screen.
3. **Filter bar + search** — query parameters of the list operation.
4. **Table** — sortable headers (`aria-sort`, server-side `sort` + `order`), flagged rows tinted with a logical-side bar, row actions ≥ 44 px.
5. **Cursor pager** — “Showing N rows · 25 per page”, Previous/Next; **no total count** unless the API returns one; Previous disabled on the first page.
6. **No bulk actions** — none of these lists has a bulk API; add bulk selection only with an approved bulk operation.

## Scenarios (what the build must handle)
| Scenario | Rows | Behaviour |
|---|---|---|
| Sparse | 0–2 | 0 → empty state with the primary action; 1–2 → table without pager; summary strip still visible; exception lane hidden when empty |
| Normal | 3–25 | single page; pager shows “Showing N rows”, Next disabled when `next_cursor` is null |
| Peak | 26–10,000+ | cursor pages of 25 (50/100 selectable); sticky header; filters and sort kept in the URL; loading skeleton rows while fetching; never client-side sort of a partial page |
| Incident | any | exception lane pinned at the top with count + tone; flagged rows tinted; lane items link to the resolving screen; nothing auto-resolves |

## Screen-specific facets
| Screen | Summary facets | Exception rule (lane) |
|---|---|---|
| UX-ADMIN-005 Staff & permissions | active, without MFA, pending invites, active break-glass | staff without MFA (blocked from sensitive screens) |
| UX-ADMIN-007 Teachers | active, pending approval, suspended, quality review | suspended / quality review rows flagged |
| UX-ADMIN-011 Programs | published, drafts, awaiting academic approval, missing translation | drafts that cannot publish (copy or approval missing) |
| UX-ADMIN-015 Booking ops | payment pending, reschedule requests, conflicts, holds expired today | DST gap, shift clash |
| UX-ADMIN-027 Competitions | open, judging, appeal window, drafts & scheduled | upcoming deadlines that block publishing |
| UX-ADMIN-031 Appeals | open, unassigned, past SLA, independence conflicts | reviewer = original judge; past SLA |
| UX-SUP-008 Role assignments | active, awaiting second approval, expiring ≤7 days, revoked this month | — (flagged rows only) |
| UX-SUP-009 Access audit | events 7 days, pending review, break-glass, impersonation | reviews due within 24 h |
| UX-SUP-010 Settings registry | keys, drafts, awaiting second approval, market overrides | — |
| UX-SUP-011 Localization | published, in review, missing translation, validation errors | placeholder/plural mismatch; legal copy pending owner |

Below 760 px the tables become stacked records (D-19); header sort buttons are hidden there (R-019, accepted risk for desktop-first admin screens).
