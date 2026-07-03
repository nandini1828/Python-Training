"""
for_else_while_else.py

Topic:
    - for-else: Code block executes if loop completes without break
    - while-else: Code block executes if loop completes without break
    - Understanding the difference from regular if-else

Real World Application:
    Inventory Management System - Search operations, verification checks

Run:
    python for_else_while_else.py
"""


def for_else_basic() -> None:
    """
    Demonstrates for-else clause.
    Real-world: Search inventory and confirm if item was found.
    """
    print("\n--- For-Else Basic (Item Found) ---")
    
    products = ["Mouse", "Keyboard", "Monitor"]
    search_item = "Keyboard"
    
    print(f"  Searching for: {search_item}\n")
    
    for product in products:
        if product == search_item:
            print(f"  ✓ Found: {product}")
            break
    else:
        # This block runs only if the loop completes without break
        print(f"  ✗ {search_item} not found in inventory")


def for_else_not_found() -> None:
    """
    Demonstrates for-else when item is not found.
    Real-world: Item not available in any warehouse section.
    """
    print("\n--- For-Else Not Found ---")
    
    products = ["Mouse", "Keyboard", "Monitor"]
    search_item = "Laptop"
    
    print(f"  Searching for: {search_item}\n")
    
    for product in products:
        print(f"  Checking: {product}")
        if product == search_item:
            print(f"  ✓ Found: {product}")
            break
    else:
        # This block executes because the loop completed without break
        print(f"\n  ✗ {search_item} is NOT available in inventory!")


def for_else_warehouse_search() -> None:
    """
    Demonstrates for-else with nested loops in warehouse search.
    Real-world: Search item across multiple warehouse sections.
    """
    print("\n--- For-Else Warehouse Search (Nested) ---")
    
    warehouse = {
        "Section_A": ["Mouse", "Keyboard"],
        "Section_B": ["Monitor", "Headphones"],
        "Section_C": ["USB Cable"],
    }
    
    search_item = "Monitor"
    print(f"  Searching for {search_item} across warehouse:\n")
    
    for section, products in warehouse.items():
        for product in products:
            if product == search_item:
                print(f"  ✓ Found in {section}: {product}")
                break
        else:
            # Continue to next section if not found
            print(f"  - {section}: Not found")
            continue
        
        # Break outer loop if found
        break
    else:
        # This block executes if item was not found in any section
        print(f"\n  ✗ {search_item} is not available in any warehouse section!")


def while_else_basic() -> None:
    """
    Demonstrates while-else clause.
    Real-world: Keep checking stock until item is available.
    """
    print("\n--- While-Else Basic ---")
    
    stock = 5
    attempt = 0
    
    print(f"  Checking stock status (initial stock: {stock}):\n")
    
    while stock > 0:
        print(f"  Attempt {attempt + 1}: Stock available = {stock}")
        stock -= 1
        attempt += 1
    else:
        # Executes after while loop completes (stock becomes 0)
        print(f"\n  ✓ Processed all {attempt} items successfully!")


def while_else_with_break() -> None:
    """
    Demonstrates while-else where loop breaks (else doesn't execute).
    Real-world: Stock depletion detection.
    """
    print("\n--- While-Else With Break ---")
    
    day = 0
    stock = 100
    critical_threshold = 20
    
    print(f"  Monitoring daily sales:")
    print(f"  - Initial Stock: {stock}")
    print(f"  - Critical Threshold: {critical_threshold}\n")
    
    while True:
        day += 1
        stock -= 15
        print(f"  Day {day}: Stock = {stock}")
        
        if stock < critical_threshold:
            print(f"\n  ⚠ ALERT: Critical stock level reached!")
            print(f"  Action: Initiating emergency reorder...")
            break
    else:
        # This won't execute because we break out of the loop
        print(f"\n  ✓ Stock monitoring completed normally")


def authentication_retry() -> None:
    """
    Demonstrates while-else for authentication retry logic.
    Real-world: PIN entry attempts.
    """
    print("\n--- Authentication Retry (While-Else) ---")
    
    correct_pin = 1234
    attempts = 0
    max_attempts = 3
    
    print(f"  PIN: {correct_pin}")
    print(f"  Maximum attempts: {max_attempts}\n")
    
    while attempts < max_attempts:
        attempts += 1
        entered_pin = 1234 if attempts == 3 else 0000  # Correct PIN on 3rd attempt
        
        print(f"  Attempt {attempts}: Entered PIN = {entered_pin}", end="")
        
        if entered_pin == correct_pin:
            print(" → Correct!")
            break
        else:
            print(" → Incorrect")
    else:
        # Executes if we reach max_attempts without breaking
        print(f"\n  ✗ Maximum attempts exceeded. Account locked!")


def validation_loop_with_else() -> None:
    """
    Demonstrates validation loop with for-else.
    Real-world: Validate all order items before processing.
    """
    print("\n--- Validation Loop (For-Else) ---")
    
    orders = [
        {"id": 1, "amount": 5000, "valid": True},
        {"id": 2, "amount": 10000, "valid": True},
        {"id": 3, "amount": -1000, "valid": False},
    ]
    
    print("  Validating orders:\n")
    
    for order in orders:
        print(f"  Order {order['id']}: Amount = ₹{order['amount']}", end="")
        
        if not order["valid"]:
            print(" → Invalid!")
            break
        else:
            print(" → Valid")
    else:
        # All orders are valid
        print(f"\n  ✓ All orders validated successfully!")


def inventory_verification() -> None:
    """
    Demonstrates for-else for inventory verification.
    Real-world: Check if all products meet minimum stock.
    """
    print("\n--- Inventory Verification (For-Else) ---")
    
    inventory = {
        "Laptop": 15,
        "Mouse": 120,
        "Keyboard": 75,
        "Monitor": 5,
    }
    
    min_stock = 10
    print(f"  Checking inventory (minimum stock: {min_stock} units):\n")
    
    for product, quantity in inventory.items():
        print(f"  {product}: {quantity} units", end="")
        
        if quantity < min_stock:
            print(f" → Low stock!")
            break
        else:
            print(" → OK")
    else:
        # All products have sufficient stock
        print(f"\n  ✓ All products have sufficient stock!")


def comparison_break_vs_else() -> None:
    """
    Demonstrates the key difference between loop ending normally vs with break.
    """
    print("\n--- Comparison: Break vs Normal Completion ---")
    
    print("\n  Scenario 1: Loop with break (else skipped):")
    numbers = [1, 2, 3, 4, 5]
    for num in numbers:
        if num == 3:
            print(f"    Found 3, breaking...")
            break
    else:
        print("    This won't print (loop was broken)")
    
    print("\n  Scenario 2: Loop completes normally (else executes):")
    numbers = [1, 2, 3, 4, 5]
    for num in numbers:
        if num == 10:  # Never true
            print("    This won't execute")
            break
    else:
        print("    Loop completed normally, else block executed!")


def run() -> None:
    """
    Runs all for-else and while-else examples.
    """
    for_else_basic()
    for_else_not_found()
    for_else_warehouse_search()
    while_else_basic()
    while_else_with_break()
    authentication_retry()
    validation_loop_with_else()
    inventory_verification()
    comparison_break_vs_else()


if __name__ == "__main__":
    run()
