"""
Collect callable methods and their documentation for any object.
"""
from __future__ import annotations

import inspect
from typing import Any, Dict


def get_methods_and_docs(obj: Any) -> Dict[str, str]:
    """
    Return a mapping of callable attribute names to their documentation strings.

    Args:
        obj: Any Python object to inspect.

    Returns:
        A dict where keys are method names and values are docstrings (possibly empty).
    """
    methods: Dict[str, str] = {}
    for name in dir(obj):
        try:
            attribute = getattr(obj, name)
        except Exception:
            continue
        if callable(attribute):
            doc = inspect.getdoc(attribute) or ""
            methods[name] = doc
    return methods
