from truthiness import count_truthy_falsy


def test_truthiness():
    data = [0, "hello", [], None, True, 3.14]
    result = count_truthy_falsy(data)

    assert result["truthy"] == 3
    assert result["falsy"] == 3