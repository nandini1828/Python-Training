"""
Simple JSON-like dictionary query utility supporting dot paths.
"""
from __future__ import annotations

from typing import Any, Mapping


def query_json(data_dict: Mapping[str, Any], path_str: str, default: Any = None) -> Any:
    """
    Traverse `data_dict` following `path_str` separated by dots.

    Args:
        data_dict: Nested mapping to query.
        path_str: Dot-delimited path, e.g. "user.profile.name".
        default: Value to return if traversal fails.

    Returns:
        The value at the target path or `default`.
    """
    if not path_str:
        return data_dict

    parts = path_str.split(".")
    current: Any = data_dict
    for part in parts:
        if isinstance(current, Mapping) and part in current:
            current = current[part]
        else:
            return default
    return current
