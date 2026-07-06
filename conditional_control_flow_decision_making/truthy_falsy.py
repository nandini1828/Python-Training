def check_cart(order):

    if order.cart:
        return "Items available for checkout."

    return "No items found."