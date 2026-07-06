"""
==================================================
Module: Dictionary Utilities
Topic: Python Dictionaries
Author: Sagar

Description:
Demonstrates commonly used Python
dictionary methods.
==================================================
"""


def demonstrate_dictionary_methods():
    """
    Demonstrates dictionary methods.

    Returns:
        None
    """

    print("\n======= DICTIONARY METHODS =======\n")

    products = {
        "Laptop": 75000,
        "Keyboard": 2500,
        "Monitor": 18000
    }

    print("Original Dictionary:")
    print(products)

    # get()

    print("\nget('Laptop')")
    print(products.get("Laptop"))

    # keys()

    print("\nkeys()")
    print(products.keys())

    # values()

    print("\nvalues()")
    print(products.values())

    # items()

    print("\nitems()")
    print(products.items())

    # update()

    products.update(
        {
            "Mouse": 1200
        }
    )

    print("\nupdate()")
    print(products)

    # pop()

    removed_product = products.pop(
        "Keyboard"
    )

    print("\npop('Keyboard')")
    print("Removed:", removed_product)

    # popitem()

    last_item = products.popitem()

    print("\npopitem()")
    print(last_item)

    # copy()

    backup_products = products.copy()

    print("\ncopy()")
    print(backup_products)

    # clear()

    backup_products.clear()

    print("\nclear()")
    print(backup_products)

    print("\n=================================")