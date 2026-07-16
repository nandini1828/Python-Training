"""
Patient Service

This service contains business logic for managing patients.
Static in-memory data is stored here.

Functions are organized to follow the pattern:
- get_all_*
- find_* 
- create_*
- update_*
- delete_*
"""

from typing import Optional, List
from app.models.patient import Patient, PatientUpdate


# Static data - list of patients stored in memory
patients: List[Patient] = [
    Patient(id=1, name="John Doe", age=30, gender="Male", phone="9876543210"),
    Patient(id=2, name="Jane Smith", age=28, gender="Female", phone="9123456789"),
    Patient(id=3, name="Mike Johnson", age=45, gender="Male", phone="9988776655"),
]


def get_all_patients() -> List[dict]:
    """
    Get all patients.
    
    Returns:
        List of patient dictionaries.
    """
    result = []
    for patient in patients:
        result.append(patient.to_dict())
    return result


def find_patient_by_id(patient_id: int) -> Optional[Patient]:
    """
    Find a patient by their ID.
    
    Args:
        patient_id: The ID to search for.
        
    Returns:
        Patient object if found, None otherwise.
    """
    # Loop through all patients
    for patient in patients:
        # Check if this patient's ID matches
        if patient.id == patient_id:
            return patient
    
    # If not found, return None
    return None


def find_patients_by_name(name: str) -> List[dict]:
    """
    Find patients by name (partial match).
    
    Args:
        name: The name to search for.
        
    Returns:
        List of patient dictionaries.
    """
    result = []
    
    # Loop through all patients
    for patient in patients:
        # Check if name is contained in patient's name
        if name.lower() in patient.name.lower():
            result.append(patient.to_dict())
    
    return result


def find_patients_by_age(age: int) -> List[dict]:
    """
    Find patients by age.
    
    Args:
        age: The age to search for.
        
    Returns:
        List of patient dictionaries.
    """
    result = []
    
    # Loop through all patients
    for patient in patients:
        # Check if age matches
        if patient.age == age:
            result.append(patient.to_dict())
    
    return result


def create_patient(name: str, age: int, gender: str, phone: str) -> dict:
    """
    Create a new patient.
    
    Args:
        name: Patient's name.
        age: Patient's age.
        gender: Patient's gender.
        phone: Patient's phone number.
        
    Returns:
        Created patient as dictionary.
        
    Raises:
        ValueError: If phone number already exists.
    """
    # Check if phone already exists
    for patient in patients:
        if patient.phone == phone:
            raise ValueError("Phone number already exists.")
    
    # Find the highest ID
    highest_id = 0
    for patient in patients:
        if patient.id > highest_id:
            highest_id = patient.id
    
    # Create new patient with new ID
    new_patient = Patient(
        id=highest_id + 1,
        name=name,
        age=age,
        gender=gender,
        phone=phone
    )
    
    # Add to list
    patients.append(new_patient)
    
    # Return as dictionary
    return new_patient.to_dict()


def update_patient(patient_id: int, name: str, age: int, gender: str, phone: str) -> Optional[dict]:
    """
    Update a patient's information.
    
    Args:
        patient_id: ID of patient to update.
        name: New name.
        age: New age.
        gender: New gender.
        phone: New phone number.
        
    Returns:
        Updated patient as dictionary if found, None otherwise.
        
    Raises:
        ValueError: If new phone already exists.
    """
    # Find the patient
    patient = find_patient_by_id(patient_id)
    if patient is None:
        return None
    
    # Check if phone exists (but not for this patient)
    if phone != patient.phone:
        for p in patients:
            if p.phone == phone:
                raise ValueError("Phone number already exists.")
    
    # Get the index
    patient_index = patients.index(patient)
    
    # Create updated patient
    updated_patient = Patient(
        id=patient.id,
        name=name,
        age=age,
        gender=gender,
        phone=phone
    )
    
    # Replace in list
    patients[patient_index] = updated_patient
    
    # Return as dictionary
    return updated_patient.to_dict()


def patch_patient(patient_id: int, name: str = None, age: int = None, gender: str = None, phone: str = None) -> Optional[dict]:
    """
    Partially update a patient's information.
    
    Args:
        patient_id: ID of patient to update.
        name: New name (optional).
        age: New age (optional).
        gender: New gender (optional).
        phone: New phone number (optional).
        
    Returns:
        Updated patient as dictionary if found, None otherwise.
        
    Raises:
        ValueError: If new phone already exists.
    """
    # Find the patient
    patient = find_patient_by_id(patient_id)
    if patient is None:
        return None
    
    # Check if phone exists (but not for this patient)
    if phone and phone != patient.phone:
        for p in patients:
            if p.phone == phone:
                raise ValueError("Phone number already exists.")
    
    # Get the index
    patient_index = patients.index(patient)
    
    # Get existing values, replace only if provided
    new_name = name if name is not None else patient.name
    new_age = age if age is not None else patient.age
    new_gender = gender if gender is not None else patient.gender
    new_phone = phone if phone is not None else patient.phone
    
    # Create updated patient
    updated_patient = Patient(
        id=patient.id,
        name=new_name,
        age=new_age,
        gender=new_gender,
        phone=new_phone
    )
    
    # Replace in list
    patients[patient_index] = updated_patient
    
    # Return as dictionary
    return updated_patient.to_dict()


def delete_patient(patient_id: int) -> bool:
    """
    Delete a patient from the system.
    
    Args:
        patient_id: ID of patient to delete.
        
    Returns:
        True if deleted, False if not found.
    """
    # Find the patient
    patient = find_patient_by_id(patient_id)
    if patient is None:
        return False
    
    # Remove the patient from the list
    patients.remove(patient)
    
    # Return True to show it was deleted
    return True
