"""
cart_api.py

API endpoints related to Cart operations.
"""

from fastapi import (
    APIRouter,
    HTTPException,
    status,
)

from app.schemas.cart_schema import (
    CartCreate,
    AddProductToCart,
    CartResponse,
)

from app.services.cart_service import cart_service
from app.utils.exceptions import EcommerceException


router = APIRouter(
    prefix="/carts",
    tags=["Carts"],
)


@router.post(
    "/",
    response_model=CartResponse,
    status_code=status.HTTP_201_CREATED,
)
async def create_cart(
    cart: CartCreate,
):
    """
    Create a cart for a user.
    """

    try:
        return cart_service.create_cart(
            user_id=cart.user_id,
        )

    except EcommerceException as error:
        raise HTTPException(
            status_code=400,
            detail=str(error),
        )


@router.get(
    "/{user_id}",
    response_model=CartResponse,
)
async def get_cart(
    user_id: str,
):
    """
    Get a user's cart.
    """

    try:
        return cart_service.get_cart(user_id)

    except EcommerceException as error:
        raise HTTPException(
            status_code=404,
            detail=str(error),
        )


@router.post(
    "/{user_id}/products",
    response_model=CartResponse,
)
async def add_product_to_cart(
    user_id: str,
    product: AddProductToCart,
):
    """
    Add a product to a cart.
    """

    try:
        return cart_service.add_product(
            user_id=user_id,
            product_id=product.product_id,
        )

    except EcommerceException as error:
        raise HTTPException(
            status_code=400,
            detail=str(error),
        )


@router.delete(
    "/{user_id}/products/{product_id}",
    response_model=CartResponse,
)
async def remove_product_from_cart(
    user_id: str,
    product_id: str,
):
    """
    Remove a product from a cart.
    """

    try:
        return cart_service.remove_product(
            user_id=user_id,
            product_id=product_id,
        )

    except EcommerceException as error:
        raise HTTPException(
            status_code=400,
            detail=str(error),
        )


@router.delete(
    "/{user_id}",
    response_model=CartResponse,
)
async def clear_cart(
    user_id: str,
):
    """
    Remove all products from a cart.
    """

    try:
        return cart_service.clear_cart(user_id)

    except EcommerceException as error:
        raise HTTPException(
            status_code=400,
            detail=str(error),
        )