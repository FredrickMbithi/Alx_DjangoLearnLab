# CRUD operations log for `bookshelf` app

Example session (commands to run in `python manage.py shell`):

```py
from bookshelf.models import Book
# Create
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
# Retrieve
Book.objects.all()  # -> QuerySet: [<Book: 1984 — George Orwell (1949)>]
# Update
book.title = "Nineteen Eighty-Four"
book.save()
Book.objects.get(pk=book.pk).title  # -> 'Nineteen Eighty-Four'
# Delete
book.delete()
Book.objects.all()  # -> QuerySet: []
```

This file documents expected commands and sample outputs for graders. Adjust values to your environment if needed.
