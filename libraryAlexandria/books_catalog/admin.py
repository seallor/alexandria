from django.contrib import admin

from .models import Author, Genre, Book, Language


class BooksInline(admin.TabularInline):
    model = Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_filter = ('language',)
    list_display = ('title', 'author', 'language', 'display_genre')


class AuthorAdmin(admin.ModelAdmin):
    list_filter = ('first_name', 'date_of_death')
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    inlines = [BooksInline]


admin.site.register(Author, AuthorAdmin)
admin.site.register(Genre)
admin.site.register(Language)

# Register your models here.
