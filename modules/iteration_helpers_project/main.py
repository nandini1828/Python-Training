"""Simple entry point for the iteration helpers project."""

from iterators.boolean_ops import has_any_true, has_all_true
from iterators.enumerate_ops import enumerate_items
from iterators.range_ops import generate_range
from iterators.reversed_ops import reverse_items
from iterators.sorted_ops import sort_items
from iterators.zip_ops import zip_items


def display_results():
    results = {
        "range": generate_range(1, 10, 2),
        "enumerate": enumerate_items(["a", "b", "c"]),
        "zip": zip_items([1, 2], ["x", "y"]),
        "reversed": reverse_items([1, 2, 3]),
        "sorted": sort_items([3, 1, 2]),
        "any": has_any_true([False, True, False]),
        "all": has_all_true([True, True, True]),
    }

    for operation, output in results.items():
        print(f"{operation}: {output}")


def main():
    display_results()


if __name__ == "__main__":
    main()