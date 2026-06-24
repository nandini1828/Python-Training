from __future__ import annotations

from dataclasses import dataclass, field
from typing import List


@dataclass(slots=True)
class Employee:
    """Represents a company employee."""

    name: str
    role: str


@dataclass(slots=True)
class Department:
    """Represents a department composed of employees."""

    name: str
    employees: List[Employee] = field(default_factory=list)


@dataclass(slots=True)
class Company:
    """Represents a company composed of departments."""

    name: str
    departments: List[Department] = field(default_factory=list)
