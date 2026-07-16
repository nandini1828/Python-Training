from fastapi import APIRouter, HTTPException

from models.member import MemberCreate, MemberRead
from services.library_service import create_member, get_member, list_members

router = APIRouter()


@router.post("/", response_model=MemberRead)
def create_member_api(payload: MemberCreate):
    return create_member(payload.model_dump())


@router.get("/", response_model=list[MemberRead])
def list_members_api():
    return list_members()


@router.get("/{member_id}", response_model=MemberRead)
def get_member_api(member_id: int):
    member = get_member(member_id)
    if not member:
        raise HTTPException(status_code=404, detail="Member not found")
    return member
