from __future__ import annotations

from tuple_methods.tuple_utils import count_occurrences, tuple_to_dict


def run_tuple_demo() -> None:
    """Show simple tuple operations for beginners."""

    numbers = (1, 2, 2, 3)
    print("First item:", numbers[0])
    print("Count of 2:", count_occurrences(numbers, 2))
    print("Mapping:", tuple_to_dict(("name", "age"), ("Ada", 21)))
