from iterators_generators import generator_expression


def test_generator_expression_demo_output(capsys):
    generator_expression.demo()
    captured = capsys.readouterr()

    expected = [str(value) for value in [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]]

    assert captured.out.splitlines() == expected
