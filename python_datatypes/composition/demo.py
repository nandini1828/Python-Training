from .composition_utils import Address, Customer, Order


def run_composition_demo() -> None:
    address = Address(street="100 Innovation Way", city="Boston", postal_code="02118", country="USA")
    customer = Customer(customer_id="C-1001", name="Avery Smith", address=address)

    customer.place_order(Order(order_id="O-001", quantity=4, price_per_unit=29.95))
    customer.place_order(Order(order_id="O-002", quantity=1, price_per_unit=199.99))

    print(customer.billing_summary())
    print("Address:", customer.address)
    print("Order history total:", customer.order_history.total_revenue())
