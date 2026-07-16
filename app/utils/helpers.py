"""
helpers.py

Reusable helper functions used across the application.
"""

from datetime import datetime
from uuid import uuid4
from typing import Any


def generate_id() -> str:
    """
    Generates a unique identifier.
    """

    return str(uuid4())


def current_timestamp() -> datetime:
    """
    Returns the current date and time.
    """

    return datetime.now()


def success_response(
    message: str,
    data: Any = None
) -> dict:
    """
    Creates a consistent success response.
    """

    return {
        "success": True,
        "message": message,
        "data": data
    }


def error_response(message: str) -> dict:
    """
    Creates a consistent error response.
    """

    return {
        "success": False,
        "message": message
    }