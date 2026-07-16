"""
Helper Utilities

This module contains helper functions for the application.
It's a place to put utility functions that don't belong in services or routers.
"""

from typing import Any, List
from app.models.patient import Patient
from app.models.doctor import Doctor


def get_object_attributes(obj: Any) -> List[str]:
    """
    Educational example demonstrating dir() function.
    
    The dir() function returns all attributes and methods of an object.
    This is useful for debugging and understanding what an object can do.
    
    Args:
        obj: Any Python object.
        
    Returns:
        List of attribute names for the object.
        
    Note:
        This function demonstrates dir() which lists all attributes and methods.
        In debugging, you might use this to explore an object's capabilities.
        
    Example:
        >>> patient = Patient(...)
        >>> attrs = get_object_attributes(patient)
        >>> "name" in attrs
        True
    """
    # dir() returns a list of all attributes and methods of an object
    return [attr for attr in dir(obj) if not attr.startswith('_')]


def is_function_callable(obj: Any) -> bool:
    """
    Check if an object is callable (i.e., can be called like a function).
    
    The callable() function returns True if the object can be called with parentheses.
    Functions, methods, and classes are callable. Regular values are not.
    
    Args:
        obj: Any Python object to check.
        
    Returns:
        True if the object is callable, False otherwise.
        
    Note:
        callable() is useful for checking if something is a function or method
        before trying to call it. This helps prevent errors.
        
    Example:
        >>> from app.services.patient_service import PatientService
        >>> is_function_callable(PatientService.get_all_patients)
        True
        >>> is_function_callable(PatientService.get_all_patients())
        False
    """
    # callable() returns True if the object can be called (like a function)
    return callable(obj)


def validate_positive_integer(value: int, field_name: str = "value") -> bool:
    """
    Validate that a value is a positive integer.
    
    Args:
        value: The value to validate.
        field_name: Name of the field (for error messages).
        
    Returns:
        True if value is positive, False otherwise.
        
    Note:
        This demonstrates basic validation using isinstance() to check
        if something is an integer before comparing it.
        
    Example:
        >>> validate_positive_integer(5, "ID")
        True
        >>> validate_positive_integer(0, "ID")
        False
        >>> validate_positive_integer(-1, "ID")
        False
    """
    # isinstance() checks if value is an integer type
    # This ensures we're comparing the right types
    if not isinstance(value, int):
        return False
    
    # Check if value is positive (greater than 0)
    return value > 0


def get_patient_summary(patient: Patient) -> str:
    """
    Generate a text summary of a patient's information.
    
    Args:
        patient: Patient object to summarize.
        
    Returns:
        String summary of patient information.
        
    Note:
        This demonstrates string formatting and type checking with isinstance().
    """
    # Validate that the argument is actually a Patient object
    if not isinstance(patient, Patient):
        return "Invalid patient object"
    
    # Create a formatted string with the patient information
    summary = f"{patient.name} ({patient.gender}), Age: {patient.age}, Phone: {patient.phone}"
    return summary


def get_doctor_summary(doctor: Doctor) -> str:
    """
    Generate a text summary of a doctor's information.
    
    Args:
        doctor: Doctor object to summarize.
        
    Returns:
        String summary of doctor information.
    """
    if not isinstance(doctor, Doctor):
        return "Invalid doctor object"
    
    summary = f"{doctor.name} - {doctor.specialization}, Experience: {doctor.experience} years"
    return summary


def filter_list_by_condition(items: List[Any], condition) -> List[Any]:
    """
    Filter a list using a condition function.
    
    This demonstrates using list comprehension with complex conditions.
    
    Args:
        items: List to filter.
        condition: A function that returns True for items to keep.
        
    Returns:
        Filtered list containing only items where condition is True.
        
    Example:
        >>> patients = [Patient(...), Patient(...)]
        >>> adults = filter_list_by_condition(
        ...     patients,
        ...     lambda p: p.age >= 18
        ... )
    """
    # List comprehension filters items based on the condition function
    # The condition function should accept an item and return True/False
    return [item for item in items if condition(item)]
