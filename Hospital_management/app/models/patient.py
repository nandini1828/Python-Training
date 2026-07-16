"""Patient model."""

from dataclasses import dataclass


@dataclass
class Patient:
    patient_id: int
    name: str
    age: int
    gender: str
    disease: str
