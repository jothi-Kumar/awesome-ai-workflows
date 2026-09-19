# Awesome AI Workflows 🤖

> A practical, open-source collection of reusable AI workflows, prompts, agent instructions, templates, and engineering patterns for real-world work.

## Why this project?

AI assistants are becoming powerful enough to help with software development, research, documentation, analysis, project management, and many other types of work.

However, getting consistently useful results is often less about writing a single "perfect prompt" and more about having a well-structured workflow.

This repository collects practical, reusable workflows that can be adapted to different AI assistants and development environments.

The goal is simple:

**Turn common real-world tasks into repeatable AI-assisted workflows.**

---

## What you'll find here

### 🧑‍💻 Software Development

Reusable workflows for:

* Understanding an unfamiliar codebase
* Debugging difficult issues
* Refactoring legacy code
* Writing unit tests
* Performing code reviews
* Generating technical documentation
* Designing APIs
* Reviewing pull requests
* Investigating production issues
* Planning implementation work

### 🔬 Research

Workflows for:

* Breaking down complex research questions
* Finding and evaluating sources
* Comparing competing explanations
* Extracting evidence
* Identifying uncertainty
* Creating literature-review structures
* Producing research summaries

### 📊 Data Analysis

Workflows for:

* Exploring datasets
* Data-quality checks
* Statistical analysis planning
* Generating visualizations
* Finding anomalies
* Explaining analytical results
* Reviewing analytical assumptions

### 📝 Documentation

Templates and workflows for:

* README files
* Architecture documentation
* Technical specifications
* API documentation
* Release notes
* Incident reports
* Project proposals

### 🤖 AI Agents

Reusable instructions for specialized AI roles such as:

* Code Reviewer
* Debugging Assistant
* Research Assistant
* Documentation Agent
* Test Engineer
* Architecture Reviewer
* Project Planner

---

## Quick Start

You don't need a specific AI platform to use this repository.

Choose a workflow, copy the instructions, provide your project context, and adapt the output to your environment.

For example:

```text
1. Select a workflow
2. Provide the required context
3. Ask the AI to identify assumptions
4. Ask it to produce a proposed solution
5. Review the result
6. Run tests or validate the output
7. Iterate
```

---

## Example: Codebase Investigation

A useful AI coding workflow should not immediately ask an AI assistant to modify code.

Instead:

```text
Understand → Map → Identify → Hypothesize → Validate → Change → Test
```

### Step 1 — Understand

Ask the assistant to identify:

* Project structure
* Main components
* Entry points
* Dependencies
* Configuration
* Important data flows

### Step 2 — Map

Create a concise architecture map showing how the important components interact.

### Step 3 — Identify

Define:

* The observed problem
* Relevant files
* Relevant functions
* Existing behavior
* Constraints

### Step 4 — Hypothesize

Generate possible causes and explain the evidence supporting each hypothesis.

### Step 5 — Validate

Inspect the relevant implementation and tests before changing anything.

### Step 6 — Change

Make the smallest appropriate change.

### Step 7 — Test

Run relevant tests and verify that existing behavior has not been unintentionally changed.

---

## Design Principles

This project follows several principles.

### 1. Context before generation

AI systems generally perform better when they receive relevant context rather than being asked to immediately generate an answer.

### 2. Evidence before assumptions

When investigating a problem, distinguish between:

* Facts
* Observations
* Assumptions
* Hypotheses
* Conclusions

### 3. Small changes are easier to validate

Prefer focused changes over unnecessary rewrites.

### 4. Verification is part of the workflow

Generated code, analysis, documentation and recommendations should be reviewed and validated.

### 5. Reusable beats clever

A workflow should be understandable and adaptable by someone encountering it for the first time.

### 6. Human judgment remains important

AI should assist with reasoning and execution, not replace appropriate human review or domain expertise.

---

## Repository Goals

This project aims to become a practical reference for people who want to use AI effectively without turning every task into trial-and-error prompting.

We welcome contributions that:

* Solve common real-world problems
* Improve existing workflows
* Add useful templates
* Document practical techniques
* Include reproducible examples
* Improve clarity and accessibility

---

## Contributing

Before contributing, please read [CONTRIBUTING.md](CONTRIBUTING.md).

Good contributions are:

* Practical
* Reusable
* Clearly documented
* Easy to understand
* Tested where applicable
* Honest about limitations

---

## License

This project is released under the MIT License.

See [LICENSE](LICENSE) for details.
