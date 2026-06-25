from __future__ import annotations

import inspect
from typing import Any, Dict, List


class IntrospectionHelper:
    """A simple helper that shows how Python can inspect objects."""

    def __init__(self, target: Any) -> None:
        self.target = target

    def inspect(self) -> Dict[str, Any]:
        """Return a simple summary of the object."""
        kind = self._find_kind()
        attributes = [name for name in dir(self.target) if not name.startswith("__")]
        methods = [name for name in dir(self.target) if callable(getattr(self.target, name)) and not name.startswith("__")]

        return {
            "kind": kind,
            "type_name": type(self.target).__name__,
            "is_callable": callable(self.target),
            "attributes": sorted(attributes),
            "methods": methods,
        }

    def _find_kind(self) -> str:
        """Return a simple label for the object's type."""
        if inspect.isfunction(self.target) or inspect.ismethod(self.target) or inspect.isbuiltin(self.target):
            return "function"
        if inspect.isclass(self.target):
            return "class"
        if isinstance(self.target, (list, tuple, set, dict, str, int, float, bool)):
            return type(self.target).__name__
        return "instance"


def inspect_object(target: Any) -> Dict[str, Any]:
    """Inspect an object using a beginner-friendly helper."""
    return IntrospectionHelper(target).inspect()


def extract_documentation(target: Any) -> Dict[str, Any]:
    """Return the docstrings attached to an object."""
    return {
        "docstring": inspect.getdoc(target),
        "module_docstring": inspect.getmodule(target).__doc__ if inspect.getmodule(target) else None,
    }


def list_available_methods(target: Any) -> List[str]:
    """Return all callable methods exposed by an object."""
    return [name for name in dir(target) if callable(getattr(target, name)) and not name.startswith("__")]
