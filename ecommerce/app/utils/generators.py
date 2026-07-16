def available_products(products):

    for product in products:

        if product.stock > 0:
            yield product


def product_names(products):

    yield from [
        product.name
        for product in products
    ]