from __future__ import annotations

import inspect
import logging
from typing import Any, Dict, List, Optional, Tuple

from ..logging_config import configure_logging

logger = configure_logging()


def _safe_getattr(obj: Any, name: str) -> Any:
    try:
        return getattr(obj, name)
    except Exception:
        return None


def _normalize_attribute_type(value: Any) -> str:
    if value is None:
        return "None"
    if isinstance(value, type):
        return f"class {value.__name__}"
    return type(value).__name__


def _extract_attributes(obj: Any) -> Dict[str, str]:
    attributes: Dict[str, str] = {}
    if isinstance(obj, dict):
        for key, value in obj.items():
            attributes[repr(key)] = _normalize_attribute_type(value)
        return attributes

    if hasattr(obj, "__dict__"):
        for key, value in vars(obj).items():
            attributes[key] = _normalize_attribute_type(value)
        return attributes

    if isinstance(obj, (list, tuple, set)):
        attributes["length"] = str(len(obj))
        attributes["sample"] = _normalize_attribute_type(next(iter(obj), None)) if obj else "empty"
        return attributes

    return attributes


def _extract_callable_signatures(obj: Any) -> Dict[str, Optional[str]]:
    signatures: Dict[str, Optional[str]] = {}
    for name in dir(obj):
        if name.startswith("__") and name.endswith("__"):
            continue
        candidate = _safe_getattr(obj, name)
        if callable(candidate):
            try:
                signatures[name] = str(inspect.signature(candidate))
            except (ValueError, TypeError):
                signatures[name] = None
    return signatures


def introspect_object(obj: Any) -> Dict[str, Any]:
    logger.info("Introspecting object of type %s", type(obj).__name__)
    type_name = obj.__name__ if inspect.isclass(obj) else type(obj).__name__
    docstring = inspect.getdoc(obj)
    module = inspect.getmodule(obj)
    module_name = module.__name__ if module is not None else None
    module_docstring = inspect.getdoc(module) if module is not None else None

    return {
        "type": type_name,
        "module": module_name,
        "repr": repr(obj),
        "docstring": docstring,
        "module_docstring": module_docstring,
        "attributes": _extract_attributes(obj),
        "callable_signatures": _extract_callable_signatures(obj),
    }
