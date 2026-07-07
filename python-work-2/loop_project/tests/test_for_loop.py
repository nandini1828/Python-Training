from loops import for_loop


def test_iterate_list_output(capsys):
    for_loop.iterate_list()
    captured = capsys.readouterr()

    assert captured.out.splitlines() == ["Apple", "Orange", "Banana"]


def test_iterate_string_output(capsys):
    for_loop.iterate_string()
    captured = capsys.readouterr()

    assert captured.out.splitlines() == ["P", "y", "t", "h", "o", "n"]


def test_iterate_range_output(capsys):
    for_loop.iterate_range()
    captured = capsys.readouterr()

    assert captured.out.splitlines() == ["0", "1", "2", "3", "4"]
