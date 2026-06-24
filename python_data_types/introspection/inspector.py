import inspect
from typing import Any


def get_type(obj: Any) -> type:
    """
    Return the type of an object.
    """
    return type(obj)


def get_id(obj: Any) -> int:
    """
    Return the memory ID of an object.
    """
    return id(obj)


def get_all_attributes(obj: Any) -> list[str]:
    """
    Return all attributes and methods of an object.
    """
    return dir(obj)


def get_public_attributes(obj: Any) -> list[str]:
    """
    Return only public attributes (ignores _ and __ attributes).
    """
    return [
        attr
        for attr in dir(obj)
        if not attr.startswith("_")
    ]


def get_doc(obj: Any) -> str | None:
    """
    Return the documentation string (__doc__) of an object.
    """
    return inspect.getdoc(obj)


def get_methods(obj: Any) -> list[str]:
    """
    Return all callable methods of an object.
    """
    return [
        attr
        for attr in dir(obj)
        if callable(getattr(obj, attr))
    ]


def get_methods_with_docs(obj: Any) -> list[dict[str, str | None]]:
    """
    Return all methods along with their documentation.
    """
    result: list[dict[str, str | None]] = []

    for attr in dir(obj):
        value = getattr(obj, attr)

        if callable(value):
            result.append(
                {
                    "method": attr,
                    "doc": inspect.getdoc(value),
                }
            )

    return result