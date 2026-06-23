"""
Utility module to extract documentation and methods from any Python object.
"""

import inspect


def get_object_docs(obj):
    """
    Returns the __doc__ string of any object safely.
    """

    return inspect.getdoc(obj)


def get_methods_with_docs(obj):
    """
    Returns all methods of an object with their documentation.

    Output format:
    [
        {"method": "method_name", "doc": "documentation"},
        ...
    ]
    """

    result = []

    for name in dir(obj):

        attribute = getattr(obj, name)

        if callable(attribute):

            result.append({
                "method": name,
                "doc": inspect.getdoc(attribute)
            })

    return result