from iteration_helpers.enumerate_helper import enumerate_items


def test_enumerate_items():
    assert enumerate_items(["a", "b", "c"]) == [(0, "a"), (1, "b"), (2, "c")]