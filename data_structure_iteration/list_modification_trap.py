"""
list_modification_trap.py

Topic:
    - Unsafe removal while iterating
    - Safe list filtering

Real World Application:
    Order processing and batch cleanup

Run:
    python list_modification_trap.py
"""

from typing import List


def why_list_removal_skips_items() -> None:
    """Shows why removing while iterating can skip elements."""
    print("\n--- Why Removal Skips Items ---")
    numbers = [1, 2, 3, 4, 5]
    print(f"  Original numbers: {numbers}")

    for number in numbers:
        if number % 2 == 0:
            numbers.remove(number)
        print(f"    step -> {numbers}")

    print(f"  Result after unsafe removal: {numbers}")


def list_modification_trap() -> List[str]:
    """
    Demonstrates the list modification trap and returns the safe result.
    """
    orders = ["order-001", "order-002", "order-003", "order-004"]

    # Safe pattern: build a new list or iterate over a copy
    safe_list = [order for order in orders if not order.endswith("002") and not order.endswith("004")]
    return safe_list


def run() -> None:
    """
    Runs the list modification trap example.
    """
    print("\n--- List Modification Trap ---")
    why_list_removal_skips_items()

    orders = ["order-001", "order-002", "order-003", "order-004"]
    print(f"  Original orders: {orders}")

    print("  Safe removal using list comprehension:")
    safe_list = list_modification_trap()
    print(f"    {safe_list}")


if __name__ == "__main__":
    run()
