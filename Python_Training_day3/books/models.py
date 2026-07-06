from django.db import models


class Author(models.Model):
    """
    Represents an author who writes books.
    """

    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self) -> str:
        return self.name


class Book(models.Model):
    """
    Represents a book in the library.
    """

    title = models.CharField(max_length=200)
    publication_year = models.IntegerField()
    available = models.BooleanField(default=True)

    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        related_name="books"
    )

    def __str__(self) -> str:
        return self.title


class Member(models.Model):
    """
    Represents a library member.
    """

    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    membership_date = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name