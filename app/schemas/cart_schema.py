"""
cart_schema.py

Pydantic schemas for Cart APIs.
"""

from pydantic import BaseModel, ConfigDict

from app.schemas.product_schema import ProductResponse
from app.schemas.user_schema import UserResponse


class CartCreate(BaseModel):
    """
    Request schema for creating a cart.

    """

    user_id: str


class AddProductToCart(BaseModel):
    """
    Request schema for adding a product to a cart.
    """

    product_id: str


class CartResponse(BaseModel):
    """
    Response schema returned for cart operations.
    """

    user: UserResponse

    products: list[ProductResponse]

    total_items: int

    total_price: float

    model_config = ConfigDict(
        from_attributes=True
    )