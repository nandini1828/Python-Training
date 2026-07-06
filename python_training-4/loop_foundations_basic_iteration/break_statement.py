def inspect_products(products):

    print("\nInspecting Products")

    for product in products:

        if product.damaged:

            print(f"{product.name} is damaged.")

            break

        print(f"{product.name} passed inspection.")