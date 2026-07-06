"""
list_iteration.py

Topic:
    - Accessing indices
    - Slicing lists
    - Looping over list elements

Real World Application:
    Inventory browsing and sublist extraction

Run:
    python list_iteration.py
"""

from typing import List


def list_iteration_and_slicing(products: List[str]) -> None:
    """
    Demonstrates list indexing, slicing, and looping.
    """
    print("\n--- List Iteration and Slicing ---")
    print(f"  Full inventory: {products}")

    print("  First two products:")
    for product in products[:2]:
        print(f"    - {product}")

    print("  Last product:")
    print(f"    - {products[-1]}")

    print("  Every second product:")
    for product in products[::2]:
        print(f"    - {product}")


def run() -> None:
    """
    Runs the list iteration example.
    """
    products = ["Laptop", "Mouse", "Monitor", "Keyboard"]
    list_iteration_and_slicing(products)


if __name__ == "__main__":
    run()
