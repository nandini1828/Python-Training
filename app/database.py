"""
database.py

Temporary in-memory storage.

Later, this file can be replaced with a real database
without changing the API layer.
"""

from app.models.product import Product
from app.models.user import User
from app.models.cart import Cart
from app.models.order import Order


# Key -> Product ID
# Value -> Product object
products: dict[str, Product] = {}

# Key -> User ID
# Value -> User object
users: dict[str, User] = {}

# Key -> User ID
# Value -> Cart object
carts: dict[str, Cart] = {}

# Key -> Order ID
# Value -> Order object
orders: dict[str, Order] = {}