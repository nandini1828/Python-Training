"""
user_schema.py

Pydantic schemas for User APIs.

These schemas validate incoming request data
and define API response structures.
"""

from pydantic import (
    BaseModel,
    ConfigDict,
    EmailStr,
    Field,
)


class UserBase(BaseModel):
    """
    Common fields shared across User schemas.
    """

    name: str = Field(
        ...,
        min_length=2,
        max_length=100,
        description="User name"
    )

    email: EmailStr = Field(
        ...,
        description="User email address"
    )

    age: int = Field(
        ...,
        ge=18,
        le=100,
        description="User age"
    )


class UserCreate(UserBase):
    """
    Request schema for creating a user.
    """
    pass


class UserUpdate(UserBase):
    """
    Request schema for updating a user.
    """
    pass


class UserResponse(UserBase):
    """
    Response schema returned to the client.
    """

    id: str

    model_config = ConfigDict(
        from_attributes=True
    )