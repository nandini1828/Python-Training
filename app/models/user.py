"""
user.py

Represents a user of our e-commerce application.
"""

from app.models.common import Common


class User(Common):
    def __init__(
        self,
        name: str,
        email: str,
        age: int
    ):
        # Initialize common fields (id, timestamps)
        super().__init__()

        self.name = name
        self.email = email
        self._age = age

    @property
    def age(self):
        """
        Read-only access to age.
        Validation is handled by the setter.
        """
        return self._age

    @age.setter
    def age(self, value: int):
        if value < 18:
            raise ValueError("User must be at least 18 years old.")

        self._age = value
        self.touch()

    def update_email(self, new_email: str):
        """
        Updates the user's email.

        Email format validation will be added later
        using our validators utility.
        """
        self.email = new_email
        self.touch()

    def __str__(self):
        return (
            f"User("
            f"name='{self.name}', "
            f"email='{self.email}')"
        )