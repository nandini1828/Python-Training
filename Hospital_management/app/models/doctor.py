"""Doctor model."""

from dataclasses import dataclass


@dataclass
class Doctor:
    doctor_id: int
    name: str
    specialization: str
