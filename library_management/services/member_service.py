from typing import List, Optional

from data.store import members
from models.member import Member
from utils.id_generator import generate_member_id


def get_all_members() -> List[dict]:
    return [member.to_dict() for member in members]


def find_member_by_id(member_id: int) -> Optional[Member]:
    return next((member for member in members if member.member_id == member_id), None)


def create_member(name: str, email: str) -> dict:
    if any(member.email.lower() == email.lower() for member in members):
        raise ValueError("Email already exists.")

    member = Member(name=name, email=email)
    member.member_id = generate_member_id()
    members.append(member)
    return member.to_dict()


def update_member(member_id: int, name: str, email: str) -> Optional[dict]:
    member = find_member_by_id(member_id)
    if member is None:
        return None

    if email.lower() != member.email.lower() and any(existing.email.lower() == email.lower() for existing in members):
        raise ValueError("Email already exists.")

    member.name = name
    member.email = email
    return member.to_dict()


def patch_member(member_id: int, name: str | None, email: str | None) -> Optional[dict]:
    member = find_member_by_id(member_id)
    if member is None:
        return None

    if email and email.lower() != member.email.lower() and any(existing.email.lower() == email.lower() for existing in members):
        raise ValueError("Email already exists.")

    if name:
        member.name = name
    if email:
        member.email = email
    return member.to_dict()


def delete_member(member_id: int) -> bool:
    member = find_member_by_id(member_id)
    if member is None:
        return False

    if member.borrowed_books:
        raise ValueError("Cannot delete a member with issued books.")

    members.remove(member)
    return True
