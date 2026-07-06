from zip_module.utils import *

def test_pair_lists():
    assert pair_lists([1,2], ["a","b"]) == [(1,"a"), (2,"b")]


def test_create_dict():
    assert create_dict(["a","b"], [1,2]) == {"a":1, "b":2}


def test_sum_pairs():
    assert sum_pairs([1,2], [3,4]) == [4,6]


def test_transpose_matrix():
    assert transpose_matrix([[1,2],[3,4]]) == [[1,3],[2,4]]