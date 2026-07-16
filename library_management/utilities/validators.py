from utilities.constants import AVAILABLE, BORROWED


def validate_book_payload(payload: dict) -> None:
    # If-elif-else and match-case both demonstrate structured decision-making.
    title = payload.get("title", "")
    author = payload.get("author", "")
    isbn = payload.get("isbn", "")

    if not title or not author:
        raise ValueError("Title and author are required")
    if len(isbn) < 5:
        raise ValueError("ISBN must be at least 5 characters")

    status = payload.get("status", AVAILABLE)
    match status:
        case 0:
            return
        case 1:
            return
        case _:
            raise ValueError("Status must be 0 (available) or 1 (borrowed)")


def validate_member_payload(payload: dict) -> None:
    # Short-circuit evaluation helps us exit quickly when validation fails.
    name = payload.get("name", "")
    email = payload.get("email", "")

    if not name or not email:
        raise ValueError("Name and email are required")
    if "@" not in email or "." not in email:
        raise ValueError("Email format is invalid")
