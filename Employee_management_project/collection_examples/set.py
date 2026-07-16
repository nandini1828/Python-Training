"""Skill tracking helpers."""

employee_skills = {"Python", "FastAPI", "Testing"}


def add_skill(skill: str) -> set[str]:
    employee_skills.add(skill)
    return employee_skills


def remove_skill(skill: str) -> set[str]:
    employee_skills.discard(skill)
    return employee_skills
