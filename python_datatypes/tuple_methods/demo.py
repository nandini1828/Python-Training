from .tuple_utils import tuple_slice, tuple_statistics, tuple_to_list


def run_tuple_demo() -> None:
    values = (10, 20, 20, 30)
    converted = tuple_to_list(values)
    sliced = tuple_slice(values, 1, 3)
    stats = tuple_statistics(values)

    print("Converted tuple:", converted)
    print("Sliced tuple:", sliced)
    print("Tuple statistics:", stats)
