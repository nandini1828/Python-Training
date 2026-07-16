from services.library_service import list_books, list_members
from utilities.generators import generate_book_ids, iter_member_names


def collect_book_titles(books=None) -> list[str]:
    # enumerate() allows us to pair each title with its position in the list.
    source = books if books is not None else list_books()
    return [title for _, title in enumerate(book["title"] for book in source)]


def get_member_name_stream() -> list[str]:
    # zip() can pair two iterables together and iterators can be consumed lazily.
    names = list(iter_member_names(list_members()))
    return names


def preview_ids(limit: int = 3) -> list[int]:
    # A generator expression can be consumed into a list for easy inspection.
    return list(generate_book_ids(limit))
