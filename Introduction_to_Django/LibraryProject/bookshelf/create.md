# Create and run commands for the `bookshelf` app

This file documents useful commands to create migrations, apply them, create a superuser, and run the development server for the `bookshelf` app in this project.

1. From the project root (`Introduction_to_Django`) create migrations for the `bookshelf` app:

```bash
cd /home/ghost/Alx_DjangoLearnLab/Introduction_to_Django
python manage.py makemigrations bookshelf
```

2. Apply migrations to the database:

```bash
python manage.py migrate
```

3. Create a Django superuser (follow prompts for username / email / password):

```bash
python manage.py createsuperuser
```

4. Run the development server (default: http://127.0.0.1:8000/):

```bash
python manage.py runserver
```

5. Quick shell examples for creating/querying `Book` objects (use the current `Book` model fields: `title`, `author`, `published_date`, `isbn`):

```bash
python manage.py shell
```

Inside the Django shell:

```py
from bookshelf.models import Book
from datetime import date
book = Book.objects.create(title="1984", author="George Orwell", published_date=date(1949,6,8), isbn="9780451524935")
Book.objects.all()
book.title = "Nineteen Eighty-Four"
book.save()
book.delete()
```

Notes:
- If you change the model (add/remove fields) remember to run `makemigrations` and `migrate` again.
- If you need a `publication_year` integer field instead of `published_date`, update `bookshelf/models.py` and create a migration.
