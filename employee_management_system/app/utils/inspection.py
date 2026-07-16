"""Inspection utility to show public methods and documentation of objects."""

import inspect


def inspect_object(obj: object) -> dict[str, object]:
    """Return public methods and docstrings for an object."""
    public_methods = [
        name
        for name in dir(obj)
        if not name.startswith("_") and callable(getattr(obj, name, None))
    ]
    method_docs = {
        name: getattr(getattr(obj, name, None), "__doc__", "")
        for name in public_methods
    }
    return {
        "public_methods": public_methods,
        "method_docs": method_docs,
        "module": obj.__class__.__module__,
        "inspect": inspect.getsource(obj.__class__) if inspect.isclass(obj) else "",
    }
