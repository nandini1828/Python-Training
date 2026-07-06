"""
loop_foundations package.

This package demonstrates Python's looping constructs and iteration
control statements.

Topics covered:
- for loops
- while loops
- break
- continue
- pass
- for-else
- while-else

Author: Python Training
"""

from .loops import (
    count_characters,
    factorial,
    iterate_dictionary,
    iterate_list,
    iterate_string,
    iterate_tuple,
    sum_numbers,
)

from .break_continue import (
    find_first_even,
    skip_negative_numbers,
    stop_at_value,
)

from .for_else_while_else import (
    is_prime,
    search_item,
)

__all__ = [
    "count_characters",
    "factorial",
    "iterate_dictionary",
    "iterate_list",
    "iterate_string",
    "iterate_tuple",
    "sum_numbers",
    "find_first_even",
    "skip_negative_numbers",
    "stop_at_value",
    "is_prime",
    "search_item",
]