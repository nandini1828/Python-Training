from typing import Any


def get_value_safe(data: dict[str, Any], key: str, default: Any = None) -> Any:
    return data.get(key, default)


def set_default_value(data: dict[str, Any], key: str, default: Any) -> dict[str, Any]:
    result = data.copy()
    result.setdefault(key, default)
    return result


def update_dictionary(data: dict[str, Any], updates: dict[str, Any]) -> dict[str, Any]:
    result = data.copy()
    result.update(updates)
    return result


def merge_with_override(first: dict[str, Any], second: dict[str, Any]) -> dict[str, Any]:
    result = first.copy()
    result.update(second)
    return result


def remove_key_safely(data: dict[str, Any], key: str) -> dict[str, Any]:
    result = data.copy()
    result.pop(key, None)
    return result


def key_exists(data: dict[str, Any], key: str) -> bool:
    return key in data


def filter_by_key(data: dict[str, Any], keys: list[str]) -> dict[str, Any]:
    return {k: data[k] for k in keys if k in data}


def clear_dictionary(data: dict[str, Any]) -> dict[str, Any]:
    return {}
