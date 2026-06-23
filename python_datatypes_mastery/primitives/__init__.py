"""
Primitives utilities package.

Contains modules for introspection, casting, and dunder examples.
"""

from .introspection import inspect_object
from .casting import safe_cast
from .dunder_examples import Employee, demo_dunders

__all__ = ["inspect_object", "safe_cast", "Employee", "demo_dunders"]
