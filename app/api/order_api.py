"""
order_api.py

API endpoints related to Order operations.
"""

from fastapi import (
    APIRouter,
    HTTPException,
    status,
)

from app.schemas.order_schema import (
    PlaceOrderRequest,
    UpdateOrderStatus,
    OrderResponse,
)

from app.services.order_service import order_service
from app.utils.exceptions import EcommerceException


router = APIRouter(
    prefix="/orders",
    tags=["Orders"],
)


@router.post(
    "/place",
    response_model=OrderResponse,
    status_code=status.HTTP_201_CREATED,
)
async def place_order(
    request: PlaceOrderRequest,
):
    """
    Place an order from a user's cart.
    """

    try:
        return order_service.place_order(
            user_id=request.user_id,
        )

    except EcommerceException as error:
        raise HTTPException(
            status_code=400,
            detail=str(error),
        )


@router.get(
    "/",
    response_model=list[OrderResponse],
)
async def get_all_orders():
    """
    Return all orders.
    """

    return order_service.get_all_orders()


@router.get(
    "/{order_id}",
    response_model=OrderResponse,
)
async def get_order(
    order_id: str,
):
    """
    Return an order by ID.
    """

    try:
        return order_service.get_order_by_id(order_id)

    except EcommerceException as error:
        raise HTTPException(
            status_code=404,
            detail=str(error),
        )


@router.put(
    "/{order_id}/status",
    response_model=OrderResponse,
)
async def update_order_status(
    order_id: str,
    request: UpdateOrderStatus,
):
    """
    Update the status of an order.
    """

    try:
        return order_service.update_status(
            order_id=order_id,
            status=request.status,
        )

    except EcommerceException as error:
        raise HTTPException(
            status_code=400,
            detail=str(error),
        )


@router.delete(
    "/{order_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete_order(
    order_id: str,
):
    """
    Delete an order.
    """

    try:
        order_service.delete_order(order_id)

    except EcommerceException as error:
        raise HTTPException(
            status_code=404,
            detail=str(error),
        )