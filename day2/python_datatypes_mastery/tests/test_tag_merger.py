
from exercises import merge_tags


def test_merge_tags():

    result = merge_tags(
        ["Python", "AI"],
        ["python", "ML"]
    )

    assert result["all_tags"] == [
        "ai",
        "ml",
        "python"
    ]

    assert result["common"] == [
        "python"
    ]