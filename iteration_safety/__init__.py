"""
iteration_safety package.

This package demonstrates safe iteration techniques, defensive
programming patterns, and collection mutation strategies in Python.

Topics covered:

- Safe list iteration
- Safe dictionary iteration
- Safe set iteration
- Copy vs Reference
- Mutation patterns
- Defensive iteration

Author: Python Training
"""

from .safe_list_iteration import (
    filter_even_numbers,
    remove_duplicates,
    remove_negative_numbers,
)

from .safe_dictionary_iteration import (
    remove_empty_values,
    remove_keys,
    uppercase_keys,
)

from .safe_set_iteration import (
    filter_even_set,
    remove_small_values,
)

from .copy_vs_reference import (
    create_deep_copy,
    create_shallow_copy,
    demonstrate_reference,
)

from .mutation_patterns import (
    filter_positive_numbers,
    replace_negative_numbers,
)

from .defensive_iteration import (
    safe_batch_processing,
    safe_snapshot_iteration,
)

__all__ = [
    "filter_even_numbers",
    "remove_duplicates",
    "remove_negative_numbers",
    "remove_empty_values",
    "remove_keys",
    "uppercase_keys",
    "filter_even_set",
    "remove_small_values",
    "create_deep_copy",
    "create_shallow_copy",
    "demonstrate_reference",
    "filter_positive_numbers",
    "replace_negative_numbers",
    "safe_batch_processing",
    "safe_snapshot_iteration",
]