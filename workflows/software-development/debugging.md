# Debugging Investigation

## Goal

Find and validate the root cause of a software defect.

## Required context

- Error message
- Reproduction steps
- Expected behavior
- Actual behavior
- Relevant source
- Test output

## Instructions

1. Reproduce or inspect the failure.
2. Identify the first point where actual behavior diverges from expected behavior.
3. Trace inputs into that point.
4. Form one or more hypotheses.
5. Rank hypotheses by evidence, not intuition.
6. Inspect the implementation and tests.
7. Propose the smallest fix.
8. Add a regression test when practical.
9. Run relevant tests.
10. Report any remaining uncertainty.

## Expected output

```text
Observed failure:
Root cause:
Evidence:
Fix:
Regression test:
Validation:
Remaining uncertainty:
```

## Validation checklist

- [ ] Root cause is tied to concrete evidence.
- [ ] Proposed fix addresses the cause, not just the symptom.
- [ ] Regression coverage exists where practical.
- [ ] Relevant tests pass.
