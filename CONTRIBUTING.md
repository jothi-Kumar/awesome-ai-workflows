# Contributing

Thank you for contributing to Awesome AI Workflows.

The project values practical workflows that make AI-assisted work more reliable and reproducible.

## Before opening an issue

Search existing issues first.

For bugs, include:

- What you expected
- What happened
- Relevant workflow or file
- Reproduction steps
- AI/tool used, if relevant
- Output or error message
- What you already tried

For new workflows, explain:

- The problem it solves
- Who benefits
- Required context
- Expected output
- How the result can be validated

## Adding a workflow

Create the workflow in the most appropriate category:

```text
workflows/<category>/<workflow-name>.md
```

Use this structure:

```markdown
# Workflow Name

## Goal

## When to use

## Required context

## Instructions

## Expected output

## Validation checklist

## Common failure modes
```

Keep one workflow focused on one primary task.

## Adding an agent

Place reusable agent instructions in:

```text
agents/<agent-name>.md
```

An agent should define:

- Role
- Mission
- Inputs
- Operating rules
- Workflow
- Output format
- Validation requirements
- Boundaries

Avoid instructions that encourage fabrication, unsafe automation, or bypassing human review.

## Pull requests

1. Create a focused branch.
2. Make the smallest useful change.
3. Update documentation if behavior or structure changes.
4. Run relevant tests.
5. Check Markdown links and formatting.
6. Explain what changed and how it was validated.
7. Open a pull request using the repository template.

## Quality standard

A contribution should generally be:

- Specific rather than generic
- Reusable rather than tied to one private project
- Vendor-neutral where practical
- Easy to understand
- Testable or reviewable
- Free of secrets and private data

## Commit messages

Prefer concise imperative messages:

```text
Add debugging workflow
Improve research evidence workflow
Fix Python example
Document contribution process
```

## AI-generated contributions

AI-assisted contributions are welcome.

Contributors remain responsible for reviewing their submissions, validating generated code/content, checking licenses, and ensuring that no confidential information was exposed to an AI system.

## License

By contributing, you agree that your contribution may be distributed under the repository's MIT License.
