from typing import Optional


def validate_non_empty_text(value: str, field_name: str) -> Optional[str]:
    if not value or not value.strip():
        return f"{field_name} cannot be empty."
    return None


def validate_positive_integer(value: int, field_name: str) -> Optional[str]:
    if value is None or value < 0:
        return f"{field_name} must be a non-negative integer."
    return None
