# Update Book

Open Django shell:

```bash
python manage.py shell
```

Commands:

```py
from bookshelf.models import Book
book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()
# Verify
Book.objects.get(pk=book.pk).title  # -> 'Nineteen Eighty-Four'
```
