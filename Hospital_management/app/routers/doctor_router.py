"""
doctor_router.py

This module contains all the API endpoints
related to doctors.
"""

from fastapi import APIRouter

from app.services.doctor_service import (
    add_doctor,
    get_all_doctors,
    get_doctor,
    delete_doctor,
    search_doctor,
    sort_doctors,
)

# Create a router object
router = APIRouter(
    prefix="/doctors",
    tags=["Doctors"],
)


@router.get("/")
def view_doctors():
    """
    Get all doctors.
    """
    return get_all_doctors()


@router.get("/{doctor_id}")
def view_doctor(doctor_id: int):
    """
    Get a doctor using doctor ID.
    """

    doctor = get_doctor(doctor_id)

    if doctor:
        return doctor

    return {"message": "Doctor not found"}


@router.post("/")
def create_doctor(
    name: str,
    specialization: str,
):
    """
    Add a new doctor.
    """

    return add_doctor(
        name=name,
        specialization=specialization,
    )


@router.delete("/{doctor_id}")
def remove_doctor(doctor_id: int):
    """
    Delete a doctor.
    """

    return delete_doctor(doctor_id)


@router.get("/search/{specialization}")
def search(specialization: str):
    """
    Search doctors by specialization.
    """

    return search_doctor(specialization)


@router.get("/sorted/list")
def sorted_doctors():
    """
    Return doctors sorted by name.
    """

    return sort_doctors()