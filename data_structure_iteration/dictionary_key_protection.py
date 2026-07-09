"""
dictionary_key_protection.py

Topic:
    - Safe dictionary lookup with get()
    - Automatic defaults with defaultdict

Real World Application:
    Avoiding missing inventory errors in stock lookups

Run:
    python dictionary_key_protection.py
"""

from collections import defaultdict


def missing_key_strategy_demo() -> None:
    """Shows when to use get(), setdefault(), and defaultdict."""
    print("\n--- Missing Key Strategies ---")
    product_stock = {"Laptop": 15, "Mouse": 0, "Keyboard": 8}

    print("  Using dict.get() for one-off lookups:")
    print(f"    Headphones: {product_stock.get('Headphones', 0)} units")

    print("  Using setdefault() when you want to create a missing key:")
    updated_stock = product_stock.copy()
    updated_stock.setdefault("Headphones", 0)
    print(f"    Updated stock: {updated_stock}")

    print("  Using defaultdict() for repeated missing-key access:")
    default_stock = defaultdict(int)
    default_stock.update(product_stock)
    print(f"    Headphones: {default_stock['Headphones']} units")
    print("  Notes: get() is safest for read-only lookups, setdefault() mutates when needed, and defaultdict is convenient for repeated defaults.")


def dictionary_key_protection() -> dict:
    """
    Demonstrates protecting dictionary access using get() and defaultdict.
    Returns the default stock mapping for testing.
    """
    product_stock = {
        "Laptop": 15,
        "Mouse": 0,
        "Keyboard": 8,
    }

    default_stock = defaultdict(int)
    default_stock.update(product_stock)
    return {
        "get_headphones": product_stock.get("Headphones", 0),
        "defaultdict_headphones": default_stock["Headphones"],
    }


def run() -> None:
    """
    Runs the dictionary key protection example.
    """
    product_stock = {
        "Laptop": 15,
        "Mouse": 0,
        "Keyboard": 8,
    }
    print("\n--- Dictionary Key Protection ---")
    missing_key_strategy_demo()
    print(f"  Stock map: {product_stock}")

    print("  Lookup with get() to avoid KeyError:")
    print(f"    Headphones: {product_stock.get('Headphones', 0)} units")

    print("  Building a defaultdict for automatic defaults:")
    default_stock = defaultdict(int)
    default_stock.update(product_stock)
    print(f"    Headphones: {default_stock['Headphones']} units")


if __name__ == "__main__":
    run()
