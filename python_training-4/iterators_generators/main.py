from model import Book

from utils import print_title

from iterator_protocol import browse_books
from generators import display_coupons
from generator_expressions import discounted_prices


def main():

    books = [

        Book(101,"Python Basics",599),

        Book(102,"Django Mastery",799),

        Book(103,"FastAPI Guide",699),

        Book(104,"Machine Learning",999)

    ]

    print_title("Online Book Store")

    browse_books(books)

    display_coupons()

    discounted_prices(books)


if __name__ == "__main__":

    main()