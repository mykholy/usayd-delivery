# Test templates for Codex — examples, not passing executable product tests

## PHP Pest examples — adapt after implementation
```php
it('preserves a KWD quote minor unit and amount on PSP request', function () {
    $quote = CheckoutQuote::factory()->forCountry('KW')->withAmountMinor(7500, 'KWD')->create();
    $payload = app(PaymentInitiator::class)->buildProviderPayload($quote);
    expect($payload['currency'])->toBe('KWD')->and($payload['amount_minor'])->toBe(7500);
});
it('denies a supervisor outside assigned region', function () {
    $staff = User::factory()->academicSupervisorForMarket('EG')->create();
    $learner = User::factory()->inMarket('SA')->create();
    actingAs($staff)->getJson("/api/v1/learners/{$learner->id}/learning-summary")->assertForbidden();
});
it('does not move active provider rooms after routing policy change', function () {
    // Arrange an active LiveKit lesson + approved future Daily policy,
    // assert existing binding remains LiveKit, and new lesson binds Daily.
});
```

## Playwright scenario sketch
```ts
// This is a scaffold; selectors/routes must match implemented app and active market fixtures.
test('locale switch preserves amount and timezone', async ({ page }) => {
  await page.goto('/ar/pricing?market=SA');
  const priceBefore = await page.getByTestId('charge-amount-minor').textContent();
  await page.getByRole('button', {name: 'English'}).click();
  await expect(page.locator('html')).toHaveAttribute('dir','ltr');
  await expect(page.getByTestId('charge-amount-minor')).toHaveText(priceBefore!);
});
```

## Flutter widget scenario sketch
```dart
// Arrange user selected country SA / locale en / timezone Africa/Cairo.
// Toggle locale ar, assert directionality RTL while selected SA and timezone Cairo persist.
// Validate KWD display at three decimal places in charge quote and no amount mutation.
```

## Provider contract suite
For every adapter: `getCapabilities(context)`, `healthCheck`, `createRoom`, `issueJoin`, `revokeOrInvalidate`, `webhookVerification`, `incidentRecovery`, `clientPlatformParity` with `verified/unsupported/unknown` expected results and prohibitions. Google Meet must never pass raw_audio_live_ai acceptance via deprecated Media API.
