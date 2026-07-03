"""
for_loops.py

Topic:
    - Iterating over sequences (lists, tuples, strings)
    - Iterating over ranges
    - Iterating with enumerate()
    - Iterating with zip()
    - Nested loops

Real World Application:
    Inventory Management System - Processing product data, generating reports

Run:
    python for_loops.py
"""

# Sample inventory data
INVENTORY = {
    "Laptop": {"quantity": 15, "price": 85000},
    "Mouse": {"quantity": 120, "price": 1500},
    "Keyboard": {"quantity": 75, "price": 3500},
    "Monitor": {"quantity": 25, "price": 25000},
    "Headphones": {"quantity": 45, "price": 5000},
}


def iterate_over_list() -> None:
    """
    Demonstrates basic iteration over a list.
    """
    print("\n--- Iterating Over List (Simple Inventory Listing) ---")
    
    products = ["Laptop", "Mouse", "Keyboard", "Monitor", "Headphones"]
    
    for product in products:
        print(f"  Product: {product}")


def iterate_over_range() -> None:
    """
    Demonstrates iterating using range() for numeric operations.
    """
    print("\n--- Iterating Over Range (Processing First 5 Items) ---")
    
    for i in range(5):
        print(f"  Item {i + 1}")


def iterate_with_dictionary() -> None:
    """
    Demonstrates iterating over dictionary items.
    """
    print("\n--- Iterating Over Dictionary (Full Inventory) ---")
    
    for product, details in INVENTORY.items():
        quantity = details["quantity"]
        price = details["price"]
        total_value = quantity * price
        print(f"  {product}: {quantity} units @ ₹{price:,} = ₹{total_value:,}")


def iterate_over_string() -> None:
    """
    Demonstrates iterating over string characters.
    """
    print("\n--- Iterating Over String (Processing Product Code) ---")
    
    product_code = "LP2024"
    
    print(f"  Product Code: {product_code}")
    print("  Characters: ", end="")
    for char in product_code:
        print(f"[{char}] ", end="")
    print()


def iterate_with_enumerate() -> None:
    """
    Demonstrates enumerate() for getting index and value.
    """
    print("\n--- Iterating With Enumerate (Indexed Inventory) ---")
    
    products = list(INVENTORY.keys())
    
    for index, product in enumerate(products, start=1):
        print(f"  {index}. {product}")


def iterate_with_zip() -> None:
    """
    Demonstrates zip() for parallel iteration.
    """
    print("\n--- Iterating With Zip (Matching Products and Prices) ---")
    
    products = ["Laptop", "Mouse", "Keyboard"]
    prices = [85000, 1500, 3500]
    
    for product, price in zip(products, prices):
        print(f"  {product}: ₹{price:,}")


def nested_loops() -> None:
    """
    Demonstrates nested loops for 2D operations.
    Real-world: Creating inventory reports by category and product.
    """
    print("\n--- Nested Loops (Warehouse Organization) ---")
    
    warehouse = {
        "Section_A": ["Laptop", "Monitor"],
        "Section_B": ["Mouse", "Keyboard"],
        "Section_C": ["Headphones"],
    }
    
    for section, products in warehouse.items():
        print(f"  {section}:")
        for product in products:
            print(f"    - {product}")


def generate_inventory_report() -> None:
    """
    Real-world example: Generate a formatted inventory report.
    """
    print("\n--- Inventory Report (Real-World Example) ---")
    print("\n{:<15} {:<10} {:<12} {:<15}".format("Product", "Quantity", "Price (₹)", "Total Value (₹)"))
    print("-" * 52)
    
    total_inventory_value = 0
    
    for product, details in INVENTORY.items():
        quantity = details["quantity"]
        price = details["price"]
        total_value = quantity * price
        total_inventory_value += total_value
        
        print("{:<15} {:<10} {:<12,} {:<15,}".format(product, quantity, price, total_value))
    
    print("-" * 52)
    print("{:<15} {:<10} {:<12} {:<15,}".format("TOTAL", "", "", total_inventory_value))


def run() -> None:
    """
    Runs all for loop examples.
    """
    iterate_over_list()
    iterate_over_range()
    iterate_with_dictionary()
    iterate_over_string()
    iterate_with_enumerate()
    iterate_with_zip()
    nested_loops()
    generate_inventory_report()


if __name__ == "__main__":
    run()
