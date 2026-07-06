from collections import defaultdict


def safe_lookup(inventory):

    print("\nQuantity")

    print(inventory.get("Laptop",0))

    print(inventory.get("Projector",0))


def sales_counter():

    print("\nSales Counter")

    sales = defaultdict(int)

    sales["Laptop"] += 1
    sales["Laptop"] += 1
    sales["Mouse"] += 1

    print(dict(sales))