"""
set_iteration.py

Topic:
    - Set creation from a list
    - Fast membership testing
    - Iterating over set items

Real World Application:
    Product availability checks and duplicate elimination

Run:
    python set_iteration.py
"""

from typing import List


def set_membership_and_looping(products: List[str]) -> set:
    """
    Demonstrates fast membership testing with sets and returns the product set.
    """
    return set(products)


def run() -> None:
    """
    Runs the set membership example.
    """
    products = ["Laptop", "Mouse", "Monitor", "Keyboard"]
    product_set = set_membership_and_looping(products)

    print("\n--- Set Membership and Looping ---")
    print(f"  Product set: {product_set}")

    search_items = ["Laptop", "Tablet", "Mouse"]
    for item in search_items:
        in_set = item in product_set
        print(f"    - {item}: {'available' if in_set else 'not available'}")

    print("  Looping over the set:")
    for product in product_set:
        print(f"    - {product}")


if __name__ == "__main__":
    run()
