"""
Introspection Inspector

Provides utilities to:
1. Get all callable methods of any Python object.
2. Get methods along with their documentation.
"""

import inspect


def get_methods(obj):
    """
    Returns a list of all callable methods
    available on the given object.

    Args:
        obj: Any Python object

    Returns:
        list[str]
    """

    methods = []

    for name in dir(obj):

        attribute = getattr(obj, name)

        if callable(attribute):
            methods.append(name)

    return methods


def get_methods_and_docs(obj):
    """
    Returns all callable methods and
    their associated documentation.

    Args:
        obj: Any Python object

    Returns:
        list[dict]
    """

    results = []

    for name in dir(obj):

        attribute = getattr(obj, name)

        if callable(attribute):

            results.append(
                {
                    "method": name,
                    "doc": inspect.getdoc(attribute)
                }
            )

    return results