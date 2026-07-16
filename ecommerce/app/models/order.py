from datetime import datetime
from enum import Enum


class OrderStatus(str, Enum):
    PENDING = "Pending"
    COMPLETED = "Completed"
    CANCELLED = "Cancelled"


class Order:

    def __init__(self, order_id, customer_id, items, total):

        self.order_id = order_id
        self.customer_id = customer_id
        self.items = items
        self.total = total
        self.status = OrderStatus.PENDING
        self.created_at = datetime.now()

    def complete_order(self):
        self.status = OrderStatus.COMPLETED

    def cancel_order(self):
        self.status = OrderStatus.CANCELLED

    def __str__(self):
        return f"Order #{self.order_id}"

    def __repr__(self):
        return f"Order({self.order_id})"