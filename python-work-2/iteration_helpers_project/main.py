from utils.printer import title

from iteration_helpers.range_examples import demo as range_demo
from iteration_helpers.enumerate_examples import demo as enumerate_demo
from iteration_helpers.zip_examples import demo as zip_demo
from iteration_helpers.reversed_sorted import demo as reverse_demo
from iteration_helpers.any_all import demo as any_demo


def main():

    title("Python Iteration Helpers")

    range_demo()
    enumerate_demo()
    zip_demo()
    reverse_demo()
    any_demo()


if __name__ == "__main__":
    main()