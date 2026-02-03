# Retrieve Book

Open Django shell:

```bash
python manage.py shell
```

Commands:

```py
from bookshelf.models import Book
Book.objects.all()  # -> QuerySet with the Book instances
book = Book.objects.get(title="1984")
book.title  # -> '1984'
book.author  # -> 'George Orwell'
book.publication_year  # -> 1949
```

Replace values above with the actual values from your environment.
