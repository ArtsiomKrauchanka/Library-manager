from django.shortcuts import render, redirect
from books.models import BookInstance
from django.shortcuts import render, get_object_or_404


def library(request):
    bookList = BookInstance.objects.order_by('-created_date')
    return render(request, 'books/library.html', {'title': 'Your library', 'library_class': 'nav-selected',
                                                  'show_extras': "no", 'bookInstanceList': bookList})


def bookDetails(request):
    bookInstance = get_object_or_404(BookInstance, pk=pk)
    return render(request, 'books/book_details.html', {'title': 'Book details', 'bookInstance': bookInstance})
