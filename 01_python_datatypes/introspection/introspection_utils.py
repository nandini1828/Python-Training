"""introspection.introspection_utils
=====================================
Utilities for runtime inspection and documentation extraction.

This module provides a generic introspection engine that returns a
structured dictionary describing Python objects. It also exposes helpers
to extract documentation and list available methods.
"""

from typing import Any, Dict, List
import inspect
import logging

logger = logging.getLogger(__name__)


def inspect_object(obj: Any) -> Dict[str, Any]:
    """Inspect any Python object and return structured metadata.

    Args:
        obj: Any Python object to inspect.

    Returns:
        A dictionary containing type, class name, module, memory address,
        documentation and details about attributes and methods.
    """

    logger.debug("Inspecting object of type: %s", type(obj))

    obj_type = type(obj)
    class_name = obj_type.__name__
    module = getattr(obj_type, "__module__", None)
    memory_address = hex(id(obj))
    docstring = inspect.getdoc(obj) or inspect.getdoc(obj_type) or ""

    # Attributes (non-callable)
    attributes: Dict[str, Any] = {}
    methods: List[str] = []
    callable_methods: List[str] = []
    dunder_methods: List[str] = []

    all_names = dir(obj)

    for name in all_names:
        try:
            value = getattr(obj, name)
        except Exception:
            continue

        if name.startswith("__") and name.endswith("__"):
            dunder_methods.append(name)

        if inspect.isroutine(value):
            methods.append(name)
            if callable(value):
                callable_methods.append(name)
        else:
            # Use vars() where possible to show object attributes
            attributes[name] = value

    annotations = getattr(obj, "__annotations__", None) or getattr(obj_type, "__annotations__", None) or {}
    try:
        mro = [c.__name__ for c in obj_type.__mro__]
    except Exception:
        mro = []

    result: Dict[str, Any] = {
        "type": str(obj_type),
        "class_name": class_name,
        "module": module,
        "memory_address": memory_address,
        "docstring": docstring,
        "attributes": attributes,
        "methods": sorted(set(methods)),
        "callable_methods": sorted(set(callable_methods)),
        "dunder_methods": sorted(set(dunder_methods)),
        "annotations": annotations,
        "mro": mro,
    }

    logger.info("Completed inspection for %s", class_name)

    return result


def get_documentation(obj: Any) -> str:
    """Aggregate documentation strings for an object.

    This function returns the object's docstring as well as module, class
    and method docstrings where applicable.
    """

    logger.debug("Extracting documentation for: %s", getattr(obj, "__name__", type(obj)))

    parts: List[str] = []

    # Module docstring
    module = getattr(obj, "__module__", None)
    if module:
        try:
            mod = __import__(module)
            mod_doc = inspect.getdoc(mod) or ""
            if mod_doc:
                parts.append(f"Module ({module}):\n{mod_doc}")
        except Exception:
            pass

    # Object/class docstring
    obj_doc = inspect.getdoc(obj)
    if obj_doc:
        parts.append(f"Object Docstring:\n{obj_doc}")

    # If it's a class or instance, include method docstrings
    try:
        for name in dir(obj):
            if name.startswith("__") and name.endswith("__"):
                continue
            try:
                member = getattr(obj, name)
            except Exception:
                continue
            if inspect.isroutine(member):
                doc = inspect.getdoc(member)
                if doc:
                    parts.append(f"{name}():\n{doc}")
    except Exception:
        pass

    return "\n\n".join(parts).strip()


def get_methods(obj: Any) -> List[str]:
    """Return a list of method names available on the object.

    Args:
        obj: The object to inspect.

    Returns:
        Sorted list of method names.
    """

    names = []
    for name in dir(obj):
        try:
            member = getattr(obj, name)
        except Exception:
            continue
        if callable(member):
            names.append(name)

    return sorted(set(names))
