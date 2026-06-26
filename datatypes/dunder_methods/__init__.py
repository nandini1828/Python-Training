"""
Dunder Methods Module

This module demonstrates magic methods (dunder methods) that allow
operator overloading and special behavior in classes.
"""

from .custom_number import CustomNumber
from .custom_string import CustomString
from .comparison_examples import ComparisonExamples
from .arithmetic_examples import ArithmeticExamples

__all__ = [
    "CustomNumber",
    "CustomString",
    "ComparisonExamples",
    "ArithmeticExamples",
]
