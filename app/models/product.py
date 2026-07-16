"""
product.py

Represents a product in our e-commerce application.
"""

from app.models.common import Common


class Product(Common):
    """
    Product model.

    Inherits common fields like:
    - id
    - created_at
    - updated_at
    """

    # Class Variable
    # Shared by all Product objects.
    total_products = 0

    def __init__(
        self,
        name: str,
        price: float,
        stock: int,
        category: str
    ):
        # Call the constructor of the parent class.
        super().__init__()

        # Instance variables
        self.name = name
        self.price = price
        self.category = category

        # Private attribute.
        # Access should happen through the property below.
        self._stock = stock

        # Increment class variable whenever a Product is created.
        Product.total_products += 1

    # ----------------------------
    # Property
    # ----------------------------

    @property
    def stock(self):
        """
        Getter for stock.

        Allows:
            product.stock
        instead of
            product._stock
        """
        return self._stock

    @stock.setter
    def stock(self, value: int):
        """
        Setter for stock.

        Prevents invalid stock values.
        """

        if value < 0:
            raise ValueError("Stock cannot be negative.")

        self._stock = value
        self.touch()


    def reduce_stock(self, quantity: int):
        """
        Reduce product stock after a purchase.
        """

        if quantity > self.stock:
            raise ValueError("Insufficient stock.")

        self.stock -= quantity

    def add_stock(self, quantity: int):
        """
        Increase available stock.
        """

        if quantity <= 0:
            raise ValueError("Quantity should be greater than zero.")

        self.stock += quantity


    @classmethod
    def get_total_products(cls):
        """
        Returns the number of Product objects created.
        """

        return cls.total_products


    @staticmethod
    def is_valid_price(price: float):
        """
        Utility method.

        Doesn't need object data.
        Doesn't need class data.
        """

        return price > 0


    def __str__(self):
        return (
            f"Product("
            f"name='{self.name}', "
            f"price={self.price}, "
            f"stock={self.stock})"
        )