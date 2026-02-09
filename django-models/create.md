```python
from bookshelf.models import Book
book = Book.objects.create(
    title="1984",
    author="George Orwell",
    publication_year=1949
)
book
```

---

### 📄 retrieve.md

````md
````python
Book.objects.all()


---

### 📄 update.md
```md
```python
book.title = "Nineteen Eighty-Four"
book.save()
book


---

### 📄 delete.md
```md
```python
book.delete()
Book.objects.all()


---

### 📄 CRUD_operations.md (MANDATORY)

```md
# CRUD Operations Using Django ORM

## Create
```python
Book.objects.create(title="1984", author="George Orwell", publication_year=1949)

Book.objects.all()

book.title = "Nineteen Eighty-Four"
book.save()

book.delete()
````
````
