"""
Practical demonstrations of nested comprehension helpers.
"""

from .utils import (
    filter_nested,
    flatten_nested_lists,
    matrix_transpose,
    multiplication_table,
    pairs,
)


def main():
    print("\n===== Nested Comprehension Demo =====")
    matrix = [[1, 2], [3, 4]]
    print("Transpose:", matrix_transpose(matrix))
    print("Pairs:", pairs([1, 2, 3]))
    print("Flatten:", flatten_nested_lists([[1], [2, 3]]))
    print("Filtered:", filter_nested(matrix, 2))
    print("Table:", multiplication_table(3))


if __name__ == "__main__":
    main()
