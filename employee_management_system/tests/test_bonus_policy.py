"""Tests for bonus policy business rules."""

from app.business_rules.bonus_policy import BonusPolicy
from app.models.address import Address
from app.models.employee import Employee


def test_bonus_policy_calculates_ten_percent() -> None:
    """Bonus policy should compute ten percent of salary."""
    employee = Employee(
        employee_id="E100",
        first_name="Ivy",
        last_name="Moon",
        age=27,
        email="ivy@example.com",
        department_id="D001",
        salary=80000,
        address=Address(city="Austin", state="TX", country="USA", postal_code="73301"),
    )

    bonus = BonusPolicy.calculate_bonus(employee)

    assert bonus == 8000.0
