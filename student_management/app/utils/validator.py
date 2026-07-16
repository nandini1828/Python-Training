def is_valid_age(age: int) -> bool:
    return 0 < age < 120


def is_non_empty_text(value: str) -> bool:
    return bool(value and value.strip())


def is_valid_duration(duration_weeks: int) -> bool:
    return 0 < duration_weeks <= 52
