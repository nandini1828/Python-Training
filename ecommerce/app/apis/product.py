from fastapi import APIRouter, HTTPException

from app.models.request_models import ProductRequest
from app.services.product_service import ProductService
from app.utils.exceptions import ProductNotFound

router = APIRouter(
    prefix="/products",
    tags=["Products"]
)


@router.get("/")
def get_products():
    return ProductService.get_all_products()


@router.get("/{product_id}")
def get_product(product_id: int):

    try:
        return ProductService.get_product(product_id)

    except ProductNotFound as error:
        raise HTTPException(
            status_code=404,
            detail=str(error)
        )


@router.post("/")
def add_product(product: ProductRequest):

    return ProductService.add_product(
        name=product.name,
        price=product.price,
        stock=product.stock,
        category=product.category,
        description=product.description
    )


@router.put("/{product_id}")
def update_product(product_id: int, product: ProductRequest):

    try:
        return ProductService.update_product(
            product_id,
            name=product.name,
            price=product.price,
            stock=product.stock,
            category=product.category,
            description=product.description
        )

    except ProductNotFound as error:
        raise HTTPException(
            status_code=404,
            detail=str(error)
        )


@router.delete("/{product_id}")
def delete_product(product_id: int):

    try:
        return ProductService.delete_product(product_id)

    except ProductNotFound as error:
        raise HTTPException(
            status_code=404,
            detail=str(error)
        )