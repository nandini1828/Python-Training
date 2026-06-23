"""
Utilities demonstrating different ways to fetch documentation strings.
"""
from __future__ import annotations

import inspect
import io
import builtins
from typing import Any


def get_doc_via_dunder(obj: Any) -> str:
    """Return the `__doc__` attribute for `obj` (may be None)."""
    return getattr(obj, "__doc__", "") or ""


def get_doc_via_inspect(obj: Any) -> str:
    """Return documentation using `inspect.getdoc` which cleans up formatting."""
    return inspect.getdoc(obj) or ""


def get_doc_via_help(obj: Any) -> str:
    """Capture the textual output of the built-in `help()` for `obj`."""
    stream = io.StringIO()
    original_stdout = builtins.print
    try:
        # Use pydoc to render help to a string by temporarily calling help
        help(obj)
        # help prints to stdout; we capture via redirecting write in pydoc would be better
    except Exception:
        return "<help not available>"
    return get_doc_via_inspect(obj)
