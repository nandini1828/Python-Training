"""
main.py

Entry point for the Iteration Helpers project.

This script provides an interactive menu to explore Python iteration utilities
through a real-world order and inventory example.

Run:
    python main.py
"""

import iteration_helpers


def display_menu() -> None:
    """Displays the available topics."""
    print("\n" + "=" * 60)
    print("       PYTHON ITERATION HELPERS PLAYGROUND")
    print("=" * 60)
    print("1. range()")
    print("2. enumerate()")
    print("3. zip() / zip_longest()")
    print("4. reversed()")
    print("5. sorted()")
    print("6. any() / all()")
    print("7. Run All Examples")
    print("0. Exit")
    print("=" * 60)


def run_choice(choice: str) -> bool:
    """
    Executes the selected module.

    Args:
        choice: User's menu selection

    Returns:
        False -> Exit Program
        True  -> Continue Program
    """
    products = ["Laptop", "Mouse", "Monitor", "Keyboard"]
    quantities = [10, 0, 5, 8]
    shipments = ["SHP001", "SHP002", "SHP003"]
    orders = [
        {"id": 101, "date": "2025-09-30", "status": "ready"},
        {"id": 102, "date": "2025-10-02", "status": "processing"},
        {"id": 103, "date": "2025-10-01", "status": "ready"},
    ]

    match choice:

        case "1":
            print("\n" + "=" * 60)
            print("RANGE: Generating sequence ranges")
            print("=" * 60)
            iteration_helpers.generate_daily_batches(1, 10, 2)

        case "2":
            print("\n" + "=" * 60)
            print("ENUMERATE: Index and value pairs")
            print("=" * 60)
            iteration_helpers.index_inventory_items(products)

        case "3":
            print("\n" + "=" * 60)
            print("ZIP / ZIP_LONGEST: Parallel iteration")
            print("=" * 60)
            iteration_helpers.match_order_quantities(products, quantities)
            iteration_helpers.match_order_quantities_full(products, quantities)

        case "4":
            print("\n" + "=" * 60)
            print("REVERSED: Loop backwards without mutating")
            print("=" * 60)
            iteration_helpers.audit_recent_shipments(shipments)

        case "5":
            print("\n" + "=" * 60)
            print("SORTED: Sorted iteration with custom keys")
            print("=" * 60)
            iteration_helpers.sort_products_by_price([
                {"name": "Laptop", "price": 85000},
                {"name": "Keyboard", "price": 3500},
                {"name": "Monitor", "price": 25000},
            ])
            iteration_helpers.sort_orders_by_date(orders)

        case "6":
            print("\n" + "=" * 60)
            print("ANY / ALL: Iterable condition checks")
            print("=" * 60)
            iteration_helpers.any_low_stock([
                {"name": "Laptop", "stock": 15},
                {"name": "Mouse", "stock": 3},
                {"name": "Keyboard", "stock": 8},
            ], threshold=5)
            iteration_helpers.all_orders_ready(orders)

        case "7":
            print("\n" + "=" * 60)
            print("RUNNING ALL ITERATION HELPERS")
            print("=" * 60)
            iteration_helpers.run()

        case "0":
            print("\nThanks for learning Python iteration helpers! Goodbye! 👋\n")
            return False

        case _:
            print("\n❌ Invalid choice. Please select a valid option.\n")

    return True


def main() -> None:
    """
    Main loop for the interactive menu.
    """
    print("\n" + "=" * 60)
    print("Welcome to Python Iteration Helpers Training!")
    print("=" * 60)
    print("\nThis project demonstrates iteration helper functions through")
    print("a real-world inventory and order management example.")

    while True:
        display_menu()

        choice = input("\nEnter your choice: ").strip()

        if not run_choice(choice):
            break


if __name__ == "__main__":
    main()
