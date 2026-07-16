def next_id(items: list[object], id_name: str) -> int:
    if not items:
        return 1
    return max(getattr(item, id_name) for item in items) + 1


def describe_object(value: object) -> dict[str, object]:
    return {
        "value": str(value),
        "type": type(value).__name__,
        "is_string": isinstance(value, str),
        "first_five_dir_names": dir(value)[:5],
    }
