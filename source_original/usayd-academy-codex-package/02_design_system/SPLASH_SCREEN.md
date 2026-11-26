# Mobile splash — `UX-MOBILE-000` (design addition D-16)

Added at the owner's request on 2026-11-21. It is **not in blueprint v1.2's inventory** and is logged as decision D-16. Full spec: `03_screens/screens/UX-MOBILE-000.md`.

## Two layers
1. **Native launch screen** (shown instantly by the OS):
   - Android 12+: SplashScreen API with background `#0F2529` and icon `assets/mark-reverse.svg`, exported to a 288 dp adaptive icon with the mark inside the 192 dp safe circle.
   - iOS: a LaunchScreen storyboard with the same background and the centred mark. No text, because it cannot be localised reliably.
   - Use `flutter_native_splash` to generate both.
2. **Flutter animated splash** continues from the same mark position:
   - 0–1.0 s: the canopy arc draws in.
   - 0.3 s: the mushaf rises.
   - 0.8 / 0.95 / 1.1 s: the three lamps light in sequence.
   - 1.0–1.3 s: the wordmark, the line «لتحفيظ القرآن الكريم», the divider and the tagline rise in.
   - Then a three-lamp loader and the version number.

## Rules
- The splash shows only while bootstrapping: secure-storage token read and refresh, locale and theme, remote config. It stays at least 0.8 s and at most 2.5 s. Never add an artificial delay.
- Routing:
  - Learner session → `UX-MOBILE-002`.
  - Teacher session → `UX-MOBILE-009`.
  - No session or expired session → `UX-MOBILE-001`.
  - Offline with a cached session → home in offline mode.
- Reduced motion: show the final frame statically.
- The text follows the device language (AR or EN). The splash is always Night.
- No ads, claims or statistics on the splash.
- **Unresolved:**
  - The minimum supported app version (force update) is not defined.
  - The token refresh endpoint is missing from OpenAPI v1.2.
