from utils.printer import title

from data_structures.lists import demo as list_demo
from data_structures.list_modification import demo as modification_demo
from data_structures.dictionaries import demo as dictionary_demo
from data_structures.dictionary_safety import demo as safety_demo
from data_structures.sets import demo as set_demo


def main():

    title("Data Structure Iteration & Safety")

    list_demo()
    modification_demo()
    dictionary_demo()
    safety_demo()
    set_demo()


if __name__ == "__main__":
    main()