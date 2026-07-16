"""Doctor service layer."""

from app.data import departments, doctors
from app.models.doctor import Doctor
from app.utils import get_next_id


def add_doctor(name: str, specialization: str):
    doctor_id = get_next_id(doctors)
    doctor = Doctor(
        doctor_id=doctor_id,
        name=name,
        specialization=specialization,
    )
    doctors[doctor_id] = doctor
    departments.add(specialization)
    return {"message": "Doctor added successfully", "doctor": doctor}


def get_all_doctors():
    return list(doctors.values())


def get_doctor(doctor_id: int):
    return doctors.get(doctor_id)


def delete_doctor(doctor_id: int):
    if doctor_id not in doctors:
        return {"message": "Doctor not found"}
    deleted_doctor = doctors.pop(doctor_id)
    return {"message": "Doctor deleted successfully", "doctor": deleted_doctor}


def search_doctor(specialization: str):
    return [
        doctor
        for doctor in doctors.values()
        if specialization.lower() in doctor.specialization.lower()
    ]


def sort_doctors():
    return sorted(doctors.values(), key=lambda doctor: doctor.name.lower())
