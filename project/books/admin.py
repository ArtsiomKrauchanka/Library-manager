from django.contrib import admin
from .models import Genre, Author, Book, BookInstance, Opinion


admin.site.register(Genre)
admin.site.register(Author)
admin.site.register(BookInstance)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['id','title', 'author']
    search_fields = ['title', 'author__last_name', 'author__first_name']

@admin.register(Opinion)
class OpinionAdmin(admin.ModelAdmin):
    list_display = ('book','title', 'author', 'date_posted')
    search_fields = ('book__title','author__username', 'title', 'content')