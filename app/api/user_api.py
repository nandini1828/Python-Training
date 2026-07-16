"""
user_api.py

API endpoints related to User operations.
"""

from fastapi import (
    APIRouter,
    HTTPException,
    status,
)

from app.schemas.user_schema import (
    UserCreate,
    UserUpdate,
    UserResponse,
)

from app.services.user_service import user_service
from app.utils.exceptions import EcommerceException


router = APIRouter(
    prefix="/users",
    tags=["Users"],
)


@router.post(
    "/",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED,
)
async def create_user(
    user: UserCreate,
):
    """
    Create a new user.
    """

    try:
        return user_service.create_user(
            name=user.name,
            email=user.email,
            age=user.age,
        )

    except EcommerceException as error:
        raise HTTPException(
            status_code=400,
            detail=str(error),
        )


@router.get(
    "/",
    response_model=list[UserResponse],
)
async def get_all_users():
    """
    Return all users.
    """

    return user_service.get_all_users()


@router.get(
    "/{user_id}",
    response_model=UserResponse,
)
async def get_user(
    user_id: str,
):
    """
    Return a user by ID.
    """

    try:
        return user_service.get_user_by_id(user_id)

    except EcommerceException as error:
        raise HTTPException(
            status_code=404,
            detail=str(error),
        )


@router.put(
    "/{user_id}",
    response_model=UserResponse,
)
async def update_user(
    user_id: str,
    user: UserUpdate,
):
    """
    Update an existing user.
    """

    try:
        return user_service.update_user(
            user_id=user_id,
            name=user.name,
            email=user.email,
            age=user.age,
        )

    except EcommerceException as error:
        raise HTTPException(
            status_code=400,
            detail=str(error),
        )


@router.delete(
    "/{user_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete_user(
    user_id: str,
):
    """
    Delete a user.
    """

    try:
        user_service.delete_user(user_id)

    except EcommerceException as error:
        raise HTTPException(
            status_code=404,
            detail=str(error),
        )