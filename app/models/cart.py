"""
cart.py

Represents a shopping cart.
"""

from app.models.common import Common
from app.models.user import User
from app.models.product import Product


class Cart(Common):
    """
    A Cart belongs to one User and contains multiple Product objects.
    """

    def __init__(self, user: User):
        super().__init__()

        self.user = user

        # Composition:
        # A cart maintains Product objects.
        self.products: list[Product] = []

    def add_product(self, product: Product):
        """
        Adds a product to the cart.
        """
        self.products.append(product)
        self.touch()

    def remove_product(self, product_id: str):
        """
        Removes a product from the cart using its ID.
        """

        for product in self.products:
            if product.id == product_id:
                self.products.remove(product)
                self.touch()
                return True

        return False

    def clear_cart(self):
        """
        Removes all products from the cart.
        """
        self.products.clear()
        self.touch()

    def total_items(self):
        """
        Returns the total number of products.
        """
        return len(self.products)

    def total_price(self):
        """
        Calculates the total cart value.
        """

        total = 0.0

        for product in self.products:
            total += product.price

        return total

    def __str__(self):
        return (
            f"Cart(user={self.user.name}, "
            f"items={self.total_items()}, "
            f"total={self.total_price()})"
        )