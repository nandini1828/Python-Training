from fastapi import APIRouter, HTTPException

from services.member_service import (
    create_member,
    delete_member,
    find_member_by_id,
    get_all_members,
    patch_member,
    update_member,
)

router = APIRouter()


@router.get("/")
def list_members():
    return get_all_members()


@router.get("/{member_id}")
def get_member(member_id: int):
    member = find_member_by_id(member_id)
    if member is None:
        raise HTTPException(status_code=404, detail="Member not found.")
    return member.to_dict()


@router.post("/")
def add_member(name: str, email: str):
    try:
        return create_member(name=name, email=email)
    except ValueError as error:
        raise HTTPException(status_code=400, detail=str(error))


@router.put("/{member_id}")
def edit_member(member_id: int, name: str, email: str):
    try:
        member = update_member(member_id=member_id, name=name, email=email)
    except ValueError as error:
        raise HTTPException(status_code=400, detail=str(error))

    if member is None:
        raise HTTPException(status_code=404, detail="Member not found.")
    return member


@router.patch("/{member_id}")
def patch_member_route(member_id: int, name: str | None = None, email: str | None = None):
    try:
        member = patch_member(member_id=member_id, name=name, email=email)
    except ValueError as error:
        raise HTTPException(status_code=400, detail=str(error))

    if member is None:
        raise HTTPException(status_code=404, detail="Member not found.")
    return member


@router.delete("/{member_id}")
def remove_member(member_id: int):
    try:
        deleted = delete_member(member_id)
    except ValueError as error:
        raise HTTPException(status_code=400, detail=str(error))

    if not deleted:
        raise HTTPException(status_code=404, detail="Member not found.")
    return {"message": "Member deleted successfully."}
