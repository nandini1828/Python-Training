"""
Utilities demonstrating Python introspection.

This module provides `inspect_object` which returns a dictionary with the
object's type, id, and a mapping of visible attributes and their types.
"""
from __future__ import annotations

import inspect
from typing import Any, Dict, List


def inspect_object(obj: Any) -> Dict[str, Any]:
    """
    Inspect a Python object and return key metadata.

    Args:
        obj: Any Python object to inspect.

    Returns:
        A dictionary with keys `type`, `id`, and `attributes` where
        `attributes` is a dict of attribute name -> type name.
    """
    attr_names: List[str] = sorted(dir(obj))
    attributes = {}
    for name in attr_names:
        try:
            value = getattr(obj, name)
            attributes[name] = type(value).__name__
        except Exception:
            attributes[name] = "<unreadable>"

    return {
        "type": type(obj).__name__,
        "id": id(obj),
        "attributes": attributes,
    }


class Parent:
    """Example base class for isinstance/type demo."""


class Child(Parent):
    """Example subclass for isinstance/type demo."""


def demo_type_vs_isinstance() -> Dict[str, bool]:
    """
    Demonstrate the difference between `type()` and `isinstance()`.

    Returns:
        A mapping with boolean results for comparisons between `type` and
        `isinstance` using `Parent` and `Child`.
    """
    child = Child()
    return {
        "type_is_parent": type(child) is Parent,
        "isinstance_parent": isinstance(child, Parent),
        "type_is_child": type(child) is Child,
        "isinstance_child": isinstance(child, Child),
    }


def get_source(obj: Any) -> str:
    """
    Return source code for an object if available using inspect.

    Args:
        obj: The target object.

    Returns:
        Source code string or an explanatory message.
    """
    try:
        return inspect.getsource(obj)
    except (TypeError, OSError, IOError):
        return "<source not available>"
