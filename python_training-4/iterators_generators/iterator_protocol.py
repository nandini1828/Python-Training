class BookIterator:

    def __init__(self, books):

        self.books = books
        self.index = 0

    def __iter__(self):

        return self

    def __next__(self):

        if self.index >= len(self.books):

            raise StopIteration

        book = self.books[self.index]

        self.index += 1

        return book


def browse_books(books):

    print("\nBrowsing Books")

    iterator = BookIterator(books)

    for book in iterator:

        print(book.title)