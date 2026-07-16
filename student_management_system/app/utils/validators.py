from typing import Any


def ensure_positive_int(value: Any, field_name: str) -> int:
    if not isinstance(value, int) or isinstance(value, bool) or value < 1:
        raise ValueError(f"{field_name} must be a positive integer")
    return value


def validate_status(status: str) -> str:
    allowed = {"present", "absent", "late", "excused"}
    if status not in allowed:
        raise ValueError("status must be one of: present, absent, late, excused")
    return status
