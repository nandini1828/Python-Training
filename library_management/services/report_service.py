from services.library_service import list_books, list_members
from utilities.helpers import classify_status


def get_summary() -> dict:
    books = list_books()
    members = list_members()

    # Looping through collections and using a conditional check to build a summary.
    total_borrowed = sum(1 for book in books if book["status"] == 1)
    total_available = len(books) - total_borrowed

    summary = {
        "total_books": len(books),
        "total_members": len(members),
        "borrowed_books": total_borrowed,
        "available_books": total_available,
        "status_labels": [classify_status(book["status"]) for book in books],
    }
    return summary
