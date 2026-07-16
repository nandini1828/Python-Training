"""
test_patient.py

Basic test cases for the Patient Service.
"""

from app.data import patients
from app.services.patient_service import (
    add_patient,
    get_patient,
    delete_patient,
)


def setup_function():
    """
    Clear the patient dictionary before each test.
    """
    patients.clear()


def test_add_patient():
    """
    Test adding a patient.
    """

    result = add_patient(
        name="Rahul",
        age=24,
        gender="Male",
        disease="Fever",
    )

    assert result["message"] == "Patient added successfully"
    assert len(patients) == 1


def test_get_patient():
    """
    Test getting a patient by ID.
    """

    add_patient(
        name="Anjali",
        age=22,
        gender="Female",
        disease="Cold",
    )

    patient = get_patient(1)

    assert patient.name == "Anjali"


def test_delete_patient():
    """
    Test deleting a patient.
    """

    add_patient(
        name="Kiran",
        age=30,
        gender="Male",
        disease="Cough",
    )

    result = delete_patient(1)

    assert result["message"] == "Patient deleted successfully"
    assert len(patients) == 0