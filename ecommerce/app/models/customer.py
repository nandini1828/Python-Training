from typing import Optional


class Customer:

    total_customers = 0

    def __init__(
        self,
        customer_id: int,
        name: str,
        email: str,
        phone: str,
        address: Optional[str] = None
    ):

        self.customer_id = customer_id
        self.name = name
        self.email = email
        self.phone = phone
        self.address = address

        Customer.total_customers += 1

    @classmethod
    def get_total_customers(cls):
        return cls.total_customers

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"Customer({self.customer_id}, {self.name})"

    def __eq__(self, other):

        if not isinstance(other, Customer):
            return False

        return self.customer_id == other.customer_id