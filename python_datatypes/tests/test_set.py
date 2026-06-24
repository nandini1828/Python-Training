from python_datatypes.set_methods import intersection_summary, set_statistics, symmetric_difference


def test_set_symmetric_difference() -> None:
    assert symmetric_difference([1, 2, 3], [2, 3, 4]) == {1, 4}


def test_intersection_summary_returns_expected_sets() -> None:
    result = intersection_summary([1, 2, 3], [2, 4])
    assert set(result["intersection"]) == {2}
    assert set(result["left_only"]) == {1, 3}
    assert set(result["right_only"]) == {4}


def test_set_statistics_reports_unique_elements() -> None:
    stats = set_statistics([1, 1, 2])
    assert stats["count"] == 2
    assert stats["unique"] == 2
