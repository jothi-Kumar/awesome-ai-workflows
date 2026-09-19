"""Minimal local helper demonstrating workflow discovery.

This intentionally does not call an AI API. It shows how a deterministic
application can load a workflow from this repository before handing the
instructions and task context to an AI system of the user's choice.
"""

from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]


def load_workflow(relative_path: str) -> str:
    path = ROOT / relative_path
    if not path.is_file():
        raise FileNotFoundError(path)
    return path.read_text(encoding="utf-8")


if __name__ == "__main__":
    workflow = load_workflow(
        "workflows/software-development/debugging.md"
    )
    print(workflow)
