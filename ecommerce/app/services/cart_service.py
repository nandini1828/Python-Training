from collections import deque

from app.models.cart import Cart
from app.services.product_service import ProductService
from app.utils.exceptions import CartEmpty
from app.utils.store import Store


recent_products = deque(maxlen=5)


class CartService:

    @staticmethod
    def get_cart(customer_id):

        if customer_id not in Store.carts:
            Store.carts[customer_id] = Cart()

        return Store.carts[customer_id]

    @staticmethod
    def add_to_cart(customer_id, product_id):

        cart = CartService.get_cart(customer_id)

        product = ProductService.get_product(product_id)

        cart.add_item(product)

        recent_products.append(product.name)

        return cart

    @staticmethod
    def remove_from_cart(customer_id, product_id):

        cart = CartService.get_cart(customer_id)

        cart.remove_item(product_id)

        return cart

    @staticmethod
    def clear_cart(customer_id):

        cart = CartService.get_cart(customer_id)

        cart.clear()

        return {"message": "Cart Cleared"}

    @staticmethod
    def calculate_total(customer_id):

        cart = CartService.get_cart(customer_id)

        if len(cart) == 0:
            raise CartEmpty("Cart is empty.")

        return {
            "total": cart.get_total()
        }

    @staticmethod
    def view_cart(customer_id):
        cart = CartService.get_cart(customer_id)
        return {
            "items": [str(item) for item in cart.items],
            "total": cart.get_total()
        }

    @staticmethod
    def recent_items():

        return list(recent_products)