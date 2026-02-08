"""
Compatibility wrapper exposing the app models at the project-level
so tests that expect `django-models/models.py` can import them.
"""
from relationship_app.models import Author, Book, Library, Librarian  # noqa: F401
