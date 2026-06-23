"""
Method Inspector

Provides functionality to extract
all public methods from any object.
"""


class MethodInspector:

    @staticmethod
    def get_methods(obj) -> list[str]:
        """
        Returns all public callable methods
        from the given object.

        Parameters
        ----------
        obj : object
            Any Python object.

        Returns
        -------
        list[str]
            List of public method names.
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
                    attribute_name
                )

        return methods


def get_method_names(obj) -> list[str]:
    """Get all public method names from an object.
    
    Parameters
    ----------
    obj : object
        Any Python object.
    
    Returns
    -------
    list[str]
        List of public method names.
    """
    return MethodInspector.get_methods(obj)