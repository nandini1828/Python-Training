from collections import namedtuple

Product = namedtuple("Product", ["product_id", "name", "price", "stock"])
products = []


def add_product():
    """Add a new product to the inventory list."""
    try:
        product_id = input("Enter product ID: ").strip()
        name = input("Enter product name: ").strip()
        price = float(input("Enter product price: ").strip())
        stock = int(input("Enter stock quantity: ").strip())

        if not product_id or not name:
            print("Product ID and name cannot be empty.")
            return
        if price < 0:
            print("Price cannot be negative.")
            return
        if stock < 0:
            print("Stock cannot be negative.")
            return

        products.append(Product(product_id, name, price, stock))
        print(f"Added {name} to inventory.")
    except ValueError:
        print("Invalid input. Please enter valid numeric values.")


def display_products():
    """Display all products in a table format."""
    if not products:
        print("No products available.")
        return

    print("\nInventory List")
    print("{:<10} {:<20} {:<10} {:<10}".format("ID", "Name", "Price", "Stock"))
    print("-" * 50)
    for product in products:
        print("{:<10} {:<20} {:<10.2f} {:<10}".format(product.product_id, product.name, product.price, product.stock))


def search_product_by_id():
    """Find a product using its ID."""
    product_id = input("Enter product ID to search: ").strip()
    for product in products:
        if product.product_id == product_id:
            print("Product found:")
            print(f"ID: {product.product_id}, Name: {product.name}, Price: {product.price}, Stock: {product.stock}")
            return
    print("Product not found.")


def show_low_stock_products():
    """Show products with stock less than 5."""
    low_stock = [product for product in products if product.stock < 5]
    if not low_stock:
        print("No low stock products.")
        return

    print("Low stock products:")
    for product in low_stock:
        print(f"- {product.name} (Stock: {product.stock})")


def calculate_total_inventory_value():
    """Calculate the total inventory value using price * stock."""
    total_value = sum(product.price * product.stock for product in products)
    print(f"Total inventory value: {total_value:.2f}")


def main():
    """Run the product inventory menu."""
    while True:
        print("\n=== Product Inventory ===")
        print("1. Add Product")
        print("2. Display Products")
        print("3. Search Product by ID")
        print("4. Show Low Stock Products")
        print("5. Calculate Total Inventory Value")
        print("6. Exit")

        choice = input("Choose an option (1-6): ").strip()

        if choice == "1":
            add_product()
        elif choice == "2":
            display_products()
        elif choice == "3":
            search_product_by_id()
        elif choice == "4":
            show_low_stock_products()
        elif choice == "5":
            calculate_total_inventory_value()
        elif choice == "6":
            print("Exiting Product Inventory. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 6.")


if __name__ == "__main__":
    main()
