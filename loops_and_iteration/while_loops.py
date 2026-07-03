"""
while_loops.py

Topic:
    - Basic while loops
    - Using while for conditional iteration
    - State-based repetition
    - User input handling with while

Real World Application:
    Inventory Management System - Simulating ATM transactions, user interactions

Run:
    python while_loops.py
"""

import random


def countdown_timer() -> None:
    """
    Demonstrates basic while loop with counter.
    Real-world: Stock level warning timer.
    """
    print("\n--- Countdown Timer (Stock Alert) ---")
    
    count = 5
    while count > 0:
        print(f"  Warning! Low stock alert: {count} seconds...")
        count -= 1
    print("  Alert completed!")


def validate_user_input() -> None:
    """
    Demonstrates while loop with user input validation.
    Real-world: Quantity input validation at checkout.
    """
    print("\n--- Input Validation (Purchase Quantity) ---")
    
    # Simulating user input validation (hardcoded for demo)
    attempts = 0
    max_attempts = 3
    
    # In a real scenario, this would be:
    # while True:
    #     quantity = input("Enter quantity to purchase: ")
    #     if quantity.isdigit() and int(quantity) > 0:
    #         print(f"Valid quantity: {quantity}")
    #         break
    #     attempts += 1
    
    print("  Attempting to enter valid quantity...")
    while attempts < max_attempts:
        print(f"  Attempt {attempts + 1}/{max_attempts}")
        # Simulating invalid input
        quantity = random.randint(-10, 50)
        
        if quantity > 0:
            print(f"  ✓ Valid quantity accepted: {quantity} units")
            break
        else:
            print(f"  ✗ Invalid quantity: {quantity}")
            attempts += 1
    
    if attempts == max_attempts:
        print("  ✗ Maximum attempts exceeded. Transaction cancelled.")


def stock_depletion_simulation() -> None:
    """
    Demonstrates while loop with condition evaluation.
    Real-world: Simulating stock depletion over time.
    """
    print("\n--- Stock Depletion Simulation ---")
    
    initial_stock = 50
    daily_sales = 5
    stock = initial_stock
    day = 0
    
    print(f"  Initial Stock: {initial_stock} units")
    print(f"  Daily Sales: {daily_sales} units\n")
    
    while stock > 0:
        day += 1
        stock -= daily_sales
        remaining = max(0, stock)
        print(f"  Day {day}: Stock remaining = {remaining} units")
    
    print(f"\n  Stock depleted after {day} days!")


def reorder_system_simulation() -> None:
    """
    Demonstrates while loop with multiple conditions.
    Real-world: Automated reorder system when stock is low.
    """
    print("\n--- Automated Reorder System ---")
    
    stock = 15
    reorder_threshold = 20
    reorder_amount = 50
    day = 0
    max_days = 10
    
    print(f"  Initial Stock: {stock} units")
    print(f"  Reorder Threshold: {reorder_threshold} units")
    print(f"  Reorder Amount: {reorder_amount} units\n")
    
    while day < max_days and stock > 0:
        day += 1
        
        # Simulate daily sales
        sales = random.randint(5, 15)
        stock -= sales
        
        print(f"  Day {day}: Sold {sales} units, Stock = {stock} units", end="")
        
        # Check if reorder needed
        if stock < reorder_threshold:
            stock += reorder_amount
            print(f" → Reordered! New stock = {stock} units")
        else:
            print()


def authentication_attempt() -> None:
    """
    Demonstrates while True loop with break condition.
    Real-world: Login system with retry limit.
    """
    print("\n--- Authentication Attempt (PIN Entry) ---")
    
    correct_pin = 1234
    attempts = 0
    max_attempts = 3
    
    print(f"  Maximum attempts: {max_attempts}\n")
    
    while True:
        attempts += 1
        
        # Simulating random PIN entry
        entered_pin = random.randint(1000, 9999)
        print(f"  Attempt {attempts}: Entered PIN = {entered_pin}", end="")
        
        if entered_pin == correct_pin:
            print(" → ✓ Correct!")
            break
        elif attempts >= max_attempts:
            print(" → ✗ Account locked!")
            break
        else:
            print(" → ✗ Incorrect")


def menu_system_simulation() -> None:
    """
    Demonstrates while loop for interactive menu.
    Real-world: ATM menu selection.
    """
    print("\n--- Interactive Menu System ---")
    
    menu_options = {
        1: "Check Balance",
        2: "Withdraw Cash",
        3: "Deposit Money",
        0: "Exit"
    }
    
    print("\n  ATM Menu:")
    for key, value in menu_options.items():
        print(f"    {key}. {value}")
    
    selection = 0
    iterations = 0
    
    while selection != 0 and iterations < 3:  # Limited iterations for demo
        iterations += 1
        # Simulate user selection
        selection = random.randint(0, 3)
        
        if selection == 0:
            print(f"\n  {iterations}. You selected: Exit → Exiting...")
        else:
            print(f"  {iterations}. You selected: {menu_options[selection]}")


def run() -> None:
    """
    Runs all while loop examples.
    """
    countdown_timer()
    validate_user_input()
    stock_depletion_simulation()
    reorder_system_simulation()
    authentication_attempt()
    menu_system_simulation()


if __name__ == "__main__":
    run()
