def validate_login(order):

    if not order.logged_in:
        return "Please log in."

    elif len(order.cart) == 0:
        return "Cart is empty."

    else:
        return "Login successful."