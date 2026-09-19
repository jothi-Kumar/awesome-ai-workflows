"""Small deterministic example used by the repository documentation."""


def normalize_name(name: str) -> str:
    """Return a normalized display name.

    Empty or whitespace-only names are rejected because callers need
    an explicit identifier.
    """
    value = " ".join(name.split())
    if not value:
        raise ValueError("name must not be empty")
    return value.title()


def calculate_total(values: list[float], tax_rate: float = 0.0) -> float:
    """Calculate a total after applying a non-negative tax rate."""
    if tax_rate < 0:
        raise ValueError("tax_rate must not be negative")
    return sum(values) * (1 + tax_rate)
