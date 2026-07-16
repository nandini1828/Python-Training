from fastapi import APIRouter, HTTPException

from app.services.order_service import OrderService
from app.utils.exceptions import CartEmpty, OrderNotFound

router = APIRouter(
    prefix="/orders",
    tags=["Orders"]
)


@router.post("/{customer_id}")
async def place_order(customer_id: int):

    try:
        return await OrderService.place_order(customer_id)

    except CartEmpty as error:
        raise HTTPException(
            status_code=400,
            detail=str(error)
        )


@router.get("/")
def get_orders():
    return OrderService.get_all_orders()


@router.get("/{order_id}")
def get_order(order_id: int):

    try:
        return OrderService.get_order(order_id)

    except OrderNotFound as error:
        raise HTTPException(
            status_code=404,
            detail=str(error)
        )


@router.put("/{order_id}/cancel")
def cancel_order(order_id: int):

    try:
        return OrderService.cancel_order(order_id)

    except OrderNotFound as error:
        raise HTTPException(
            status_code=404,
            detail=str(error)
        )