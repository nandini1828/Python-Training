"""Patient API routes."""

from fastapi import APIRouter

from app.services.patient_service import (
    add_patient,
    delete_patient,
    get_all_patients,
    get_patient,
    search_patient,
)

router = APIRouter(prefix="/patients", tags=["Patients"])


@router.get("/")
def view_patients():
    return get_all_patients()


@router.get("/{patient_id}")
def view_patient(patient_id: int):
    patient = get_patient(patient_id)
    return patient if patient else {"message": "Patient not found"}


@router.post("/")
def create_patient(name: str, age: int, gender: str, disease: str):
    return add_patient(name=name, age=age, gender=gender, disease=disease)


@router.delete("/{patient_id}")
def remove_patient(patient_id: int):
    return delete_patient(patient_id)


@router.get("/search/{name}")
def search(name: str):
    return search_patient(name)
