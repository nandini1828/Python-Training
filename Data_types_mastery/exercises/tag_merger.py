from collection_utils.set_utils import merge_tags


def demo_merge_tags():
    tags_a = ["Python", "AI", "Coding", "python"]
    tags_b = ["ai", "Data", "python"]
    return merge_tags(tags_a, tags_b)
