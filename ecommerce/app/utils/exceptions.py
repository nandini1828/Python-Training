"""
Custom Exceptions for E-Commerce Application
"""


class ProductNotFound(Exception):
    """Raised when a product is not found."""
    pass


class CustomerNotFound(Exception):
    """Raised when a customer is not found."""
    pass


class CartEmpty(Exception):
    """Raised when cart has no items."""
    pass


class OutOfStock(Exception):
    """Raised when product stock is not available."""
    pass


class OrderNotFound(Exception):
    """Raised when an order is not found."""
    pass