"""
Practical demonstrations of the iterator protocol.
"""

from .utils import CountDown, collect_iterator, get_first, is_iterable, manual_next


def main():
    print("\n===== Iterator Protocol Demo =====")
    countdown = CountDown(3)
    print("First value:", get_first(countdown))
    print("Collected:", collect_iterator(CountDown(3)))
    print("Manual next:", manual_next(iter([10, 20])))
    print("Is iterable:", is_iterable([1, 2, 3]))


if __name__ == "__main__":
    main()
