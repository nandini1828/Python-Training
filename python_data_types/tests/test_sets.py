from sets import (
    add_item,
    remove_item,
    union_sets,
    intersection_sets,
    difference_sets,
    merge_tags
)


# -----------------------
# BASIC SET METHODS TESTS
# -----------------------

def test_add_item():
    s = {1, 2}
    result = add_item(s, 3)
    assert 3 in result


def test_remove_item():
    s = {1, 2, 3}
    result = remove_item(s, 2)
    assert 2 not in result


def test_union_sets():
    a = {1, 2}
    b = {2, 3}
    assert union_sets(a, b) == {1, 2, 3}


def test_intersection_sets():
    a = {1, 2}
    b = {2, 3}
    assert intersection_sets(a, b) == {2}


def test_difference_sets():
    a = {1, 2, 3}
    b = {2}
    assert difference_sets(a, b) == {1, 3}


# -----------------------
# TAG MERGER TESTS
# -----------------------

def test_merge_tags_basic():
    tags_a = ["Python", "AI", "ML"]
    tags_b = ["ai", "data", "ml"]

    unique, shared, only_a = merge_tags(tags_a, tags_b)

    assert "python" in unique
    assert "ai" in shared
    assert "ml" in shared


def test_merge_tags_only_in_a():
    tags_a = ["x", "y", "z"]
    tags_b = ["z"]

    unique, shared, only_a = merge_tags(tags_a, tags_b)

    assert "x" in only_a
    assert "y" in only_a
    assert "z" not in only_a


def test_merge_tags_case_insensitive():
    tags_a = ["Python", "Data"]
    tags_b = ["python", "AI"]

    unique, shared, only_a = merge_tags(tags_a, tags_b)

    assert all(tag == tag.lower() for tag in unique)
    assert all(tag == tag.lower() for tag in shared)
    assert all(tag == tag.lower() for tag in only_a)