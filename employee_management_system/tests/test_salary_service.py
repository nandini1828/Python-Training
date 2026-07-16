"""Tests for salary calculations."""

import pytest

from app.services.salary_service import SalaryService
from app.services.validation_service import ValidationService


@pytest.fixture
def salary_service() -> SalaryService:
    """Create a salary service for tests."""
    return SalaryService(validator=ValidationService())


def test_calculate_bonus_returns_expected_value(salary_service: SalaryService) -> None:
    """Bonus should be 10 percent of salary."""
    assert salary_service.calculate_bonus(100000) == 10000.0


def test_get_net_salary_includes_bonus(salary_service: SalaryService) -> None:
    """Net salary should include salary plus bonus."""
    assert salary_service.get_net_salary(100000) == 110000.0
