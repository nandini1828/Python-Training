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
    print(f"  Stock map: {product_stock}")

    print("  Lookup with get() to avoid KeyError:")
    print(f"    Headphones: {product_stock.get('Headphones', 0)} units")

    print("  Building a defaultdict for automatic defaults:")
    default_stock = defaultdict(int)
    default_stock.update(product_stock)
    print(f"    Headphones: {default_stock['Headphones']} units")


if __name__ == "__main__":
    run()
