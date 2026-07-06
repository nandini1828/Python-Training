"""
iteration_helpers.py

Topic:
    - range(start, stop, step)
    - enumerate()
    - zip()
    - zip_longest()
    - reversed()
    - sorted()
    - any()
    - all()

Real World Application:
    Inventory audit and order validation system

Run:
    python iteration_helpers.py
"""

from itertools import zip_longest
from typing import List, Dict, Any


def generate_daily_batches(start: int, stop: int, step: int = 1) -> None:
    """
    Demonstrates range(start, stop, step) for generating sequential batches.
    """
    print("\n--- Daily Order Batches (range) ---")
    print(f"  Generating batches from {start} to {stop} with step {step}")

    for batch_number in range(start, stop, step):
        print(f"  Batch {batch_number} prepared")


def index_inventory_items(products: List[str]) -> None:
    """
    Demonstrates enumerate() to retrieve index and value side-by-side.
    """
    print("\n--- Inventory Indexing (enumerate) ---")

    for position, product in enumerate(products, start=1):
        print(f"  {position}. {product}")


def match_order_quantities(products: List[str], quantities: List[int]) -> None:
    """
    Demonstrates zip() for iterating over multiple lists in parallel.
    """
    print("\n--- Order Quantity Matching (zip) ---")

    for product, quantity in zip(products, quantities):
        print(f"  {product}: {quantity} units")


def match_order_quantities_full(products: List[str], quantities: List[int]) -> None:
    """
    Demonstrates zip_longest() to handle unequal list lengths.
    """
    print("\n--- Order Quantity Matching (zip_longest) ---")

    for product, quantity in zip_longest(products, quantities, fillvalue=0):
        print(f"  {product}: {quantity} units")


def audit_recent_shipments(shipments: List[str]) -> None:
    """
    Demonstrates reversed() to loop backward through a collection.
    """
    print("\n--- Recent Shipment Audit (reversed) ---")

    for shipment in reversed(shipments):
        print(f"  Reviewing shipment: {shipment}")


def sort_products_by_price(products: List[Dict[str, Any]]) -> None:
    """
    Demonstrates sorted() with a custom key.
    """
    print("\n--- Products Sorted by Price (sorted) ---")

    for product in sorted(products, key=lambda item: item["price"]):
        print(f"  {product['name']} - ₹{product['price']:,}")


def sort_orders_by_date(orders: List[Dict[str, Any]]) -> None:
    """
    Demonstrates sorted() with a custom date key.
    """
    print("\n--- Orders Sorted by Date (sorted) ---")

    for order in sorted(orders, key=lambda item: item["date"]):
        print(f"  Order {order['id']} - {order['date']} - {order['status']}")


def any_low_stock(products: List[Dict[str, Any]], threshold: int) -> bool:
    """
    Demonstrates any() to check if any product is below threshold.
    """
    print("\n--- Low Stock Check (any) ---")

    result = any(product["stock"] < threshold for product in products)
    if result:
        print(f"  At least one product has stock below {threshold} units")
    else:
        print(f"  All products have stock at or above {threshold} units")

    return result


def all_orders_ready(orders: List[Dict[str, Any]]) -> bool:
    """
    Demonstrates all() to check if all orders are ready.
    """
    print("\n--- Order Readiness Check (all) ---")

    result = all(order["status"] == "ready" for order in orders)
    if result:
        print("  All orders are ready to ship")
    else:
        print("  Some orders are not ready yet")

    return result


def run() -> None:
    """
    Runs all iteration helper examples.
    """
    daily_products = ["Laptop", "Mouse", "Monitor", "Keyboard"]
    stock_levels = [10, 0, 5, 8]
    orders = [
        {"id": 101, "date": "2025-09-30", "status": "ready"},
        {"id": 102, "date": "2025-10-02", "status": "processing"},
        {"id": 103, "date": "2025-10-01", "status": "ready"},
    ]

    generate_daily_batches(1, 6, 2)
    index_inventory_items(daily_products)
    match_order_quantities(daily_products, stock_levels)
    match_order_quantities_full(daily_products, stock_levels + [12, 7])
    audit_recent_shipments(["SHP001", "SHP002", "SHP003"])
    sort_products_by_price([
        {"name": "Laptop", "price": 85000},
        {"name": "Keyboard", "price": 3500},
        {"name": "Monitor", "price": 25000},
    ])
    sort_orders_by_date(orders)
    any_low_stock([
        {"name": "Laptop", "stock": 15},
        {"name": "Mouse", "stock": 3},
        {"name": "Keyboard", "stock": 8},
    ], threshold=5)
    all_orders_ready(orders)


if __name__ == "__main__":
    run()
