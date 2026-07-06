class Order:

    def __init__(
        self,
        customer_name,
        logged_in,
        cart,
        payment_success,
        address_available,
        premium_member,
        coupon,
        order_status
    ):
        self.customer_name = customer_name
        self.logged_in = logged_in
        self.cart = cart
        self.payment_success = payment_success
        self.address_available = address_available
        self.premium_member = premium_member
        self.coupon = coupon
        self.order_status = order_status