import itertools

book_id_sequence = itertools.count(1)
member_id_sequence = itertools.count(1)
transaction_id_sequence = itertools.count(1)


def generate_book_id() -> int:
    return next(book_id_sequence)


def generate_member_id() -> int:
    return next(member_id_sequence)


def generate_transaction_id() -> int:
    return next(transaction_id_sequence)
