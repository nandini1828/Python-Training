def merge_tags(tags_a, tags_b):
    """Normalize, deduplicate, and sort tags from two tag lists."""
    normalized_a = {tag.lower() for tag in tags_a}
    normalized_b = {tag.lower() for tag in tags_b}
    all_unique = sorted(normalized_a | normalized_b)
    shared = sorted(normalized_a & normalized_b)
    in_a_not_b = sorted(normalized_a - normalized_b)
    return all_unique, shared, in_a_not_b
