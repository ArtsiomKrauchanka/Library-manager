from django.shortcuts import render, redirect
from .models import Book
from django.shortcuts import render, get_object_or_404


def library(request):
    bookList = Book.objects.all().order_by('title')
    return render(request, 'books/library.html', {'title': 'Your library', 'library_class': 'nav-selected',
                                                  'show_extras': "no", 'bookList': bookList})



def bookDetails(request, pk):
    book = get_object_or_404(Book, id=pk)
    return render(request, 'books/book_details.html', {'title': 'Book details', 'book': book})
