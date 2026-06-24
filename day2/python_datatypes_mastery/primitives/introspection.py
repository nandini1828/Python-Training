from typing import Any


class ObjectInspector:
    """
    Utility class for Python object introspection.

    Demonstrates:
    - type()
    - id()
    - dir()
    - isinstance()
    - callable()
    """

    @staticmethod
    def get_type(obj: Any) -> type:
        """
        Returns the type of the object.
        """
        return type(obj)

    @staticmethod
    def get_id(obj: Any) -> int:
        """
        Returns the memory identifier of the object.
        """
        return id(obj)

    @staticmethod
    def get_attributes(obj: Any) -> list[str]:
        """
        Returns all attributes and methods
        available on the object.
        """
        return dir(obj)

    @staticmethod
    def is_instance(obj: Any, cls: type) -> bool:
        """
        Checks whether the object
        is an instance of the given class.
        """
        return isinstance(obj, cls)

    @staticmethod
    def is_callable(obj: Any) -> bool:
        """
        Checks whether the object
        can be called like a function.
        """
        return callable(obj)