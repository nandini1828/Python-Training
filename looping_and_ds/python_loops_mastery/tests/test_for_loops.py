from loops.for_loops import iterate_list, iterate_string, iterate_range


def test_iterate_list():
    assert iterate_list(["a", "b", "c"]) == ["a", "b", "c"]


def test_iterate_string():
    assert iterate_string("abc") == ["a", "b", "c"]


def test_iterate_range():
    assert iterate_range(1, 5) == [1, 2, 3, 4]