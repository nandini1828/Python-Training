"""
Patient Tests

Test cases for patient-related functionality using pytest.

pytest is a testing framework that discovers and runs tests automatically.
Test functions should start with "test_" and assertions should use assert statements.
"""

import pytest
from app.models.patient import Patient, PatientUpdate
from app.services.patient_service import PatientService, patients


class TestPatientService:
    """
    Test class for Patient Service.
    
    Grouping related tests in a class makes the test suite more organized.
    """
    
    def setup_method(self):
        """
        Setup method runs before each test.
        
        This is a pytest fixture pattern. We use it to reset the data
        to a known state before each test, ensuring tests don't affect each other.
        
        Note:
            This is important because tests should be independent.
            If one test modifies the data, it could affect other tests.
        """
        # Clear existing data and add fresh test data
        patients.clear()
        patients.append(Patient(id=1, name="John Doe", age=30, gender="Male", phone="9876543210"))
        patients.append(Patient(id=2, name="Jane Smith", age=28, gender="Female", phone="9123456789"))
    
    def test_get_all_patients(self):
        """
        Test retrieving all patients.
        
        This test checks if get_all_patients returns all patients in the list.
        """
        result = PatientService.get_all_patients()
        
        # Assert that the result is a list
        assert isinstance(result, list)
        
        # Assert that we got the expected number of patients
        assert len(result) == 2
    
    def test_get_patient_by_id_found(self):
        """
        Test retrieving a patient that exists.
        
        This tests the happy path where the patient is found.
        """
        result = PatientService.get_patient_by_id(1)
        
        # Assert that we got a Patient object back (not None)
        assert result is not None
        
        # Assert that it's the correct patient
        assert result.id == 1
        assert result.name == "John Doe"
    
    def test_get_patient_by_id_not_found(self):
        """
        Test retrieving a patient that doesn't exist.
        
        This tests the error case where the patient is not found.
        """
        result = PatientService.get_patient_by_id(999)
        
        # Assert that None is returned for non-existent patient
        assert result is None
    
    def test_add_patient(self):
        """
        Test adding a new patient.
        
        This tests creating and storing a new patient.
        """
        new_patient = Patient(id=3, name="Mike Johnson", age=45, gender="Male", phone="9988776655")
        
        # Add the patient
        result = PatientService.add_patient(new_patient)
        
        # Assert that the added patient is returned
        assert result.id == 3
        assert result.name == "Mike Johnson"
        
        # Assert that the patient was actually added to the list
        assert len(patients) == 3
    
    def test_update_patient_found(self):
        """
        Test updating a patient that exists.
        """
        # Create an update with only name field
        update = PatientUpdate(name="John Updated")
        
        # Update the patient
        result = PatientService.update_patient(1, update)
        
        # Assert that update was successful
        assert result is not None
        assert result.name == "John Updated"
        
        # Assert that other fields remain unchanged
        assert result.age == 30
    
    def test_update_patient_not_found(self):
        """
        Test updating a patient that doesn't exist.
        """
        update = PatientUpdate(name="Unknown")
        
        result = PatientService.update_patient(999, update)
        
        # Assert that None is returned when patient not found
        assert result is None
    
    def test_delete_patient_found(self):
        """
        Test deleting a patient that exists.
        """
        # Before deletion, we should have 2 patients
        assert len(patients) == 2
        
        # Delete the patient
        result = PatientService.delete_patient(1)
        
        # Assert that deletion was successful
        assert result is True
        
        # Assert that the patient count decreased
        assert len(patients) == 1
        
        # Assert that the deleted patient is no longer in the list
        assert PatientService.get_patient_by_id(1) is None
    
    def test_delete_patient_not_found(self):
        """
        Test deleting a patient that doesn't exist.
        """
        result = PatientService.delete_patient(999)
        
        # Assert that deletion failed (returns False)
        assert result is False
        
        # Assert that the list size hasn't changed
        assert len(patients) == 2
