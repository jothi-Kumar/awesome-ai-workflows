# Awesome AI Workflows 🤖

> Practical, reusable AI workflows, agent instructions, prompts, templates, and engineering patterns for real-world work.

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Contributions Welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg)](CONTRIBUTING.md)

## Why this project?

AI assistants are useful across software development, research, documentation, analysis, project management, and many other tasks. The challenge is getting **repeatable, verifiable results** instead of relying on one-off prompts.

**Awesome AI Workflows** turns common tasks into structured workflows.

The repository is designed to be:

- **Reusable** — workflows can be copied and adapted.
- **AI-readable** — files have predictable names and focused responsibilities.
- **Evidence-aware** — facts, assumptions, hypotheses, and conclusions are separated.
- **Verification-first** — generated work should be checked before it is trusted.
- **Platform-neutral** — compatible with ChatGPT, Codex, GitHub Copilot, Claude, Gemini, local models, and other assistants.
- **Human-in-the-loop** — AI assists; people review consequential decisions.

## What is included?

### Workflows

| Area | Examples |
|---|---|
| Software engineering | Codebase investigation, debugging, refactoring, testing, code review |
| Research | Research planning, source evaluation, evidence synthesis |
| Data | Dataset profiling, anomaly investigation, analysis review |
| Documentation | README generation, architecture docs, release notes |
| Project work | Requirements, technical design, implementation planning |
| Productivity | Meeting-to-actions, decision records, task decomposition |

### Agents

Reusable instruction files for:

- Code Reviewer
- Debugging Investigator
- Documentation Agent
- Research Agent
- Project Planner
- Test Engineer

### Templates

- Technical design
- Research brief
- Decision record
- Bug report
- Feature request
- Pull request
- AI task specification

## Quick start

Choose a workflow from `workflows/`, copy it into your AI tool, and provide the requested context.

A reliable default loop is:

```text
Context
  ↓
Understand
  ↓
Inspect evidence
  ↓
Form hypotheses
  ↓
Validate
  ↓
Propose
  ↓
Implement
  ↓
Test
  ↓
Review
```

Do not skip validation simply because an AI system produced a confident answer.

## Repository map

```text
awesome-ai-workflows/
├── README.md
├── LICENSE
├── CONTRIBUTING.md
├── CODE_OF_CONDUCT.md
├── SECURITY.md
├── CHANGELOG.md
├── workflows/
│   ├── software-development/
│   ├── research/
│   ├── data-analysis/
│   ├── documentation/
│   ├── project-management/
│   └── productivity/
├── agents/
├── templates/
├── examples/
│   ├── python/
│   └── markdown/
├── docs/
└── .github/
    ├── ISSUE_TEMPLATE/
    └── pull_request_template.md
```

## Workflow format

Every workflow follows the same structure:

1. **Goal**
2. **When to use**
3. **Required context**
4. **Instructions**
5. **Expected output**
6. **Validation checklist**
7. **Common failure modes**

This makes workflows easier for both humans and AI systems to discover and apply.

## AI usage principles

### Context before generation

Give the assistant the relevant files, constraints, existing behavior, and expected outcome before requesting changes.

### Evidence before assumptions

Separate:

- Facts
- Observations
- Assumptions
- Hypotheses
- Conclusions

### Minimal change

Prefer the smallest change that solves the stated problem while preserving existing behavior.

### Verification is mandatory

For code, run tests and static checks where available. For research, verify important claims against sources. For documentation, compare generated content against the actual system.

### State uncertainty

If information is missing, the assistant should say what is missing instead of silently inventing it.

### Human review

AI-generated output should receive appropriate human review, especially for security, legal, financial, medical, production, or other consequential decisions.

## Using this repository with ChatGPT and other coding assistants

The repository is intentionally structured as ordinary Markdown, source code, and configuration files so supported AI tools can inspect it easily.

For ChatGPT, GitHub-connected experiences can retrieve permitted repository content on demand, including code, README files, and documentation. Availability varies by plan and product surface. See the official OpenAI documentation for current connection details.

The repository does **not** require a specific AI provider.

## First working examples

### Python

See:

- `examples/python/ai_workflow_runner.py`
- `examples/python/sample_project.py`
- `examples/python/test_sample_project.py`

Run:

```bash
python examples/python/ai_workflow_runner.py
python -m unittest examples/python/test_sample_project.py
```

### Markdown

See:

- `examples/markdown/codebase-investigation-example.md`
- `templates/technical-design.md`

## Contributing

Contributions are welcome.

Before contributing, read [CONTRIBUTING.md](CONTRIBUTING.md).

Good contributions are:

- Practical
- Reusable
- Clearly documented
- Honest about limitations
- Easy to validate
- Independent of a single vendor where possible

## Security

See [SECURITY.md](SECURITY.md).

Never commit API keys, credentials, private customer data, production secrets, or sensitive information.

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE).

## Maintainer note

This project is intended as a community resource. It does not promise that AI output is correct, complete, safe, or suitable for every situation.


## Repository scale
The repository is intentionally growing as a reusable engineering library:
- **40 workflows** across software development, research, data analysis, documentation, project management, productivity, security, and coding-agent work.
- **11 specialized agents** for common engineering and research roles.
- Automated structural validation via `python tools/validate_workflows.py`.
- Evaluation cases under `evals/`.
- Defensive security workflows under `workflows/security/`.
- Coding-agent guidance under `docs/codex.md`.
- Python examples and tests under `examples/python/`.

Counts are maintained manually and should be updated when the catalog changes.
