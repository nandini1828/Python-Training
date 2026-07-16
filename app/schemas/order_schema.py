"""
order_schema.py

Pydantic schemas for Order APIs.
"""

from pydantic import BaseModel, ConfigDict

from app.models.order import OrderStatus
from app.schemas.product_schema import ProductResponse
from app.schemas.user_schema import UserResponse


class PlaceOrderRequest(BaseModel):
    """
    Request schema for placing an order.
    """

    user_id: str


class UpdateOrderStatus(BaseModel):
    """
    Request schema for updating an order status.
    """

    status: OrderStatus


class OrderResponse(BaseModel):
    """
    Response schema returned for order operations.
    """

    id: str

    user: UserResponse

    products: list[ProductResponse]

    status: OrderStatus

    model_config = ConfigDict(
        from_attributes=True
    )