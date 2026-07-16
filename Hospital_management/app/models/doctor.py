"""
doctor.py

This module contains the Doctor class.
A Doctor object stores all the information
related to a doctor.
"""


class Doctor:
    """
    Represents a doctor in the hospital.
    """

    def __init__(
        self,
        doctor_id: int,
        name: str,
        specialization: str,
    ):
        """
        Initialize a Doctor object.
        """

        self.doctor_id = doctor_id
        self.name = name
        self.specialization = specialization

    def __str__(self) -> str:
        """
        Return a readable representation
        of the doctor object.
        """

        return (
            f"Doctor("
            f"ID={self.doctor_id}, "
            f"Name='{self.name}', "
            f"Specialization='{self.specialization}')"
        )