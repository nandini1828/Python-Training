"""
cart_service.py

Business logic for Cart operations.
"""

from app.database import carts

from app.models.cart import Cart

from app.utils import storage
from app.utils.exceptions import CartNotFoundError

from app.services.user_service import user_service
from app.services.product_service import product_service


class CartService:
    """
    Handles all cart-related business operations.
    """

    def create_cart(
        self,
        user_id: str
    ) -> Cart:
        """
        Creates a cart for a user.
        """

        # Ensure user exists.
        user = user_service.get_user_by_id(user_id)

        cart = Cart(user)

        storage.add(
            carts,
            user.id,
            cart
        )

        return cart

    def get_cart(
        self,
        user_id: str
    ) -> Cart:
        """
        Returns a user's cart.
        """

        cart = storage.get(
            carts,
            user_id
        )

        if cart is None:
            raise CartNotFoundError(user_id)

        return cart

    def add_product(
        self,
        user_id: str,
        product_id: str
    ) -> Cart:
        """
        Adds a product to the user's cart.
        """

        cart = self.get_cart(user_id)

        product = product_service.get_product_by_id(product_id)

        cart.add_product(product)

        return cart

    def remove_product(
        self,
        user_id: str,
        product_id: str
    ) -> Cart:
        """
        Removes a product from the cart.
        """

        cart = self.get_cart(user_id)

        cart.remove_product(product_id)

        return cart

    def clear_cart(
        self,
        user_id: str
    ) -> Cart:
        """
        Removes every product from the cart.
        """

        cart = self.get_cart(user_id)

        cart.clear_cart()

        return cart

    def delete_cart(
        self,
        user_id: str
    ) -> bool:
        """
        Deletes the cart completely.
        """

        self.get_cart(user_id)

        storage.remove(
            carts,
            user_id
        )

        return True


# Shared service instance
cart_service = CartService()