# Starter TDD patterns for application engineers — illustrative only

```php
// backend/tests/Feature/BookingRaceTest.php (Pest template; adapt real app model/factory)
it('does not reserve last credit twice', function () {
    // Arrange: authenticated learner + one remaining credit + two competing reservations.
    // Act: simulate two separate transactions competing for same credit and teacher slot.
    // Assert: one success, one SLOT_CONFLICT or CREDIT_INSUFFICIENT;
    //         sum(credit ledger) >= 0; exactly one active reservation.
})->skip('Requires real Laravel app, transactional DB and factories');
```

```ts
// web/e2e/guardian-consent.spec.ts (Playwright template)
import { test } from '@playwright/test';
test.skip('minor cannot join without consent', async ({ page }) => {
  // create minor fixture via sandbox/test helpers; do not use real minors
  // assert disabled join control and *server* returns 403 CONSENT_REQUIRED
});
```

```dart
// mobile/test/learning_plan_test.dart (Flutter test template)
// testWidgets('draft AI plan is labeled pending approval', (tester) async {
//    // pump fake API response and verify pending status in Arabic/English
// });
```

These templates are intentionally skipped/illustrative, **not passing tests**. Codex must replace them with real tests before any release gate.
