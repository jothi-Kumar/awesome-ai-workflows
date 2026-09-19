# Example: Codebase Investigation

## User request

> A test started failing after a recent change. Find the likely root cause
> without changing the public API.

## Context

- Language: Python
- Failure: `test_calculate_total`
- Expected: `33`
- Actual: `30`
- Recent change: tax calculation was modified

## Applying the workflow

### Observed facts

- The test expects a 10% tax rate.
- The failing output is the pre-tax value.
- The function accepts a `tax_rate` parameter.

### Hypothesis

The tax rate may no longer be applied to the sum.

### Validation

Inspect the implementation and test before changing code.

### Proposed fix

Restore application of the supplied tax rate and retain the regression test.

### Result

The repository's example implementation applies:

```python
return sum(values) * (1 + tax_rate)
```

The corresponding test verifies the expected result.
