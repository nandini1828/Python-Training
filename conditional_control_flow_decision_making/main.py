from model import Order

from utils import print_title

from if_elif_else import validate_login
from truthy_falsy import check_cart
from logical_operators import verify_order
from short_circuit import apply_coupon
from ternary_operator import delivery_charge
from match_case import display_status


def main():

    order = Order(
        customer_name="Nandini",
        logged_in=True,
        cart=["Pizza", "Burger"],
        payment_success=True,
        address_available=True,
        premium_member=False,
        coupon={
            "code": "SAVE50",
            "active": True
        },
        order_status="OUT_FOR_DELIVERY"
    )

    print_title("Food Delivery System")

    print(validate_login(order))
    print(check_cart(order))
    print(verify_order(order))
    print(apply_coupon(order))
    print(f"Delivery Charge: ₹{delivery_charge(order)}")
    print(display_status(order))


if __name__ == "__main__":
    main()