from set_methods.set_utils import union, intersection, is_subset


def test_union_intersection_subset():
    a = ["a", "b"]
    b = ["b", "c"]
    assert union(a, b) == {"a", "b", "c"}
    assert intersection(a, b) == {"b"}
    assert is_subset(["a"], a)
