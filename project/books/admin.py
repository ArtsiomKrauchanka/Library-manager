from django.contrib import admin
from .models import Genre, Author, Book, BookInstance, Opinion, BookReservation, BookRental


admin.site.register(Genre)
admin.site.register(Author)
admin.site.register(BookReservation)
admin.site.register(BookRental)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['id','title', 'author']
    search_fields = ['title', 'author__last_name', 'author__first_name']

@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ['id', 'book']
    search_fields = ['id', 'book__title', 'book__author__first_name', 'book__author__last_name']

@admin.register(Opinion)
class OpinionAdmin(admin.ModelAdmin):
    list_display = ('book','title', 'author', 'date_posted')
    search_fields = ('book__title','author__username', 'title', 'content')