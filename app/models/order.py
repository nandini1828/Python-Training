"""
order.py

Represents an order placed by a user.
"""

from enum import Enum

from app.models.common import Common
from app.models.user import User
from app.models.product import Product


class OrderStatus(Enum):
    """
    Represents the lifecycle of an order.
    """

    PENDING = "Pending"
    CONFIRMED = "Confirmed"
    SHIPPED = "Shipped"
    DELIVERED = "Delivered"
    CANCELLED = "Cancelled"


class Order(Common):
    """
    Represents a customer's order.
    """

    def __init__(
        self,
        user: User,
        products: list[Product]
    ):
        super().__init__()

        self.user = user
        self.products = products

        # Every newly created order starts in the Pending state.
        self.status = OrderStatus.PENDING

    @property
    def total_amount(self) -> float:
        """
        Calculates the total price of all products
        whenever it is accessed.
        """

        return sum(product.price for product in self.products)

    def update_status(self, status: OrderStatus):
        """
        Updates the order status.
        """

        self.status = status
        self.touch()

    def __str__(self):
        return (
            f"Order("
            f"id={self.id}, "
            f"user={self.user.name}, "
            f"items={len(self.products)}, "
            f"status={self.status.value})"
        )