"""
Classes package exposing Student, Computer and deconstructor utilities.
"""

from .student import Student
from .computer import CPU, Computer
from .object_deconstructor import deconstruct_object

__all__ = ["Student", "CPU", "Computer", "deconstruct_object"]
