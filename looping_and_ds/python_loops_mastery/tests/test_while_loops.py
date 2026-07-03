from looping_and_ds.python_loops_mastery.loops.while_loops import count_with_while, sum_until_limit


def test_count_with_while():
    assert count_with_while(5) == [1, 2, 3, 4, 5]


def test_sum_until_limit():
    assert sum_until_limit(5) == 15