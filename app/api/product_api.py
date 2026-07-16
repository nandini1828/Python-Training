"""
product_api.py

API endpoints related to Product operations.
"""

from fastapi import (
    APIRouter,
    HTTPException,
    Query,
    status,
)

from app.schemas.product_schema import (
    ProductCreate,
    ProductUpdate,
    ProductResponse,
)

from app.services.product_service import product_service
from app.utils.exceptions import EcommerceException


router = APIRouter(
    prefix="/products",
    tags=["Products"],
)


@router.post(
    "/",
    response_model=ProductResponse,
    status_code=status.HTTP_201_CREATED,
)
async def create_product(
    product: ProductCreate,
):
    """
    Create a new product.
    """

    try:
        return product_service.create_product(
            name=product.name,
            price=product.price,
            stock_quantity=product.stock,
            category=product.category,
        )

    except EcommerceException as error:
        raise HTTPException(
            status_code=400,
            detail=str(error),
        )


@router.get(
    "/",
    response_model=list[ProductResponse],
)
async def get_all_products(
    category: str | None = Query(
        default=None,
        description="Filter products by category",
    ),
):
    """
    Return all products.

    If category is provided,
    products are filtered by category.
    """

    products = product_service.get_all_products()

    if category:

        products = [
            product
            for product in products
            if product.category.lower() == category.lower()
        ]

    return products


@router.get(
    "/{product_id}",
    response_model=ProductResponse,
)
async def get_product(
    product_id: str,
):
    """
    Return a product by ID.
    """

    try:
        return product_service.get_product_by_id(product_id)

    except EcommerceException as error:
        raise HTTPException(
            status_code=404,
            detail=str(error),
        )


@router.put(
    "/{product_id}",
    response_model=ProductResponse,
)
async def update_product(
    product_id: str,
    product: ProductUpdate,
):
    """
    Update an existing product.
    """

    try:
        return product_service.update_product(
            product_id=product_id,
            name=product.name,
            price=product.price,
            stock_quantity=product.stock,
            category=product.category,
        )

    except EcommerceException as error:
        raise HTTPException(
            status_code=400,
            detail=str(error),
        )


@router.delete(
    "/{product_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete_product(
    product_id: str,
):
    """
    Delete a product.
    """

    try:
        product_service.delete_product(product_id)

    except EcommerceException as error:
        raise HTTPException(
            status_code=404,
            detail=str(error),
        )