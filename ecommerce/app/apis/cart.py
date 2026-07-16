from fastapi import APIRouter
from fastapi import HTTPException

from app.services.cart_service import CartService
from app.utils.exceptions import CartEmpty
from app.utils.exceptions import ProductNotFound


router = APIRouter(
    prefix="/cart",
    tags=["Cart"]
)


@router.post("/{customer_id}/add/{product_id}")
def add_to_cart(customer_id: int, product_id: int):

    try:
        return CartService.add_to_cart(customer_id, product_id)

    except ProductNotFound as error:
        raise HTTPException(
            status_code=404,
            detail=str(error)
        )


@router.get("/{customer_id}")
def view_cart(customer_id: int):

    return CartService.view_cart(customer_id)


@router.get("/{customer_id}/total")
def calculate_total(customer_id: int):

    try:
        return CartService.calculate_total(customer_id)

    except CartEmpty as error:
        raise HTTPException(
            status_code=400,
            detail=str(error)
        )


@router.delete("/{customer_id}/remove/{product_id}")
def remove_from_cart(customer_id: int, product_id: int):

    return CartService.remove_from_cart(
        customer_id,
        product_id
    )


@router.delete("/{customer_id}/clear")
def clear_cart(customer_id: int):

    return CartService.clear_cart(customer_id)