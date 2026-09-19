#!/usr/bin/env python3
"""Validate AI workflow markdown files for reusable structure and safety guardrails."""
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
WORKFLOWS = ROOT / "workflows"

def has_any(text, headings):
    return any(h in text for h in headings)

def main():
    files = sorted(WORKFLOWS.rglob("*.md"))
    errors = []
    for path in files:
        text = path.read_text(encoding="utf-8")
        checks = [
            ("goal", ["## Goal"]),
            ("process", ["## Workflow", "## Instructions"]),
            ("output", ["## Output", "## Expected output"]),
            ("validation", ["## Guardrails", "## Validation checklist"]),
        ]
        for label, headings in checks:
            if not has_any(text, headings):
                errors.append(f"{path}: missing {label} section")
        safety_markers = [
            "Never fabricate", "do not invent", "No speculative claims",
            "speculative claims are presented as facts", "untrusted input"
        ]
        if not any(marker.lower() in text.lower() for marker in safety_markers):
            errors.append(f"{path}: missing anti-fabrication/untrusted-input guardrail")
        if len(text.strip()) < 220:
            errors.append(f"{path}: suspiciously short")
    print(f"Validated {len(files)} workflow(s)")
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print("All workflow checks passed")
    return 0

if __name__ == "__main__":
    sys.exit(main())
