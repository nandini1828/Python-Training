from fastapi import APIRouter, HTTPException, Query

from services.book_service import (
    create_book,
    delete_book,
    find_book_by_id,
    find_books_by_author,
    find_books_by_category,
    find_books_by_title,
    get_available_books,
    get_all_books,
    patch_book,
    update_book,
)

router = APIRouter()


@router.get("/")
def list_books(
    title: str | None = Query(None, description="Search books by title"),
    author: str | None = Query(None, description="Search books by author"),
    category: str | None = Query(None, description="Search books by category"),
):
    if title:
        return find_books_by_title(title)
    if author:
        return find_books_by_author(author)
    if category:
        return find_books_by_category(category)
    return get_all_books()


@router.get("/available")
def available_books():
    return get_available_books()


@router.get("/{book_id}")
def get_book(book_id: int):
    book = find_book_by_id(book_id)
    if book is None:
        raise HTTPException(status_code=404, detail="Book not found.")
    return book.to_dict()


@router.post("/")
def add_book(
    title: str,
    author: str,
    category: str,
    isbn: str,
    total_stock: int,
):
    try:
        return create_book(title=title, author=author, category=category, isbn=isbn, total_stock=total_stock)
    except ValueError as error:
        raise HTTPException(status_code=400, detail=str(error))


@router.put("/{book_id}")
def edit_book(
    book_id: int,
    title: str,
    author: str,
    category: str,
    isbn: str,
    total_stock: int,
):
    try:
        book = update_book(book_id, title=title, author=author, category=category, isbn=isbn, total_stock=total_stock)
    except ValueError as error:
        raise HTTPException(status_code=400, detail=str(error))

    if book is None:
        raise HTTPException(status_code=404, detail="Book not found.")
    return book


@router.patch("/{book_id}")
def patch_book_route(
    book_id: int,
    title: str | None = None,
    author: str | None = None,
    category: str | None = None,
    isbn: str | None = None,
    total_stock: int | None = None,
):
    try:
        book = patch_book(book_id, title=title, author=author, category=category, isbn=isbn, total_stock=total_stock)
    except ValueError as error:
        raise HTTPException(status_code=400, detail=str(error))

    if book is None:
        raise HTTPException(status_code=404, detail="Book not found.")
    return book


@router.delete("/{book_id}")
def remove_book(book_id: int):
    try:
        deleted = delete_book(book_id)
    except ValueError as error:
        raise HTTPException(status_code=400, detail=str(error))

    if not deleted:
        raise HTTPException(status_code=404, detail="Book not found.")
    return {"message": "Book deleted successfully."}
