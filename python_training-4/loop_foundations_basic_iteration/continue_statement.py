def ship_products(products):

    print("\nShipping Products")

    for product in products:

        if not product.available:

            continue

        print(f"Shipping {product.name}")