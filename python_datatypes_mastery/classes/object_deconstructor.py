"""
Recursive deconstruction of complex Python objects into JSON-serializable structures.
"""
from __future__ import annotations

from typing import Any, Dict, List


def deconstruct_object(obj: Any) -> Any:
    """
    Recursively convert Python objects (including custom objects) into
    primitives (dicts, lists, tuples) suitable for JSON serialization.

    Rules:
    - Primitive types (int, float, str, bool, None) are returned as-is.
    - dict: each value is deconstructed.
    - list/tuple: each element is deconstructed and original type preserved for tuple.
    - custom objects: use `__dict__` when available and deconstruct it.

    Args:
        obj: Any Python object.

    Returns:
        A structure composed of primitives, dicts, lists, and tuples.
    """
    primitive_types = (str, int, float, bool, type(None))

    if isinstance(obj, primitive_types):
        return obj

    if isinstance(obj, dict):
        return {k: deconstruct_object(v) for k, v in obj.items()}

    if isinstance(obj, list):
        return [deconstruct_object(x) for x in obj]

    if isinstance(obj, tuple):
        return tuple(deconstruct_object(x) for x in obj)

    if hasattr(obj, "__dict__"):
        return deconstruct_object(obj.__dict__)

    # Fallback: try to convert iterables
    try:
        iterator = iter(obj)  # type: ignore
    except TypeError:
        return repr(obj)
    else:
        return [deconstruct_object(x) for x in iterator]
