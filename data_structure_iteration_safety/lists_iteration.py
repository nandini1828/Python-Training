def display_products(products):

    print("\nProducts")

    for product in products:

        print(product.name)


def slicing_demo(products):

    print("\nFirst Three Products")

    for product in products[:3]:

        print(product.name)