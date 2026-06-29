"""
Introspection Package

This package contains utilities for examining
Python objects at runtime.
"""

from .introspection_utils import (
	inspect_object,
	get_documentation,
	get_methods,
)

__all__ = ["inspect_object", "get_documentation", "get_methods"]