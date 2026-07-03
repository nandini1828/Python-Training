"""
break_continue_pass.py

Topic:
    - break: Exit loop prematurely
    - continue: Skip to next iteration
    - pass: Null statement / placeholder

Real World Application:
    Inventory Management System - Order processing, data filtering

Run:
    python break_continue_pass.py
"""


def break_simple() -> None:
    """
    Demonstrates break statement to exit loop early.
    Real-world: Stop searching when item is found.
    """
    print("\n--- Break Statement (Find Product) ---")
    
    products = ["Mouse", "Keyboard", "Monitor", "Laptop", "Headphones"]
    search_item = "Monitor"
    
    print(f"  Searching for: {search_item}")
    
    for index, product in enumerate(products, start=1):
        print(f"  Checking position {index}: {product}", end="")
        
        if product == search_item:
            print(f" → Found at position {index}!")
            break
        else:
            print(" → Not found")


def break_with_condition() -> None:
    """
    Demonstrates break with multiple conditions.
    Real-world: Stop processing orders when budget is exceeded.
    """
    print("\n--- Break With Condition (Order Processing) ---")
    
    items = [
        {"name": "Laptop", "price": 85000},
        {"name": "Mouse", "price": 1500},
        {"name": "Monitor", "price": 25000},
        {"name": "Keyboard", "price": 3500},
    ]
    
    budget = 100000
    total_spent = 0
    
    print(f"  Budget: ₹{budget:,}\n")
    
    for item in items:
        if total_spent + item["price"] > budget:
            print(f"  ✗ Cannot afford {item['name']} (₹{item['price']:,}) - Budget exceeded!")
            print("  Order processing stopped.")
            break
        
        total_spent += item["price"]
        print(f"  ✓ Added {item['name']} (₹{item['price']:,}) - Total: ₹{total_spent:,}")


def continue_simple() -> None:
    """
    Demonstrates continue statement to skip iterations.
    Real-world: Skip products that are out of stock.
    """
    print("\n--- Continue Statement (Skip Out of Stock Items) ---")
    
    products = [
        {"name": "Laptop", "stock": 15},
        {"name": "Mouse", "stock": 0},
        {"name": "Keyboard", "stock": 75},
        {"name": "Monitor", "stock": 0},
        {"name": "Headphones", "stock": 45},
    ]
    
    print("  Processing inventory report:\n")
    
    for product in products:
        if product["stock"] == 0:
            print(f"  ⚠ {product['name']}: Skipped (Out of stock)")
            continue
        
        print(f"  ✓ {product['name']}: {product['stock']} units available")


def continue_with_condition() -> None:
    """
    Demonstrates continue with multiple conditions.
    Real-world: Process only premium products in inventory.
    """
    print("\n--- Continue With Condition (Filter Premium Products) ---")
    
    products = [
        {"name": "Mouse", "price": 1500, "category": "Accessories"},
        {"name": "Laptop", "price": 85000, "category": "Computing"},
        {"name": "Keyboard", "price": 3500, "category": "Accessories"},
        {"name": "Monitor", "price": 25000, "category": "Display"},
        {"name": "Headphones", "price": 5000, "category": "Audio"},
    ]
    
    min_price = 10000
    print(f"  Showing products above ₹{min_price:,}:\n")
    
    for product in products:
        if product["price"] < min_price:
            print(f"  ✗ {product['name']} (₹{product['price']:,}) - Skipped (Below threshold)")
            continue
        
        print(f"  ✓ {product['name']} (₹{product['price']:,}) - {product['category']}")


def pass_as_placeholder() -> None:
    """
    Demonstrates pass statement as placeholder.
    Real-world: Skeleton code for future implementation.
    """
    print("\n--- Pass Statement (Placeholder) ---")
    
    products = ["Laptop", "Mouse", "Keyboard"]
    
    print("  Processing products (feature under development):\n")
    
    for product in products:
        # Future implementation: Validate product
        pass
        
        # Future implementation: Update database
        pass
        
        print(f"  → {product}: Processing...")


def pass_in_conditional() -> None:
    """
    Demonstrates pass in conditional blocks.
    Real-world: Graceful handling of edge cases.
    """
    print("\n--- Pass in Conditional Blocks ---")
    
    orders = [
        {"id": 1, "status": "completed"},
        {"id": 2, "status": "pending"},
        {"id": 3, "status": "cancelled"},
        {"id": 4, "status": "pending"},
    ]
    
    print("  Order processing report:\n")
    
    for order in orders:
        if order["status"] == "pending":
            # Will implement pending order logic later
            pass
        elif order["status"] == "completed":
            print(f"  ✓ Order {order['id']}: Completed - Confirmed")
        elif order["status"] == "cancelled":
            print(f"  ✗ Order {order['id']}: Cancelled - No action needed")


def break_nested_loops() -> None:
    """
    Demonstrates break in nested loops.
    Real-world: Stop searching when item found in warehouse.
    """
    print("\n--- Break in Nested Loops (Warehouse Search) ---")
    
    warehouse = {
        "Section_A": ["Mouse", "Keyboard"],
        "Section_B": ["Laptop", "Monitor"],
        "Section_C": ["Headphones"],
    }
    
    search_item = "Laptop"
    found = False
    
    print(f"  Searching for: {search_item}\n")
    
    for section, products in warehouse.items():
        for product in products:
            print(f"  Checking {section}: {product}", end="")
            
            if product == search_item:
                print(f" → Found!")
                found = True
                break
            else:
                print()
        
        if found:
            break
    
    if not found:
        print(f"  → {search_item} not found in warehouse")


def complex_loop_control() -> None:
    """
    Demonstrates complex use of break and continue together.
    Real-world: Validate and process transaction records.
    """
    print("\n--- Complex Loop Control (Transaction Validation) ---")
    
    transactions = [
        {"id": 1, "amount": 50000, "valid": True},
        {"id": 2, "amount": -5000, "valid": False},
        {"id": 3, "amount": 10000, "valid": True},
        {"id": 4, "amount": 0, "valid": False},
        {"id": 5, "amount": 25000, "valid": True},
    ]
    
    print("  Processing transactions:\n")
    total_processed = 0
    
    for trans in transactions:
        # Skip invalid transactions
        if not trans["valid"]:
            print(f"  ✗ Transaction {trans['id']}: Skipped (Invalid)")
            continue
        
        # Stop processing if suspicious pattern detected
        if trans["amount"] > 100000:
            print(f"  ⚠ Transaction {trans['id']}: Stopped (Amount too high - Manual review needed)")
            break
        
        total_processed += trans["amount"]
        print(f"  ✓ Transaction {trans['id']}: ₹{trans['amount']:,} processed")
    
    print(f"\n  Total Processed: ₹{total_processed:,}")


def run() -> None:
    """
    Runs all break, continue, and pass examples.
    """
    break_simple()
    break_with_condition()
    continue_simple()
    continue_with_condition()
    pass_as_placeholder()
    pass_in_conditional()
    break_nested_loops()
    complex_loop_control()


if __name__ == "__main__":
    run()
