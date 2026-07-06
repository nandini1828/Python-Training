def apply_coupon(order):

    if order.coupon and order.coupon.get("active"):
        return f"Coupon Applied: {order.coupon['code']}"

    return "No active coupon."