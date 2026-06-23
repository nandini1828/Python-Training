"""
==================================================
Module: Introspection Utilities
Topic: Introspection
Author: Nandini

Description:
Provides utility functions for inspecting
Python objects at runtime.
==================================================
"""

from typing import Any


def inspect_object(obj: Any) -> None:
    """
    Display information about a Python object.

    Args:
        obj (Any): Any Python object.

    Returns:
        None
    """

    print("\n========== OBJECT INSPECTION ==========")

    print(f"Object Value      : {obj}")
    print(f"Object Type       : {type(obj)}")
    print(f"Class Name        : {obj.__class__.__name__}")
    print(f"Memory Address    : {id(obj)}")

    print("\nAttributes & Methods:")
    print(dir(obj))

    print("\n=======================================")