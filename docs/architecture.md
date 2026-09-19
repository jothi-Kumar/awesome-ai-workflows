# Repository Architecture

## Design goals

The repository is organized around discovery and reuse.

### Workflows

A workflow solves a specific task.

```text
workflows/
```

### Agents

An agent is a reusable role/instruction set that can apply across multiple tasks.

```text
agents/
```

### Templates

Templates provide structured input/output formats.

```text
templates/
```

### Examples

Examples demonstrate how the concepts can be used in practice.

```text
examples/
```

## Recommended AI retrieval strategy

When an AI assistant works with this repository:

1. Read `README.md`.
2. Identify the relevant category.
3. Retrieve the smallest set of relevant workflow/agent/template files.
4. Apply the instructions to the user's actual context.
5. Validate the output against the workflow checklist.
6. Report uncertainty and missing information.

Avoid loading the entire repository when a focused subset is sufficient.
