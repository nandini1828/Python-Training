"""
patient_router.py

This module contains all the API endpoints
related to patients.
"""

from fastapi import APIRouter

from app.services.patient_service import (
    add_patient,
    get_all_patients,
    get_patient,
    delete_patient,
    search_patient,
)

# Create a router object
router = APIRouter(
    prefix="/patients",
    tags=["Patients"],
)


@router.get("/")
def view_patients():
    """
    Get all patients.
    """
    return get_all_patients()


@router.get("/{patient_id}")
def view_patient(patient_id: int):
    """
    Get a patient using patient ID.
    """
    patient = get_patient(patient_id)

    if patient:
        return patient

    return {"message": "Patient not found"}


@router.post("/")
def create_patient(
    name: str,
    age: int,
    gender: str,
    disease: str,
):
    """
    Add a new patient.
    """

    return add_patient(
        name=name,
        age=age,
        gender=gender,
        disease=disease,
    )


@router.delete("/{patient_id}")
def remove_patient(patient_id: int):
    """
    Delete a patient.
    """

    return delete_patient(patient_id)


@router.get("/search/{name}")
def search(name: str):
    """
    Search patients by name.
    """

    return search_patient(name)