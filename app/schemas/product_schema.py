"""
product_schema.py

Pydantic schemas for Product APIs.

These models are responsible for:
1. Validating incoming request data.
2. Defining API response structure.

They DO NOT contain business logic.
"""

from pydantic import BaseModel, Field, ConfigDict


class ProductBase(BaseModel):
    """
    Common fields shared across multiple Product schemas.
    """

    name: str = Field(
        ...,
        min_length=2,
        max_length=100,
        description="Product name"
    )

    price: float = Field(
        ...,
        gt=0,
        description="Product price"
    )

    stock: int = Field(
        ...,
        ge=0,
        description="Available stock"
    )

    category: str = Field(
        ...,
        min_length=2,
        max_length=50,
        description="Product category"
    )


class ProductCreate(ProductBase):
    """
    Request schema used while creating a product.

    Inherits all fields from ProductBase.
    """
    pass


class ProductUpdate(ProductBase):
    """
    Request schema used while updating a product.
    """
    pass


class ProductResponse(ProductBase):
    """
    Response schema returned to the client.
    """

    id: str

    model_config = ConfigDict(
        from_attributes=True
    )