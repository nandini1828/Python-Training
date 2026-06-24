import inspect
import logging
from typing import Any, Dict, Optional

from ..logging_config import configure_logging

logger = configure_logging()


def _document_methods(clazz: Any) -> Dict[str, Optional[str]]:
    method_docs: Dict[str, Optional[str]] = {}
    for attribute_name in dir(clazz):
        if attribute_name.startswith("__") and attribute_name.endswith("__"):
            continue
        attribute_value = getattr(clazz, attribute_name, None)
        if inspect.isfunction(attribute_value) or inspect.ismethod(attribute_value):
            method_docs[attribute_name] = inspect.getdoc(attribute_value)
    return method_docs


def extract_documentation(obj: Any) -> Dict[str, Any]:
    logger.info("Extracting documentation for object type %s", type(obj).__name__)
    module = inspect.getmodule(obj)
    class_docstring: Optional[str] = None
    method_docstrings: Dict[str, Optional[str]] = {}

    if inspect.isclass(obj):
        class_docstring = inspect.getdoc(obj)
        method_docstrings = _document_methods(obj)
    elif hasattr(obj, "__class__"):
        clazz = obj.__class__
        class_docstring = inspect.getdoc(clazz)
        method_docstrings = _document_methods(clazz)

    return {
        "docstring": inspect.getdoc(obj),
        "module_docstring": inspect.getdoc(module) if module is not None else None,
        "class_docstring": class_docstring,
        "method_docstrings": method_docstrings,
    }
