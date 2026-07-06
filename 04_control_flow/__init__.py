"""
control_flow package.

This package demonstrates Python's control flow concepts, including:

- Conditional statements
- Truthy and falsy values
- Logical operators
- Short-circuit evaluation
- Ternary expressions
- Structural pattern matching (Python 3.10+)

The package is designed for educational purposes and follows
enterprise Python coding standards.
"""

from .conditionals import (
    calculate_grade,
    determine_discount,
    is_adult,
)

from .truthy_falsy import is_truthy

from .logical_operators import (
    can_access_admin_panel,
    is_eligible_for_loan,
)

from .short_circuit import (
    get_cached_value,
)

from .ternary_operator import (
    determine_status,
)

from .pattern_matching import (
    get_http_status_message,
)

__all__ = [
    "calculate_grade",
    "determine_discount",
    "is_adult",
    "is_truthy",
    "can_access_admin_panel",
    "is_eligible_for_loan",
    "get_cached_value",
    "determine_status",
    "get_http_status_message",
]