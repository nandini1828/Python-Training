def safe_int(value: str) -> int | None:
    try:
        return int(value)
    except ValueError:
        return None


def safe_float(value: str) -> float | None:
    try:
        return float(value)
    except ValueError:
        return None


def string_to_bool(value: str) -> bool | None:
    cleaned_value = value.strip().lower()

    if cleaned_value in ["true", "yes", "1"]:
        return True
    if cleaned_value in ["false", "no", "0"]:
        return False
    return None
