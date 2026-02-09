"""
Sample queries for `relationship_app` demonstrating ORM relationships.

Use these helpers inside `manage.py shell` or any Django context.
"""
from typing import Iterable, Optional

from .models import Author, Book, Library, Librarian


def get_books_by_author_name(author_name: str) -> Iterable[Book]:
    try:
        author = Author.objects.get(name=author_name)
    except Author.DoesNotExist:
        return Book.objects.none()
    return Book.objects.filter(author=author)


def get_books_in_library(library_name: str) -> Iterable[Book]:
    try:
        library = Library.objects.get(name=library_name)
    except Library.DoesNotExist:
        return Book.objects.none()
    return library.books.all()


def get_librarian_for_library(library_name: str) -> Optional[Librarian]:
    try:
        library = Library.objects.get(name=library_name)
    except Library.DoesNotExist:
        return None
    return getattr(library, 'librarian', None)
