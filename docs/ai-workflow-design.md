# Designing Reliable AI Workflows

A useful workflow should reduce ambiguity rather than simply make a prompt longer.

## The six-layer model

### 1. Context

What does the assistant need to know?

### 2. Objective

What concrete result is required?

### 3. Constraints

What must not change? What limitations apply?

### 4. Procedure

What sequence should be followed?

### 5. Output contract

What should the final result contain?

### 6. Validation

How can a person verify the result?

## Bad pattern

```text
Fix this.
```

## Better pattern

```text
Goal:
Identify the root cause of the failing test.

Context:
- Python 3.x
- Unit test: ...
- Error: ...

Constraints:
- Do not change public API
- Prefer a minimal fix

Procedure:
1. Inspect the failing test.
2. Trace the relevant function.
3. Identify the first incorrect assumption.
4. Propose the smallest fix.
5. Add or update a regression test.
6. Run the relevant tests.

Output:
- Root cause
- Evidence
- Proposed change
- Test plan
- Remaining uncertainty
```

## The important distinction

A workflow is not a guarantee of correctness.

It is a repeatable process for improving the probability that the work is understandable, reviewable, and verifiable.
