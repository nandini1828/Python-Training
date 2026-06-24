from .set_utils import intersection_summary, symmetric_difference, set_statistics


def run_set_demo() -> None:
    left = [1, 2, 3, 4]
    right = [3, 4, 5, 6]
    diff = symmetric_difference(left, right)
    summary = intersection_summary(left, right)
    stats = set_statistics(left)

    print("Symmetric difference:", diff)
    print("Intersection summary:", summary)
    print("Set statistics:", stats)
