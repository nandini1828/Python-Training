def verify_order(order):

    if order.payment_success and order.address_available:
        return "Order can be processed."

    return "Payment or address validation failed."