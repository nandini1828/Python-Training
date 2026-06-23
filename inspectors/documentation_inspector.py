"""
Documentation Inspector

Provides functionality to retrieve
method documentation from any object.
"""

from .method_inspector import MethodInspector


class DocumentationInspector:

    @staticmethod
    def inspect(obj) -> dict:
        """
        Returns method names and their
        associated documentation.

        Parameters
        ----------
        obj : object
            Any Python object.

        Returns
        -------
        dict
            Object metadata and method details.
        """

        method_details = []

        for method_name in (
            MethodInspector.get_methods(obj)
        ):

            method = getattr(
                obj,
                method_name
            )

            method_details.append(
                {
                    "method_name": method_name,
                    "documentation":
                        method.__doc__
                        or "No documentation available"
                }
            )

        return {
            "object_type": type(obj).__name__,
            "object_id": id(obj),
            "total_methods": len(
                method_details
            ),
            "methods": method_details
        }


def get_docstrings(obj) -> dict:
    """Get method names and their docstrings from an object.
    
    Parameters
    ----------
    obj : object
        Any Python object or class.
    
    Returns
    -------
    dict
        Object metadata and method documentation details.
    """
    return DocumentationInspector.inspect(obj)