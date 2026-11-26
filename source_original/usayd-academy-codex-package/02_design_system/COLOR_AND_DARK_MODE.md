# Colour & dark mode — v0.4

Source of truth: `tokens.color.v0.4.json` and the first two blocks of `usayd-ui.css`. These values replace the colour values in `tokens.json` (v0.1).

## What changed
- **Light (Parchment):** crisper raised surfaces (`#FFFDF8`), darker secondary text (`#57524A`), stronger borders and more saturated status colours. Every text pair meets WCAG AA.
- **Dark (Night):** rebuilt around a deeper night (`#0A1B1E` page). There are now three clear elevation steps: sunken `#07151A`, page, raised `#11282C` and subtle `#173237`. The sidebar and hero use `#06141A`.
- In dark, primary actions are lamp gold and their hover is lighter (`#F2C463`). Accent text is `#F0C25F`. Charts use lamp gold.
- Inputs sit on the sunken surface, secondary buttons are outlined, and glass bars are tinted night.
- `color-scheme` is set per theme, so native controls and scrollbars match.

## Theme behaviour (implement in web and Flutter)
- Setting: **Auto (follow device) · Light · Dark**. The default is Auto. Store the choice on the device and in account preferences (`PATCH /api/v1/me/preferences`).
- Quick toggle (sun/moon icon) in the app top bar, public header, auth pages and the mobile app bar. Appearance cards are on `UX-LEARNER-032` and `UX-MOBILE-011`.
- Theme is independent of language, country and timezone.
- The splash screen and night surfaces (sidebar, hero, banners) stay Night in both themes.

## Contrast check (WCAG 2.1)
| Theme | Foreground | Background | Ratio | Result |
|---|---|---|---|---|
| light | `--tx` | `--bg-page` | 16.58 | OK |
| light | `--tx` | `--bg-raised` | 17.44 | OK |
| light | `--tx2` | `--bg-page` | 7.24 | OK |
| light | `--tx2` | `--bg-subtle` | 6.59 | OK |
| light | `--tx3` | `--bg-page` | 5.92 | OK |
| light | `--tx3` | `--bg-raised` | 6.23 | OK |
| light | `--tx-accent` | `--bg-page` | 5.72 | OK |
| light | `--tx-accent` | `--bg-raised` | 6.01 | OK |
| light | `--on-act` | `--act` | 14.16 | OK |
| light | `--on-act` | `--act-h` | 9.83 | OK |
| light | `--tx-on-brand` | `--bg-brand` | 13.45 | OK |
| light | `--tx-on-brand2` | `--bg-brand` | 7.91 | OK |
| light | `--line-strong` | `--bg-raised` | 3.79 | OK |
| light | `--focus` | `--bg-page` | 5.27 | OK |
| light | `--ok` | `--ok-bg` | 5.87 | OK |
| light | `--err` | `--err-bg` | 5.49 | OK |
| light | `--warn` | `--warn-bg` | 5.36 | OK |
| light | `--info` | `--info-bg` | 6.42 | OK |
| light | `--clay` | `--clay-bg` | 5.53 | OK |
| light | `--ai` | `--ai-bg` | 6.41 | OK |
| light | `--lock` | `--lock-bg` | 6.02 | OK |
| light | `--tx-brand` | `--bg-brand-soft` | 13.25 | OK |
| light | `--tx-accent` | `--bg-accent-soft` | 5.36 | OK |
| light | `--tx` | `--bg-page` | 16.58 | OK |
| light | `--tx` | `--bg-raised` | 17.44 | OK |
| light | `--tx` | `--bg-subtle` | 15.09 | OK |
| light | `--tx` | `--bg-sunken` | 13.77 | OK |
| light | `--tx2` | `--bg-page` | 7.24 | OK |
| light | `--tx2` | `--bg-raised` | 7.62 | OK |
| light | `--tx2` | `--bg-subtle` | 6.59 | OK |
| light | `--tx2` | `--bg-sunken` | 6.02 | OK |
| light | `--tx3` | `--bg-page` | 5.92 | OK |
| light | `--tx3` | `--bg-raised` | 6.23 | OK |
| light | `--tx3` | `--bg-subtle` | 5.39 | OK |
| light | `--tx3` | `--bg-sunken` | 4.92 | OK |
| light | `--tx-accent` | `--bg-page` | 5.72 | OK |
| light | `--tx-accent` | `--bg-raised` | 6.01 | OK |
| light | `--tx-accent` | `--bg-subtle` | 5.2 | OK |
| light | `--tx-accent` | `--bg-sunken` | 4.75 | OK |
| light | `--err` | `--bg-page` | 6.27 | OK |
| light | `--err` | `--bg-raised` | 6.6 | OK |
| light | `--err` | `--bg-subtle` | 5.71 | OK |
| light | `--err` | `--bg-sunken` | 5.21 | OK |
| light | `--ok` | `--bg-page` | 6.51 | OK |
| light | `--ok` | `--bg-raised` | 6.85 | OK |
| light | `--ok` | `--bg-subtle` | 5.93 | OK |
| light | `--ok` | `--bg-sunken` | 5.41 | OK |
| light | `--info` | `--bg-page` | 7.15 | OK |
| light | `--info` | `--bg-raised` | 7.52 | OK |
| light | `--info` | `--bg-subtle` | 6.51 | OK |
| light | `--info` | `--bg-sunken` | 5.94 | OK |
| light | `--warn` | `--bg-page` | 5.72 | OK |
| light | `--warn` | `--bg-raised` | 6.01 | OK |
| light | `--warn` | `--bg-subtle` | 5.2 | OK |
| light | `--warn` | `--bg-sunken` | 4.75 | OK |
| light | `--ai` | `--bg-page` | 7.2 | OK |
| light | `--ai` | `--bg-raised` | 7.58 | OK |
| light | `--ai` | `--bg-subtle` | 6.56 | OK |
| light | `--ai` | `--bg-sunken` | 5.99 | OK |
| light | `--clay` | `--bg-page` | 6.33 | OK |
| light | `--clay` | `--bg-raised` | 6.66 | OK |
| light | `--clay` | `--bg-subtle` | 5.77 | OK |
| light | `--clay` | `--bg-sunken` | 5.26 | OK |
| light | `--lock` | `--bg-page` | 7.24 | OK |
| light | `--lock` | `--bg-raised` | 7.62 | OK |
| light | `--lock` | `--bg-subtle` | 6.59 | OK |
| light | `--lock` | `--bg-sunken` | 6.02 | OK |
| dark | `--tx` | `--bg-page` | 15.17 | OK |
| dark | `--tx` | `--bg-raised` | 13.22 | OK |
| dark | `--tx2` | `--bg-page` | 8.96 | OK |
| dark | `--tx2` | `--bg-subtle` | 6.88 | OK |
| dark | `--tx3` | `--bg-page` | 6.55 | OK |
| dark | `--tx3` | `--bg-raised` | 5.71 | OK |
| dark | `--tx-accent` | `--bg-page` | 10.59 | OK |
| dark | `--tx-accent` | `--bg-raised` | 9.23 | OK |
| dark | `--on-act` | `--act` | 9.57 | OK |
| dark | `--on-act` | `--act-h` | 11.45 | OK |
| dark | `--tx-on-brand` | `--bg-brand` | 16.06 | OK |
| dark | `--tx-on-brand2` | `--bg-brand` | 9.48 | OK |
| dark | `--line-strong` | `--bg-raised` | 3.42 | OK |
| dark | `--focus` | `--bg-page` | 10.59 | OK |
| dark | `--ok` | `--ok-bg` | 7.22 | OK |
| dark | `--err` | `--err-bg` | 7.1 | OK |
| dark | `--warn` | `--warn-bg` | 8.93 | OK |
| dark | `--info` | `--info-bg` | 7.3 | OK |
| dark | `--clay` | `--clay-bg` | 7.55 | OK |
| dark | `--ai` | `--ai-bg` | 7.83 | OK |
| dark | `--lock` | `--lock-bg` | 6.88 | OK |
| dark | `--tx-brand` | `--bg-brand-soft` | 11.36 | OK |
| dark | `--tx-accent` | `--bg-accent-soft` | 9.24 | OK |
| dark | `--tx` | `--bg-page` | 15.17 | OK |
| dark | `--tx` | `--bg-raised` | 13.22 | OK |
| dark | `--tx` | `--bg-subtle` | 11.65 | OK |
| dark | `--tx` | `--bg-sunken` | 15.93 | OK |
| dark | `--tx2` | `--bg-page` | 8.96 | OK |
| dark | `--tx2` | `--bg-raised` | 7.81 | OK |
| dark | `--tx2` | `--bg-subtle` | 6.88 | OK |
| dark | `--tx2` | `--bg-sunken` | 9.41 | OK |
| dark | `--tx3` | `--bg-page` | 6.55 | OK |
| dark | `--tx3` | `--bg-raised` | 5.71 | OK |
| dark | `--tx3` | `--bg-subtle` | 5.03 | OK |
| dark | `--tx3` | `--bg-sunken` | 6.89 | OK |
| dark | `--tx-accent` | `--bg-page` | 10.59 | OK |
| dark | `--tx-accent` | `--bg-raised` | 9.23 | OK |
| dark | `--tx-accent` | `--bg-subtle` | 8.13 | OK |
| dark | `--tx-accent` | `--bg-sunken` | 11.13 | OK |
| dark | `--err` | `--bg-page` | 8.31 | OK |
| dark | `--err` | `--bg-raised` | 7.25 | OK |
| dark | `--err` | `--bg-subtle` | 6.38 | OK |
| dark | `--err` | `--bg-sunken` | 8.73 | OK |
| dark | `--ok` | `--bg-page` | 9.21 | OK |
| dark | `--ok` | `--bg-raised` | 8.02 | OK |
| dark | `--ok` | `--bg-subtle` | 7.07 | OK |
| dark | `--ok` | `--bg-sunken` | 9.67 | OK |
| dark | `--info` | `--bg-page` | 9.33 | OK |
| dark | `--info` | `--bg-raised` | 8.13 | OK |
| dark | `--info` | `--bg-subtle` | 7.17 | OK |
| dark | `--info` | `--bg-sunken` | 9.81 | OK |
| dark | `--warn` | `--bg-page` | 10.55 | OK |
| dark | `--warn` | `--bg-raised` | 9.19 | OK |
| dark | `--warn` | `--bg-subtle` | 8.1 | OK |
| dark | `--warn` | `--bg-sunken` | 11.08 | OK |
| dark | `--ai` | `--bg-page` | 10.46 | OK |
| dark | `--ai` | `--bg-raised` | 9.11 | OK |
| dark | `--ai` | `--bg-subtle` | 8.03 | OK |
| dark | `--ai` | `--bg-sunken` | 10.99 | OK |
| dark | `--clay` | `--bg-page` | 8.96 | OK |
| dark | `--clay` | `--bg-raised` | 7.81 | OK |
| dark | `--clay` | `--bg-subtle` | 6.88 | OK |
| dark | `--clay` | `--bg-sunken` | 9.41 | OK |
| dark | `--lock` | `--bg-page` | 8.96 | OK |
| dark | `--lock` | `--bg-raised` | 7.81 | OK |
| dark | `--lock` | `--bg-subtle` | 6.88 | OK |
| dark | `--lock` | `--bg-sunken` | 9.41 | OK |

Body text needs 4.5:1, and borders and focus rings need 3:1. Lamp gold `#E8B04B` is never used as text on Parchment.
