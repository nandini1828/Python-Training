"""
exceptions.py

Contains all custom exceptions used by the application.

Using custom exceptions makes the service layer easier to
understand and allows the API layer to return meaningful
HTTP responses.
"""


class EcommerceException(Exception):
    """
    Base exception for the application.

    Every custom exception should inherit from this class.
    """
    pass


class ProductNotFoundError(EcommerceException):
    def __init__(self, product_id: str):
        message = f"Product with ID '{product_id}' was not found."
        super().__init__(message)


class UserNotFoundError(EcommerceException):
    def __init__(self, user_id: str):
        message = f"User with ID '{user_id}' was not found."
        super().__init__(message)


class OrderNotFoundError(EcommerceException):
    def __init__(self, order_id: str):
        message = f"Order with ID '{order_id}' was not found."
        super().__init__(message)


class CartNotFoundError(EcommerceException):
    def __init__(self, user_id: str):
        message = f"Cart for user '{user_id}' was not found."
        super().__init__(message)


class InvalidPriceError(EcommerceException):
    def __init__(self):
        super().__init__("Price must be greater than zero.")


class InvalidStockError(EcommerceException):
    def __init__(self):
        super().__init__("Stock cannot be negative.")


class InsufficientStockError(EcommerceException):
    def __init__(self):
        super().__init__("Insufficient stock available.")