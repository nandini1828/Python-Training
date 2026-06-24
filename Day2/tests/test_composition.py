from __future__ import annotations

from composition.composition_utils import Employee, Department, Company


def test_company_composition_structure() -> None:
    employee = Employee("Ada", "Engineer")
    department = Department("Engineering", [employee])
    company = Company("Acme", [department])

    assert company.name == "Acme"
    assert company.departments[0].name == "Engineering"
    assert company.departments[0].employees[0].name == "Ada"
