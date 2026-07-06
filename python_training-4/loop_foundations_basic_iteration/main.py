from model import Product

from utils import print_title

from for_loops import display_products
from while_loops import process_deliveries
from break_statement import inspect_products
from continue_statement import ship_products
from pass_statement import future_validation
from loop_else import search_product, complete_deliveries


def main():

    products = [

        Product("Laptop", True, False),
        Product("Mouse", False, False),
        Product("Keyboard", True, False),
        Product("Monitor", True, True),
        Product("Printer", True, False)

    ]

    print_title("Inventory Management System")

    display_products(products)

    process_deliveries(3)

    inspect_products(products)

    ship_products(products)

    future_validation(products)

    search_product(products, "Keyboard")

    search_product(products, "Camera")

    complete_deliveries(3)


if __name__ == "__main__":

    main()