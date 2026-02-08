"""
Sample queries for `relationship_app` demonstrating ORM relationships.

This script defines functions that can be used inside a Django shell or
imported from a management command. If you want to run it as a standalone
script, ensure `DJANGO_SETTINGS_MODULE` is set to your project settings and
call `django.setup()` before using the functions.

Examples:

    from relationship_app.query_samples import (
        get_books_by_author_name,
        get_books_in_library,
        get_librarian_for_library,
    )

    books = get_books_by_author_name('Agatha Christie')
    for b in books:
        print(b.title)

"""
from typing import Iterable, Optional

try:
    import django
    django.setup()
except Exception:
    # Running without Django configured is fine for static analysis.
    pass

from .models import Author, Book, Library, Librarian


def get_books_by_author_name(author_name: str) -> Iterable[Book]:
    """Return a queryset (iterable) of books written by `author_name`.

    Example:
        get_books_by_author_name('Jane Austen')
    """
    try:
        author = Author.objects.get(name=author_name)
    except Author.DoesNotExist:
        return Book.objects.none()
    return Book.objects.filter(author=author)


def get_books_in_library(library_name: str) -> Iterable[Book]:
    """Return all books that belong to the library named `library_name`.

    Uses the `Library.books` ManyToMany relation.
    """
    try:
        library = Library.objects.get(name=library_name)
    except Library.DoesNotExist:
        return Book.objects.none()
    return library.books.all()


def get_librarian_for_library(library_name: str) -> Optional[Librarian]:
    """Return the Librarian for a given library, or `None` if not found."""
    try:
        library = Library.objects.get(name=library_name)
    except Library.DoesNotExist:
        return None
    # thanks to related_name='librarian' we can access it directly
    return getattr(library, 'librarian', None)


if __name__ == '__main__':
    print('This module provides helper functions to query the relationship_app models.')
    print('Run these functions inside `manage.py shell` or configure Django settings before running.')
