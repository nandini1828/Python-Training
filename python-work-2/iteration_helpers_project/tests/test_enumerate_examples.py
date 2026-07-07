from iteration_helpers import enumerate_examples


def test_enumerate_demo_output(capsys):
    enumerate_examples.demo()
    captured = capsys.readouterr()

    assert captured.out.splitlines() == ["0 Alice", "1 Bob", "2 Charlie"]
