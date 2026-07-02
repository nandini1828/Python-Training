from utils.printer import title

from iterators_generators.iterator_protocol import demo as iterator_demo
from iterators_generators.generators import demo as generator_demo
from iterators_generators.generator_expression import demo as expression_demo


def main():

    title("Iterators & Generators")

    iterator_demo()
    generator_demo()
    expression_demo()


if __name__ == "__main__":
    main()