"""
validators.py

Reusable validation functions used throughout the application.
"""

import re

from app.utils.exceptions import (
    InvalidPriceError,
    InvalidStockError,
)


def validate_price(price: float) -> None:
    """
    Ensures the product price is valid.
    """

    if price <= 0:
        raise InvalidPriceError()


def validate_stock(stock: int) -> None:
    """
    Ensures stock is not negative.
    """

    if stock < 0:
        raise InvalidStockError()


def validate_name(name: str) -> None:
    """
    Product/User names cannot be empty.
    """

    if not name.strip():
        raise ValueError("Name cannot be empty.")


def validate_email(email: str) -> None:
    """
    Basic email validation.

    Note:
    This is sufficient for our learning project.
    In production, dedicated libraries are usually preferred.
    """

    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"

    if not re.fullmatch(pattern, email):
        raise ValueError("Invalid email address.")