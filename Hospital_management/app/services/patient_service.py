"""Patient service layer."""

from app.data import patients
from app.models.patient import Patient
from app.utils import get_next_id, validate_age


def add_patient(name: str, age: int, gender: str, disease: str):
    if not validate_age(age):
        return {"message": "Invalid age"}

    patient_id = get_next_id(patients)
    patient = Patient(
        patient_id=patient_id,
        name=name,
        age=age,
        gender=gender,
        disease=disease,
    )
    patients[patient_id] = patient
    return {"message": "Patient added successfully", "patient": patient}


def get_all_patients():
    return list(patients.values())


def get_patient(patient_id: int):
    return patients.get(patient_id)


def delete_patient(patient_id: int):
    if patient_id not in patients:
        return {"message": "Patient not found"}
    deleted_patient = patients.pop(patient_id)
    return {"message": "Patient deleted successfully", "patient": deleted_patient}


def search_patient(name: str):
    return [
        patient
        for patient in patients.values()
        if name.lower() in patient.name.lower()
    ]
