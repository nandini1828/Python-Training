"""
demo.py

Demonstration of loop-else behavior.

Run:
    python demo.py
"""

from .utils import (
    find_prime,
    search_element_with_else,
    find_first_even_with_else,
    validate_all_positive,
    find_divisor,
    process_until_zero,
    find_with_while_else,
)


def demo_prime():
    print("\n=== PRIME CHECK (for-else) ===")
    for n in [1, 2, 3, 4, 17, 18]:
        print(f"{n} -> {find_prime(n)}")


def demo_search():
    print("\n=== SEARCH ELEMENT (for-else) ===")
    data = [10, 20, 30, 40]
    print("Find 30:", search_element_with_else(data, 30))
    print("Find 99:", search_element_with_else(data, 99))


def demo_even():
    print("\n=== FIRST EVEN (for-else) ===")
    print(find_first_even_with_else([1, 3, 5, 8]))
    print(find_first_even_with_else([1, 3, 5]))


def demo_validation():
    print("\n=== ALL POSITIVE CHECK ===")
    print(validate_all_positive([1, 2, 3]))
    print(validate_all_positive([1, -2, 3]))


def demo_divisor():
    print("\n=== FIND DIVISOR ===")
    print("15 ->", find_divisor(15))
    print("13 ->", find_divisor(13))  # prime


def demo_break_vs_else():
    print("\n=== BREAK vs ELSE ===")
    print("With zero:", process_until_zero([1, 2, 0, 5]))
    print("Without zero:", process_until_zero([1, 2, 3]))


def demo_while_else():
    print("\n=== WHILE-ELSE SEARCH ===")
    data = [5, 10, 15]
    print("Find 10:", find_with_while_else(data, 10))
    print("Find 99:", find_with_while_else(data, 99))


def main():
    print("=" * 60)
    print("LOOP ELSE DEMONSTRATION")
    print("=" * 60)

    demo_prime()
    demo_search()
    demo_even()
    demo_validation()
    demo_divisor()
    demo_break_vs_else()
    demo_while_else()

    print("\nAll loop-else demos executed successfully.")


if __name__ == "__main__":
    main()