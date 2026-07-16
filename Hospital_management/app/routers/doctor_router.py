"""Doctor API routes."""

from fastapi import APIRouter

from app.services.doctor_service import (
    add_doctor,
    delete_doctor,
    get_all_doctors,
    get_doctor,
    search_doctor,
    sort_doctors,
)

router = APIRouter(prefix="/doctors", tags=["Doctors"])


@router.get("/")
def view_doctors():
    return get_all_doctors()


@router.get("/{doctor_id}")
def view_doctor(doctor_id: int):
    doctor = get_doctor(doctor_id)
    return doctor if doctor else {"message": "Doctor not found"}


@router.post("/")
def create_doctor(name: str, specialization: str):
    return add_doctor(name=name, specialization=specialization)


@router.delete("/{doctor_id}")
def remove_doctor(doctor_id: int):
    return delete_doctor(doctor_id)


@router.get("/search/{specialization}")
def search(specialization: str):
    return search_doctor(specialization)


@router.get("/sorted/list")
def sorted_doctors():
    return sort_doctors()
