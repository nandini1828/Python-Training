"""Simple entry point for the iteration helpers project."""

from iterators.boolean_ops import has_all_true, has_any_true
from iterators.enumerate_ops import enumerate_items
from iterators.range_ops import generate_range
from iterators.reversed_ops import reverse_items
from iterators.sorted_ops import sort_items
from iterators.zip_ops import zip_items


def main() -> None:
    print("range:", generate_range(1, 10, 2))
    print("enumerate:", enumerate_items(["a", "b", "c"]))
    print("zip:", zip_items([1, 2], ["x", "y"]))
    print("reversed:", reverse_items([1, 2, 3]))
    print("sorted:", sort_items([3, 1, 2]))
    print("any:", has_any_true([False, True, False]))
    print("all:", has_all_true([True, True, True]))


if __name__ == "__main__":
    main()
