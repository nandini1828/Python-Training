"""
user_service.py

Business logic for User operations.
"""

from app.database import users
from app.models.user import User
from app.utils import storage
from app.utils.validators import (
    validate_name,
    validate_email,
)
from app.utils.exceptions import UserNotFoundError


class UserService:
    """
    Handles all user-related business operations.
    """

    def create_user(
        self,
        name: str,
        email: str,
        age: int
    ) -> User:
        """
        Creates and stores a new user.
        """

       
        validate_name(name)
        validate_email(email)

        user = User(
            name=name,
            email=email,
            age=age
        )

        storage.add(
            users,
            user.id,
            user
        )

        return user

    def get_all_users(self) -> list[User]:
        """
        Returns all users.
        """

        return storage.get_all(users)

    def get_user_by_id(
        self,
        user_id: str
    ) -> User:
        """
        Returns a user by ID.
        """

        user = storage.get(users, user_id)

        if user is None:
            raise UserNotFoundError(user_id)

        return user

    def update_user(
        self,
        user_id: str,
        name: str,
        email: str,
        age: int
    ) -> User:
        """
        Updates an existing user.
        """

        validate_name(name)
        validate_email(email)

        user = self.get_user_by_id(user_id)

        user.name = name
        user.email = email

        # Uses the property setter in User
        user.age = age

        user.touch()

        return user

    def delete_user(
        self,
        user_id: str
    ) -> bool:
        """
        Deletes a user.
        """

        # Ensures the user exists
        self.get_user_by_id(user_id)

        storage.remove(users, user_id)

        return True


# Shared service instance
user_service = UserService()