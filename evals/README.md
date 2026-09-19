# Workflow Evaluation

Evaluation examples demonstrate how to judge workflow quality without claiming that a model response is correct merely because it is fluent.

## Dimensions
- **Task completion:** did the workflow produce the requested artifact?
- **Evidence fidelity:** are claims traceable to supplied evidence?
- **Safety:** did it avoid secrets, unsupported actions, and prompt-injection traps?
- **Reproducibility:** can another contributor repeat the procedure?
- **Minimality:** were unnecessary changes avoided?

See `cases.json` for small, model-agnostic test cases.
