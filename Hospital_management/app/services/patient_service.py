"""
patient_service.py

This module contains all the business logic
related to patients.
"""

from app.data import patients
from app.models.patient import Patient
from app.utils import get_next_id, validate_age


def add_patient(
    name: str,
    age: int,
    gender: str,
    disease: str,
):
    """
    Add a new patient.
    """

    # Validate age before creating a patient
    if not validate_age(age):
        return {"message": "Invalid age"}

    # Generate a unique patient id
    patient_id = get_next_id(patients)

    # Create a Patient object
    patient = Patient(
        patient_id=patient_id,
        name=name,
        age=age,
        gender=gender,
        disease=disease,
    )

    # Store the object in dictionary
    patients[patient_id] = patient

    return {
        "message": "Patient added successfully",
        "patient": patient,
    }


def get_all_patients():
    """
    Return all patients.
    """

    return list(patients.values())


def get_patient(patient_id: int):
    """
    Return a patient using patient id.
    """

    return patients.get(patient_id)


def delete_patient(patient_id: int):
    """
    Delete a patient from the dictionary.
    """

    if patient_id not in patients:
        return {"message": "Patient not found"}

    deleted_patient = patients.pop(patient_id)

    return {
        "message": "Patient deleted successfully",
        "patient": deleted_patient,
    }


def search_patient(name: str):
    """
    Search patient by name.

    Demonstrates list comprehension.
    """

    return [
        patient
        for patient in patients.values()
        if name.lower() in patient.name.lower()
    ]


def display_patients():
    """
    Display all patients using enumerate().

    This function demonstrates enumerate().
    """

    for index, patient in enumerate(patients.values(), start=1):
        print(f"{index}. {patient}")