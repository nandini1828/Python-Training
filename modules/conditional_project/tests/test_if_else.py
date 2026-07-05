from modules.conditional_project.conditions.if_else import *


def test_grade_a():
    assert calculate_grade(95) == "A"


def test_grade_b():
    assert calculate_grade(80) == "B"


def test_grade_fail():
    assert calculate_grade(20) == "Fail"


def test_gold_plan():
    assert insurance_plan(200000) == "Gold"


def test_bronze_plan():
    assert insurance_plan(10000) == "Bronze"


def test_voting():
    assert voting_eligibility(22) == "Eligible"


def test_minor():
    assert voting_eligibility(15) == "Not Eligible"


def test_hot():
    assert temperature_status(42) == "Hot"