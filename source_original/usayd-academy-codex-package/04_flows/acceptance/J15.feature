# language: en
# Specification only — no backend exists; run once the Laravel API implements the approved contracts.
@J15 @FR-PAYROLL-001 @FR-PAYROLL-002 @FR-PAYROLL-007 @FR-PAYROLL-008
Feature: Payroll: accrual → calculation → review → dual approval → disbursement/reconciliation (no invented rules)

  Scenario: Dual control
    Given a pay run prepared by F1
    When F1 approves it
    Then the API answers 403 SELF_APPROVAL_FORBIDDEN
