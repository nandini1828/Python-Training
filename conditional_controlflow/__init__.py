"""
Control Flow Package

This package demonstrates Python control flow concepts
using a Smart ATM System.

Modules:
    - conditionals
    - truthy_falsy
    - logical_operators
    - short_circuit
    - ternary_operator
    - pattern_matching
"""

from . import conditionals
from . import truthy_falsy
from . import logical_operators
from . import short_circuit
from . import terinary_operators as ternary_operator
from . import pattern_matching

__all__ = [
    "conditionals",
    "truthy_falsy",
    "logical_operators",
    "short_circuit",
    "ternary_operator",
    "pattern_matching",
]