"""
Object Inspector

Provides runtime inspection of Python objects.
Returns all public methods and their documentation.
"""

from typing import Any


def inspect_object(
    obj: Any
) -> dict:
    """
    Inspects any Python object and returns
    method information along with documentation.

    Parameters
    ----------
    obj : Any
        Any Python object.

    Returns
    -------
    dict
        Object metadata and method information.
    """

    methods = []

    for attribute_name in dir(obj):

        if attribute_name.startswith("_"):
            continue

        attribute = getattr(
            obj,
            attribute_name
        )

        if callable(attribute):

            methods.append(
                {
                    "method_name": attribute_name,
                    "documentation":
                        attribute.__doc__
                        or "No documentation available"
                }
            )

    return {
        "object_type": type(obj).__name__,
        "object_id": id(obj),
        "total_methods": len(methods),
        "methods": methods
    }


def get_method_names(obj: Any) -> list:
    """
    Get all public method names from an object.
    
    Parameters
    ----------
    obj : Any
        Any Python object.
    
    Returns
    -------
    list
        List of public method names.
    """
    methods = []
    for attribute_name in dir(obj):
        if attribute_name.startswith("_"):
            continue
        attribute = getattr(obj, attribute_name)
        if callable(attribute):
            methods.append(attribute_name)
    return methods


def get_docstrings(obj: Any) -> dict:
    """
    Get documentation for all public methods of an object.
    
    Parameters
    ----------
    obj : Any
        Any Python object or class.
    
    Returns
    -------
    dict
        Dictionary mapping method names to their docstrings.
    """
    docstrings = {}
    for attribute_name in dir(obj):
        if attribute_name.startswith("_"):
            continue
        try:
            attribute = getattr(obj, attribute_name)
            if callable(attribute):
                docstrings[attribute_name] = attribute.__doc__ or "No documentation"
        except AttributeError:
            continue
    return docstrings