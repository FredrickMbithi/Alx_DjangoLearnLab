# ALX Django Learning Lab

A collection of Django projects and exercises created as part of the ALX Software Engineering program, demonstrating progressive learning from Django fundamentals to advanced web application development.

## Overview

This repository contains three Django projects showcasing different aspects of web development with Django framework:

1. **Introduction to Django** — Basic Django setup and project structure
2. **Django Models** — ORM, database relationships, and queries
3. **Django Blog** — Full-featured blog application with user authentication

## 🏗️ Repository Structure

```
Alx_DjangoLearnLab/
├── Introduction_to_Django/
│   └── django-models/          # Basic model examples
├── django-models/
│   ├── LibraryProject/         # Library management system
│   ├── bookshelf/              # Book catalog app
│   ├── create.md               # Setup instructions
│   └── query_samples.py        # Django ORM query examples
└── django_blog/
    ├── blog/                   # Blog application
    ├── django_blog/            # Project settings
    └── manage.py               # Django management script
```

## Learning Objectives

### Module 1: Introduction to Django
- Setting up Django development environment
- Understanding project vs app structure
- Creating first Django project
- Running development server

### Module 2: Django Models & ORM
- Defining models with Django ORM
- Database migrations (`makemigrations`, `migrate`)
- Model relationships (ForeignKey, ManyToMany)
- QuerySet API and database queries
- Django admin interface

### Module 3: Django Blog Application
- User authentication and authorization
- CRUD operations (Create, Read, Update, Delete)
- Template rendering with DTL (Django Template Language)
- Form handling and validation
- Static files management

## Quick Start

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Virtual environment (recommended)

### Installation

```bash
# Clone the repository
git clone https://github.com/FredrickMbithi/Alx_DjangoLearnLab.git
cd Alx_DjangoLearnLab

# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install Django
pip install django
```

### Running Projects

#### 1. Django Models Project

```bash
cd django-models
python manage.py migrate
python manage.py createsuperuser  # Create admin account
python manage.py runserver
```

Access admin panel: http://127.0.0.1:8000/admin

#### 2. Django Blog

```bash
cd django_blog
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Access blog: http://127.0.0.1:8000

## Project Details

### Django Models (Library Project)

**Location:** `django-models/LibraryProject/`

**Features:**
- Book model with fields (title, author, publication_year)
- Django admin integration
- Custom query examples in `query_samples.py`

**Key Files:**
- `bookshelf/models.py` — Model definitions
- `query_samples.py` — ORM query demonstrations
- `create.md` — Setup documentation

**Sample Queries:**
```python
# See query_samples.py for examples
from bookshelf.models import Book

# Retrieve all books
books = Book.objects.all()

# Filter books by author
books = Book.objects.filter(author="Author Name")

# Get single book
book = Book.objects.get(id=1)
```

### Django Blog Application

**Location:** `django_blog/`

**Features:**
- User registration and login
- Create, edit, delete blog posts
- User profiles
- Comment system (if implemented)
- Responsive templates

**Apps:**
- `blog/` — Main blog application
- `django_blog/` — Project configuration

**URLs:**
- `/` — Home page with post list
- `/post/<id>/` — Individual post detail
- `/post/new/` — Create new post
- `/admin/` — Admin interface

## Technologies Used

- **Django 4.x** — Web framework
- **SQLite** — Default database (dev)
- **Django ORM** — Object-Relational Mapping
- **Django Template Language** — Frontend templating
- **Django Admin** — Built-in admin interface

## Learning Resources

**Django Documentation:** https://docs.djangoproject.com/

**Key Concepts Covered:**
- MTV (Model-Template-View) architecture
- URL routing and views
- Database models and migrations
- Forms and validation
- User authentication
- Static files and media handling
- Django admin customization

## 🔧 Development Workflow

1. **Create Models** → Define data structure
2. **Make Migrations** → Generate migration files (`python manage.py makemigrations`)
3. **Apply Migrations** → Update database (`python manage.py migrate`)
4. **Create Views** → Handle request logic
5. **Configure URLs** → Map URLs to views
6. **Create Templates** → Design frontend
7. **Test** → Verify functionality

## Database Schema Examples

### Book Model (django-models)

```python
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()
    
    def __str__(self):
        return self.title
```

### Blog Post Model (django_blog)

```python
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
```

## ALX Program Context

This repository is part of the **ALX Software Engineering Program**, a comprehensive full-stack development curriculum. These projects demonstrate:

- Progressive skill development
- Django framework mastery
- Web development best practices
- MVC/MTV architectural patterns
- Database design and ORM usage

## Testing

Each project includes database files (`db.sqlite3`) for demonstration purposes. In production:

```bash
# Remove test databases
rm */db.sqlite3

# Create fresh migrations
python manage.py makemigrations
python manage.py migrate
```

## Notes

- Database files (`db.sqlite3`) are included for educational purposes
- `.pyc` files and `__pycache__` directories may be present
- Each project can run independently
- Some projects may share similar structure (intentional for learning progression)

## 🤝 Contributing

This is an educational repository. For learning purposes:

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to your fork
5. Submit a pull request

## License

Educational project - MIT License

## Author

**Fredrick Mbithi**  
ALX Software Engineering Student

## Related Projects

- [Advanced Library Management System](https://github.com/FredrickMbithi/Advanced-Library-Management-System) — Production-grade library system
- [Event Management API](https://github.com/FredrickMbithi/event_management_api) — Django REST Framework API

---

**Program:** ALX Software Engineering  
**Framework:** Django 4.x  
**Focus:** Web Development & Django Fundamentals  
**Status:** Learning Projects - Educational Use
