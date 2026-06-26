"""
Primitive Data Types Module

This module demonstrates and teaches Python's fundamental primitive data types:
- integers: whole numbers (positive, negative, zero)
- floats: decimal numbers with precision considerations
- strings: text and character sequences
- booleans: True/False logical values
"""

from .integer_demo import IntegerDemo
from .float_demo import FloatDemo
from .string_demo import StringDemo
from .boolean_demo import BooleanDemo
from .primitive_manager import PrimitiveManager

__all__ = [
    "IntegerDemo",
    "FloatDemo",
    "StringDemo",
    "BooleanDemo",
    "PrimitiveManager",
]
