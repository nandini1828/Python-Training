"""
Section 1: Primitives, Introspection & Naming Conventions
"""


def get_object_type(obj):
    """
    Returns the type of the object.
    """
    return type(obj)


def get_object_id(obj):
    """
    Returns the unique identifier of the object.
    """
    return id(obj)


def get_object_attributes(obj):
    """
    Returns all attributes and methods available on the object.
    """
    return dir(obj)


def inspect_object(obj):
    """
    Returns complete introspection information.
    """

    return {
        "type": type(obj),
        "id": id(obj),
        "attributes": dir(obj)
    }


def list_public_attributes(obj):
    """
    Returns only public attributes and methods.
    Public members do not start with '_'.
    """

    return [
        attribute
        for attribute in dir(obj)
        if not attribute.startswith("_")
    ]