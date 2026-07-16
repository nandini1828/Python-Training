"""
data.py

This file acts as our in-memory database.

Instead of using MySQL or SQLite, we are storing
everything in Python data structures.
"""


# Dictionary to store patients
# Key   -> Patient ID
# Value -> Patient Object
patients = {}


# Dictionary to store doctors
doctors = {}


# List to store appointments
appointments = []


# Set to store departments
# Duplicate department names are not allowed.

departments = {
    "Cardiology",
    "Neurology",
    "Orthopedics",
    "General Medicine"
}


# Tuple to store hospital information
# Tuple is immutable.

hospital_info = (
    "ABC Hospital",
    "Hyderabad"
)