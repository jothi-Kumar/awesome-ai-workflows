# Code Review

## Goal

Review a change for correctness, maintainability, security, and unintended behavior.

## Instructions

1. Understand the intended behavior.
2. Inspect the complete diff.
3. Check changed code in surrounding context.
4. Identify correctness issues first.
5. Check error handling and edge cases.
6. Check security-sensitive behavior.
7. Check performance only where relevant.
8. Check tests.
9. Avoid style comments unless they materially improve maintainability.
10. Report findings with file/line references when available.

## Finding format

```text
Severity: Critical | High | Medium | Low
Location:
Problem:
Evidence:
Suggested fix:
```

## Expected output

- Summary
- Findings ordered by severity
- Missing tests
- Questions/uncertainties
- Approval recommendation only if the human reviewer requests one

## Validation checklist

- [ ] Findings are actionable.
- [ ] No speculative claims are presented as facts.
- [ ] Security concerns are explicitly identified.
- [ ] Tests were inspected.
