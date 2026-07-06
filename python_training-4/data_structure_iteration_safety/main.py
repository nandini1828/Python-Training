from model import Product

from utils import print_title

from lists_iteration import display_products, slicing_demo
from list_modification_trap import remove_expired_products
from dictionary_iteration import display_inventory
from dictionary_safety import safe_lookup, sales_counter
from set_iteration import display_categories


def main():

    products = [

        Product(101, "Laptop", "Electronics", 15, False),
        Product(102, "Mouse", "Electronics", 40, False),
        Product(103, "Milk", "Groceries", 10, True),
        Product(104, "Keyboard", "Electronics", 25, False),
        Product(105, "Bread", "Groceries", 8, True)

    ]

    inventory = {

        "Laptop":15,
        "Mouse":40,
        "Keyboard":25

    }

    print_title("Warehouse Inventory Management")

    display_products(products)

    slicing_demo(products)

    products = remove_expired_products(products)

    display_products(products)

    display_inventory(inventory)

    safe_lookup(inventory)

    sales_counter()

    display_categories(products)


if __name__ == "__main__":

    main()