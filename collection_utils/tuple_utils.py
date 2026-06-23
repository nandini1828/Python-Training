def tuple_examples():
    """Return tuple method results for count() and index()."""
    example = (1, 2, 2, 3)
    return {
        "count_2": example.count(2),
        "index_3": example.index(3),
    }
