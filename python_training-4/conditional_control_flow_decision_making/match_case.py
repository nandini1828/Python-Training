def display_status(order):

    status = order.order_status

    if status == "PLACED":
        return "Order Placed"

    elif status == "PREPARING":
        return "Restaurant is preparing your food."

    elif status == "OUT_FOR_DELIVERY":
        return "Delivery partner is on the way."

    elif status == "DELIVERED":
        return "Order Delivered."

    else:
        return "Unknown Status"