"""Compatibility wrapper re-exporting query helper functions.

This file forwards calls to the real `relationship_app.query_samples` so code
importing `LibraryProject.relationship_app.query_samples` will work as expected.
"""
from relationship_app.query_samples import (
    get_books_by_author_name,
    get_books_in_library,
    get_librarian_for_library,
)

__all__ = [
    'get_books_by_author_name',
    'get_books_in_library',
    'get_librarian_for_library',
]
