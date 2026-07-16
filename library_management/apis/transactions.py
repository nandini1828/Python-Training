from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from services.transaction_service import create_transaction, get_all_transactions


class TransactionRequest(BaseModel):
    member_id: int
    book_id: int
    action: str


router = APIRouter()


@router.get("/")
def list_transactions():
    return get_all_transactions()


@router.post("/")
def add_transaction(request: TransactionRequest):
    try:
        return create_transaction(
            member_id=request.member_id,
            book_id=request.book_id,
            action=request.action,
        )
    except ValueError as error:
        raise HTTPException(status_code=400, detail=str(error))
