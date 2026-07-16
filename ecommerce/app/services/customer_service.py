from collections import defaultdict

from app.models.customer import Customer
from app.utils.store import Store
from app.utils.exceptions import CustomerNotFound


class CustomerService:

    @staticmethod
    def add_customer(name, email, phone, address=None):

        customer = Customer(
            Store.customer_id,
            name,
            email,
            phone,
            address
        )

        Store.customers[Store.customer_id] = customer

        Store.customer_id += 1

        return customer

    @staticmethod
    def get_customer(customer_id):

        customer = Store.customers.get(customer_id)

        if customer is None:
            raise CustomerNotFound("Customer not found.")

        return customer

    @staticmethod
    def get_all_customers():

        return list(Store.customers.values())

    @staticmethod
    def customers_by_city():

        grouped = defaultdict(list)

        for customer in Store.customers.values():

            city = customer.address if customer.address else "Unknown"

            grouped[city].append(customer)

        return grouped

    @staticmethod
    def update_customer(customer_id, **kwargs):

        customer = CustomerService.get_customer(customer_id)

        for key, value in kwargs.items():

            if hasattr(customer, key):
                setattr(customer, key, value)

        return customer

    @staticmethod
    def delete_customer(customer_id):

        if customer_id not in Store.customers:
            raise CustomerNotFound("Customer not found.")

        return Store.customers.pop(customer_id)