from rest_framework.viewsets import ModelViewSet

from .models import Author, Book, Member
from .serializers import (
    AuthorSerializer,
    BookSerializer,
    MemberSerializer,
)


class AuthorViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class MemberViewSet(ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer