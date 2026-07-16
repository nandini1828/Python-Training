"""
common.py

Base model used by every entity in our application.

This class contains fields that are common across all models.
Other models will inherit from this class.
"""

from uuid import uuid4
from datetime import datetime


class Common:
    """
    Parent class for all application models.
    """

    def __init__(self):
        # Every object gets a unique ID.
        self.id = str(uuid4())

        # Creation time never changes.
        self.created_at = datetime.now()

        # Updated whenever the object is modified.
        self.updated_at = datetime.now()

    def touch(self):
        """
        Updates the 'updated_at' timestamp.

        We'll call this whenever an object is modified.
        """
        self.updated_at = datetime.now()

    def __str__(self):
        """
        Human-readable representation.

        print(object) will call this automatically.
        """
        return f"{self.__class__.__name__}(id={self.id})"