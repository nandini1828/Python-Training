"""
doctor_service.py

This module contains all the business logic
related to doctors.
"""

from app.data import doctors, departments
from app.models.doctor import Doctor
from app.utils import get_next_id


def add_doctor(
    name: str,
    specialization: str,
):
    """
    Add a new doctor.
    """

    # Generate doctor ID
    doctor_id = get_next_id(doctors)

    # Create Doctor object
    doctor = Doctor(
        doctor_id=doctor_id,
        name=name,
        specialization=specialization,
    )

    # Store object inside dictionary
    doctors[doctor_id] = doctor

    # Add specialization to department set
    departments.add(specialization)

    return {
        "message": "Doctor added successfully",
        "doctor": doctor,
    }


def get_all_doctors():
    """
    Return all doctors.
    """

    return list(doctors.values())


def get_doctor(doctor_id: int):
    """
    Return a doctor by ID.
    """

    return doctors.get(doctor_id)


def delete_doctor(doctor_id: int):
    """
    Delete a doctor.
    """

    if doctor_id not in doctors:
        return {"message": "Doctor not found"}

    deleted_doctor = doctors.pop(doctor_id)

    return {
        "message": "Doctor deleted successfully",
        "doctor": deleted_doctor,
    }


def search_doctor(specialization: str):
    """
    Search doctors by specialization.

    Demonstrates list comprehension.
    """

    return [
        doctor
        for doctor in doctors.values()
        if specialization.lower() in doctor.specialization.lower()
    ]


def display_doctors():
    """
    Display all doctors using enumerate().
    """

    for index, doctor in enumerate(doctors.values(), start=1):
        print(f"{index}. {doctor}")


def sort_doctors():
    """
    Return doctors sorted by name.

    Demonstrates sorted().
    """

    return sorted(
        doctors.values(),
        key=lambda doctor: doctor.name.lower()
    )