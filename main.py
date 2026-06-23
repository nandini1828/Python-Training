from day1.examples.class_objects import main as class_demo
from day1.examples.data_types import display_basic_data_types
from day1.examples.oops_examples import main as oops_demo

from day2.examples.collections_examples import main as collections_demo
from day2.examples.introspection_examples import main as introspection_demo
from day2.examples.json_examples import main as json_demo


def main() -> None:

    print("\n=== DAY 1 ===\n")

    display_basic_data_types()
    class_demo()
    oops_demo()

    print("\n=== DAY 2 ===\n")

    collections_demo()
    introspection_demo()
    json_demo()


if __name__ == "__main__":
    main()