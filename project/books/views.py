from django.shortcuts import render, redirect
from .models import Book, Author
from django.shortcuts import render, get_object_or_404


def library(request):
    bookList = Book.objects.all().order_by('title')
    return render(request, 'books/library.html', {'title': 'Your library', 'library_class': 'nav-selected',
                                                  'show_extras': "no", 'bookList': bookList})



def bookDetails(request, pk):
    book = get_object_or_404(Book, id=pk)
    return render(request, 'books/book_details.html', {'title': 'Book details', 'book': book})

def book_search_view(request):
    qs = Book.objects.all()
    book_title = request.GET.get('book_title')
    book_author = request.GET.get('book_author')

    if book_title != '' and book_title is not None:
        qs = qs.filter(title__icontains=book_title).order_by('title')
    elif book_author != '' and book_author is not None:
        qs = qs.filter(author__last_name__icontains=book_author) | qs.filter(author__first_name__icontains=book_author)
        qs = qs.order_by('title')
    context = {
        'bookList': qs
    }

    return render(request, 'books/library.html', context)