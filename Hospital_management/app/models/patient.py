"""
patient.py

This module contains the Patient class.
A Patient object stores all the information
related to a patient.
"""


class Patient:
    """
    Represents a patient in the hospital.
    """

    def __init__(
        self,
        patient_id: int,
        name: str,
        age: int,
        gender: str,
        disease: str,
    ):
        """
        Initialize a Patient object.
        """

        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.gender = gender
        self.disease = disease

    def __str__(self) -> str:
        """
        Return a readable representation
        of the patient object.
        """

        return (
            f"Patient("
            f"ID={self.patient_id}, "
            f"Name='{self.name}', "
            f"Age={self.age}, "
            f"Gender='{self.gender}', "
            f"Disease='{self.disease}')"
        )