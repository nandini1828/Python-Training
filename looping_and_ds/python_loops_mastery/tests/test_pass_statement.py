from looping_and_ds.python_loops_mastery.loops.pass_statement import pass_in_loop_demo, pass_in_condition_demo


def test_pass_in_loop_demo():
    assert pass_in_loop_demo() == "pass used inside loop"


def test_pass_in_condition_demo():
    assert pass_in_condition_demo(10) == "pass used inside condition"