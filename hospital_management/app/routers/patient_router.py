"""
Patient Router

REST API endpoints for patient management.
"""

from fastapi import APIRouter, HTTPException, status
from typing import List
from app.models.patient import Patient, PatientUpdate
import app.services.patient_service as patient_service


router = APIRouter(prefix="/patients", tags=["Patients"])


@router.get("", response_model=List[dict])
async def get_all_patients():
    """Get all patients."""
    return patient_service.get_all_patients()


@router.get("/{patient_id}", response_model=dict)
async def get_patient(patient_id: int):
    """Get a specific patient by ID."""
    # Find the patient using the service
    patient = patient_service.find_patient_by_id(patient_id)
    
    # If not found, raise error
    if patient is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Patient with ID {patient_id} not found"
        )
    
    # Return as dictionary
    return patient.to_dict()


@router.get("/search/by-name/{name}", response_model=List[dict])
async def search_patients_by_name(name: str):
    """Search patients by name."""
    return patient_service.find_patients_by_name(name)


@router.get("/search/by-age/{age}", response_model=List[dict])
async def search_patients_by_age(age: int):
    """Search patients by age."""
    return patient_service.find_patients_by_age(age)


@router.post("", response_model=dict, status_code=status.HTTP_201_CREATED)
async def create_patient(patient: Patient):
    """Create a new patient."""
    try:
        # Call service to create patient
        return patient_service.create_patient(
            name=patient.name,
            age=patient.age,
            gender=patient.gender,
            phone=patient.phone
        )
    except ValueError as error:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(error)
        )


@router.put("/{patient_id}", response_model=dict)
async def update_patient(patient_id: int, patient_update: PatientUpdate):
    """Update a patient's information."""
    # Validate ID
    if patient_id <= 0:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Patient ID must be positive"
        )
    
    # Check if patient exists
    patient = patient_service.find_patient_by_id(patient_id)
    if patient is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Patient with ID {patient_id} not found"
        )
    
    try:
        # Call patch service since we want partial update
        return patient_service.patch_patient(
            patient_id=patient_id,
            name=patient_update.name,
            age=patient_update.age,
            gender=patient_update.gender,
            phone=patient_update.phone
        )
    except ValueError as error:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(error)
        )


@router.delete("/{patient_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_patient(patient_id: int):
    """Delete a patient."""
    # Validate ID
    if patient_id <= 0:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Patient ID must be positive"
        )
    
    # Delete the patient
    deleted = patient_service.delete_patient(patient_id)
    
    # If not found, raise error
    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Patient with ID {patient_id} not found"
        )
