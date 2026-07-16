"""
order_service.py

Business logic for Order operations.
"""

from app.database import orders

from app.models.order import Order, OrderStatus

from app.utils import storage
from app.utils.exceptions import OrderNotFoundError

from app.services.cart_service import cart_service


class OrderService:
    """
    Handles all order-related business operations.
    """

    def place_order(
        self,
        user_id: str
    ) -> Order:
        """
        Creates an order from the user's cart.
        """

        # Get user's cart
        cart = cart_service.get_cart(user_id)

        # Cart should not be empty
        if not cart.products:
            raise ValueError("Cannot place an order with an empty cart.")

        # Reduce stock for every product
        for product in cart.products:
            product.reduce_stock(1)

        # Create Order
        order = Order(
            user=cart.user,
            products=cart.products.copy()
        )

        # Save Order
        storage.add(
            orders,
            order.id,
            order
        )

        # Clear Cart
        cart.clear_cart()

        return order

    def get_all_orders(self) -> list[Order]:
        """
        Returns every order.
        """

        return storage.get_all(orders)

    def get_order_by_id(
        self,
        order_id: str
    ) -> Order:
        """
        Returns an order by its ID.
        """

        order = storage.get(
            orders,
            order_id
        )

        if order is None:
            raise OrderNotFoundError(order_id)

        return order

    def update_status(
        self,
        order_id: str,
        status: OrderStatus
    ) -> Order:
        """
        Updates the order status.
        """

        order = self.get_order_by_id(order_id)

        order.update_status(status)

        return order

    def delete_order(
        self,
        order_id: str
    ) -> bool:
        """
        Deletes an order.
        """

        self.get_order_by_id(order_id)

        storage.remove(
            orders,
            order_id
        )

        return True


# Shared service instance
order_service = OrderService()