from python_datatypes.composition import Address, Customer, Order


def test_composition_order_summary() -> None:
    address = Address(street="100 Main St", city="Boston", postal_code="02118", country="USA")
    customer = Customer(customer_id="C-1001", name="Avery", address=address)
    customer.place_order(Order(order_id="O-001", quantity=2, price_per_unit=30.0))

    assert customer.billing_summary() == "Customer Avery owes $60.00"
    assert customer.address.city == "Boston"
