def remove_expired_products(products):

    print("\nRemoving Expired Products")

    for product in products[:]:

        if product.expired:

            products.remove(product)

    return products