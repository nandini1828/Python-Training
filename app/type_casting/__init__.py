"""
Type Casting Module

This module demonstrates safe and unsafe type casting operations,
including conversion between primitive types and error handling.
"""

from .safe_cast import SafeCast
from .string_casting import StringCasting
from .numeric_casting import NumericCasting
from .boolean_casting import BooleanCasting

__all__ = [
    "SafeCast",
    "StringCasting",
    "NumericCasting",
    "BooleanCasting",
]
