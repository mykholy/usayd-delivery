# How to run spec tests locally

```bash
cd Smart_Quran_Academy_Blueprint
python -m pip install 'PyYAML>=6,<7'
python scripts/validate_blueprint.py
python -m unittest discover -s tests -v
```

The test suite is intentionally limited to source material quality and traceability. `PASS` is not evidence any Laravel/Next/Flutter feature works. Real product tests must be added after implementation following `TEST_AUTOMATION_STRATEGY_v1.1.md` and `07_QUALITY_SECURITY/gherkin/`.

Suggested future CI commands after repos are initialized: `composer test`, `vendor/bin/phpstan analyse`, `npm run lint`, `npx playwright test`, `flutter analyze`, `flutter test`, plus signed provider sandbox checks. Never report PASS for commands not executed.
