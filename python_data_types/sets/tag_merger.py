"""
Tag merger exercise using sets.
"""


def merge_tags(tags_a, tags_b):
    """
    Returns:
    1. unique sorted tags
    2. shared tags
    3. tags only in A
    """

    a = set(tag.lower() for tag in tags_a)
    b = set(tag.lower() for tag in tags_b)

    unique_tags = sorted(a | b)
    shared_tags = sorted(a & b)
    only_in_a = sorted(a - b)

    return unique_tags, shared_tags, only_in_a