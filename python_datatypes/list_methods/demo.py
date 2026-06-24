from .list_utils import paginate_list, unique_ordered


def run_list_demo() -> None:
    sample = [1, 2, 3, 3, 4, 5, 5, 6]
    unique_values = unique_ordered(sample)
    first_page = paginate_list(sample, page=1, page_size=3)

    print("Unique ordered values:", unique_values)
    print("First page:", first_page)
