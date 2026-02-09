from django.contrib import admin

# Register your models here.

from .models import Author, Book, Library, Librarian, UserProfile


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
	list_display = ('id', 'name')


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
	list_display = ('id', 'title', 'author')


@admin.register(Library)
class LibraryAdmin(admin.ModelAdmin):
	list_display = ('id', 'name')
	filter_horizontal = ('books',)


@admin.register(Librarian)
class LibrarianAdmin(admin.ModelAdmin):
	list_display = ('id', 'name', 'library')


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
	list_display = ('user', 'role')
