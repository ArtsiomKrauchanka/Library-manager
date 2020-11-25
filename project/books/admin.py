from django.contrib import admin

from .models import Genre
from .models import Author
from .models import Book
from .models import BookInstance

admin.site.register(Genre)
admin.site.register(Author)
admin.site.register(Book)
admin.site.register(BookInstance)

# Register your models here.
