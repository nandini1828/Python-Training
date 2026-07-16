"""
product_service.py

Business logic for Product operations.
"""

from app.database import products
from app.models.product import Product
from app.utils import storage
from app.utils.validators import (
    validate_name,
    validate_price,
    validate_stock
)
from app.utils.exceptions import ProductNotFoundError


class ProductService:
    """
    Handles all product-related business operations.
    """

    def create_product(
        self,
        name: str,
        price: float,
        stock_quantity: int,
        category: str
    ) -> Product:
        """
        Create and store a new product.
        """

       
        validate_name(name)
        validate_price(price)
        validate_stock(stock_quantity)

      
        product = Product(
            name=name,
            price=price,
            stock=stock_quantity,
            category=category
        )

      
        storage.add(
            products,
            product.id,
            product
        )

        return product

    def get_all_products(self) -> list[Product]:
        """
        Returns every available product.
        """

        return storage.get_all(products)

    def get_product_by_id(
        self,
        product_id: str
    ) -> Product:
        """
        Fetch a product using its ID.
        """

        product = storage.get(products, product_id)

        if product is None:
            raise ProductNotFoundError(product_id)

        return product

    def update_product(
        self,
        product_id: str,
        name: str,
        price: float,
        stock_quantity: int,
        category: str
    ) -> Product:
        """
        Updates an existing product.
        """

        validate_name(name)
        validate_price(price)
        validate_stock(stock_quantity)

        product = self.get_product_by_id(product_id)

        product.name = name
        product.price = price

        # Uses the property setter in Product
        product.stock = stock_quantity

        product.category = category

        # Update timestamp
        product.touch()

        return product

    def delete_product(
        self,
        product_id: str
    ) -> bool:
        """
        Deletes a product.
        """

        # Ensures product exists
        self.get_product_by_id(product_id)

        storage.remove(products, product_id)

        return True


# Singleton object
# APIs will import this instance instead of
# creating ProductService() repeatedly.
product_service = ProductService()