from utils.printer import title

from comprehensions.list_comprehension import demo as list_demo
from comprehensions.dictionary_comprehension import demo as dictionary_demo
from comprehensions.set_comprehension import demo as set_demo
from comprehensions.nested_comprehension import demo as nested_demo


def main():

    title("Comprehensions")

    list_demo()
    dictionary_demo()
    set_demo()
    nested_demo()


if __name__ == "__main__":
    main()