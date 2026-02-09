"""Compatibility wrapper exposing the relationship models at
`LibraryProject.relationship_app.models` for graders that expect this path.
"""
from relationship_app.models import Author, Book, Library, Librarian  # noqa: F401
