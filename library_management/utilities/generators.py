def generate_book_ids(limit: int):
    # yield turns this function into a generator that streams values lazily.
    for value in range(1, limit + 1):
        yield value


def iter_member_names(members):
    # Generator expressions can be used to build a stream of values.
    return (member["name"] for member in members)


def book_id_stream(prefix: str, count: int):
    # range() and yield are combined to create a simple sequence generator.
    for index in range(1, count + 1):
        yield f"{prefix}-{index}"
