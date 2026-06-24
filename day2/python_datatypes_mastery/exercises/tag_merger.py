def merge_tags(
    tags_a: list[str],
    tags_b: list[str]
) -> dict[str, list[str]]:

    set_a: set[str] = {tag.lower() for tag in tags_a}
    set_b: set[str] = {tag.lower() for tag in tags_b}

    return {
        "all_tags": sorted(set_a | set_b),
        "common": sorted(set_a & set_b),
        "only_a": sorted(set_a - set_b)
    }