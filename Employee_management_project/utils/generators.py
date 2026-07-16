"""Generator examples."""


def count_up(limit: int):
    """Yield numbers from 0 to limit - 1."""
    for value in range(limit):
        yield value
