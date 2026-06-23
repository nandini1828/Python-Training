def merge_tags(tags_a, tags_b):

    set_a = {tag.lower() for tag in tags_a}
    set_b = {tag.lower() for tag in tags_b}

    all_tags = sorted(set_a | set_b)
    common_tags = sorted(set_a & set_b)
    unique_a = sorted(set_a - set_b)

    return all_tags, common_tags, unique_a