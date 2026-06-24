# Composition

## Concept Overview

This package demonstrates object composition, where a `Customer` contains an `Address` and an `OrderHistory`.

## Why It Exists

Composition enables clean separation of responsibilities and supports enterprise-grade domain modeling.

## Real World Use Cases

- Order management systems
- Billing and invoicing workflows
- Customer account aggregation

## Example Code

```python
from python_datatypes.composition import Customer, Address, Order

customer = Customer(
    customer_id="C-1001",
    name="Avery Smith",
    address=Address(street="100 Innovation Way", city="Boston", postal_code="02118", country="USA"),
)
customer.place_order(Order(order_id="O-001", quantity=4, price_per_unit=29.95))
```

## Expected Output

```python
Customer Avery Smith owes $319.79
```
