from fastapi import APIRouter, HTTPException

from models.book import BookCreate, BookRead
from services.library_service import create_book, delete_book, get_book, list_books, update_book

router = APIRouter()


@router.post("/", response_model=BookRead)
def create_book_api(payload: BookCreate):
    return create_book(payload.model_dump())


@router.get("/", response_model=list[BookRead])
async def list_books_api():
    return list_books()


@router.get("/{book_id}", response_model=BookRead)
def get_book_api(book_id: int):
    book = get_book(book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book


@router.put("/{book_id}", response_model=BookRead)
def update_book_api(book_id: int, payload: BookCreate):
    book = update_book(book_id, payload.model_dump())
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book


@router.delete("/{book_id}")
def delete_book_api(book_id: int):
    deleted = delete_book(book_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Book not found")
    return {"deleted": True}
