# Delete Book

Open Django shell:

```bash
python manage.py shell
```

Commands:

```py
from bookshelf.models import Book
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()
# Verify
Book.objects.all()  # -> empty QuerySet if that was the only book
```
