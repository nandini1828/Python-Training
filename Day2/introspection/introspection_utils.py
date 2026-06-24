from __future__ import annotations

import inspect
import logging
from typing import Any, Dict, List, Sequence, Union

logger = logging.getLogger(__name__)


def inspect_object(target: Any) -> Dict[str, Any]:
    """Return a structured summary of an object's runtime characteristics."""

    logger.info("Inspecting object of type %s", type(target).__name__)
    kind = "unknown"
    if isinstance(target, str):
        kind = "str"
    elif isinstance(target, int):
        kind = "int"
    elif isinstance(target, float):
        kind = "float"
    elif isinstance(target, list):
        kind = "list"
    elif isinstance(target, tuple):
        kind = "tuple"
    elif isinstance(target, set):
        kind = "set"
    elif isinstance(target, dict):
        kind = "dict"
    elif inspect.isfunction(target) or inspect.ismethod(target) or inspect.isbuiltin(target):
        kind = "function"
    elif inspect.isclass(target):
        kind = "class"
    elif inspect.isroutine(target):
        kind = "routine"
    else:
        kind = "instance"

    signature = None
    try:
        signature = str(inspect.signature(target))
    except (TypeError, ValueError):
        signature = None

    attributes = sorted([name for name in dir(target) if not name.startswith("__")])
    if inspect.isfunction(target) or inspect.ismethod(target) or inspect.isbuiltin(target):
        attributes = sorted(["__name__", "__module__", *attributes])

    methods_with_docs = {
        name: inspect.getdoc(getattr(target, name))
        for name in dir(target)
        if callable(getattr(target, name)) and not name.startswith("__")
    }

    return {
        "kind": kind,
        "type_name": type(target).__name__,
        "is_callable": callable(target),
        "attributes": attributes,
        "instance_attributes": sorted([name for name in vars(target).keys()]) if hasattr(target, "__dict__") else [],
        "methods": list_available_methods(target),
        "methods_with_docs": methods_with_docs,
        "signature": signature,
        "doc": inspect.getdoc(target),
    }


def extract_documentation(target: Any) -> Dict[str, Any]:
    """Return the docstrings attached to an object, module, class, and methods."""

    logger.info("Extracting documentation for %s", getattr(target, "__name__", type(target).__name__))
    return {
        "docstring": inspect.getdoc(target),
        "module_docstring": inspect.getmodule(target).__doc__ if inspect.getmodule(target) else None,
        "class_docstring": inspect.getdoc(type(target)) if inspect.isclass(target) else None,
        "method_docstrings": {
            name: inspect.getdoc(getattr(target, name))
            for name in dir(target)
            if callable(getattr(target, name)) and not name.startswith("__")
        },
    }


def list_available_methods(target: Any) -> List[str]:
    """Return all callable methods and functions exposed by an object."""

    logger.info("Listing methods for %s", type(target).__name__)
    return [name for name in dir(target) if callable(getattr(target, name)) and not name.startswith("__")]


def query_json(payload: Any, path: Union[str, Sequence[str], None]) -> Any:
    """Safely query nested JSON-like structures using dot notation or sequence paths."""

    logger.info("Querying JSON path %s", path)
    if path is None:
        return None

    if isinstance(path, str):
        parts = [segment for segment in path.split(".") if segment]
    else:
        parts = [segment for segment in path if segment]

    current: Any = payload
    for part in parts:
        if isinstance(current, dict) and part in current:
            current = current[part]
        elif isinstance(current, list) and part.isdigit():
            index = int(part)
            if 0 <= index < len(current):
                current = current[index]
            else:
                return None
        else:
            return None
    return current
