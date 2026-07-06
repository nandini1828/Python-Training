"""
Unit tests for match_case utilities.
"""

from match_case.utils import (
    age_group,
    calculate,
    classify_point,
    execute_command,
    get_day,
    get_grade_remark,
    get_http_status,
    get_role_permissions,
    list_information,
    student_information,
)


def test_get_day():
    assert get_day(1) == "Monday"
    assert get_day(10) == "Invalid Day"


def test_calculate():
    assert calculate(10, 5, "+") == 15
    assert calculate(10, 5, "-") == 5
    assert calculate(10, 5, "*") == 50
    assert calculate(10, 5, "/") == 2
    assert calculate(10, 0, "/") == "Division by Zero"


def test_http_status():
    assert get_http_status(200) == "OK"
    assert get_http_status(404) == "Not Found"


def test_role_permissions():
    assert get_role_permissions("admin") == "Full Access"
    assert get_role_permissions("guest") == "Limited Access"


def test_grade_remark():
    assert get_grade_remark("A") == "Excellent"
    assert get_grade_remark("D") == "Average"


def test_classify_point():
    assert classify_point((0, 0)) == "Origin"
    assert classify_point((0, 5)) == "Y-Axis"
    assert classify_point((5, 0)) == "X-Axis"
    assert classify_point((3, 4)) == "General Point"


def test_list_information():
    assert list_information([]) == "Empty List"
    assert list_information([1]) == "Single Element"
    assert list_information([1, 2]) == "Two Elements"
    assert list_information([1, 2, 3]) == "Multiple Elements"


def test_student_information():
    student = {"name": "Ganesh", "age": 22}
    assert student_information(student) == "Ganesh (22)"


def test_age_group():
    assert age_group(15) == "Minor"
    assert age_group(30) == "Adult"
    assert age_group(70) == "Senior Citizen"


def test_execute_command():
    assert execute_command("start") == "Application Started"
    assert execute_command("restart") == "Application Restarted"
    assert execute_command("xyz") == "Unknown Command"