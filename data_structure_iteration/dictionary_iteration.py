"""
dictionary_iteration.py

Topic:
    - Iterating over dictionary keys
    - Iterating over dictionary values
    - Iterating over dictionary items

Real World Application:
    Inventory lookup and summary reporting

Run:
    python dictionary_iteration.py
"""

from typing import List


def dictionary_iteration(keys: List[str], values: List[int]) -> dict:
    """
    Demonstrates dictionary iteration using keys(), values(), and items().
    Returns the created dictionary for testing.
    """
    inventory = dict(zip(keys, values))
    return inventory


def run() -> None:
    """
    Runs the dictionary iteration example.
    """
    inventory = dictionary_iteration(["Laptop", "Mouse", "Monitor", "Keyboard"], [15, 0, 8, 25])

    print("\n--- Dictionary Iteration ---")
    print(f"  Inventory map: {inventory}")

    print("  Keys:")
    for key in inventory.keys():
        print(f"    - {key}")

    print("  Values:")
    for value in inventory.values():
        print(f"    - {value}")

    print("  Items:")
    for key, value in inventory.items():
        print(f"    - {key}: {value} units")


if __name__ == "__main__":
    run()
