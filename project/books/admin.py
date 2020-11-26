from django.contrib import admin
from .models import Genre, Author, Book, BookInstance, Opinion


admin.site.register(Genre)
admin.site.register(Author)
admin.site.register(Book)
admin.site.register(BookInstance)

@admin.register(Opinion)
class OpinionAdmin(admin.ModelAdmin):
    list_display = ('book','title', 'author', 'date_posted')
    search_fields = ('book__title','author__username', 'title', 'content')