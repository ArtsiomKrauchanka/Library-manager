from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Book, Author, Genre
from .models import BookInstance, BookRental, BookReservation
from .forms import OpinionCreateForm
from users.models import Profile
from django.shortcuts import render, get_object_or_404


def library(request):
    bookList = Book.objects.all().order_by('title')
    genres = Genre.objects.all().order_by('name')

    context = {
        'title': 'Your library',
        'library_class': 'nav-selected',
        'show_extras': 'no',
        'bookList': bookList,
        'genres': genres,
    }
    return render(request, 'books/library.html', context)


def bookDetails(request, pk):
    book = get_object_or_404(Book, id=pk)

    def update_book_rating():
        rating = 0
        opinions = book.opinions.all()
        for opinion in opinions:
            rating += opinion.rating
        book.rating = round(rating / len(opinions),2)
        book.save()

    bookInstance = BookInstance.objects.get(book=pk)
    opinions = book.opinions.all()

    new_opinion = None

    # Opinion posted
    if request.method == 'POST':
        opinion_create_form = OpinionCreateForm(data=request.POST)
        if opinion_create_form.is_valid():
            if opinions.filter(author=request.user).exists():
                messages.warning(request, "Cannot add another review. You have already reviewed this book!")
                return redirect(f'/book_details/{pk}/')
            new_opinion = opinion_create_form.save(commit=False)
            new_opinion.book = book
            new_opinion.author = request.user
            opinion_create_form.save()
            update_book_rating()
            messages.success(request, "Review succesfully added!")
            return redirect(f'/book_details/{pk}/')
        elif bookInstance is not None:
                bookInstance.status = "R"
                bookInstance.save()
                bookReservation = BookReservation.objects.create(book=bookInstance, booker=request.user)
                bookReservation.save()
    else:
        opinion_create_form = OpinionCreateForm()

    return render(request, 'books/book_details.html', {'title': 'Book details', 'book': book, 'bookInstance': bookInstance})


def is_valid_queryparam(param):
    return param != '' and param is not None


def book_filter_view(request):
    qs = Book.objects.all()
    book_title = request.GET.get('book_title')
    book_author = request.GET.get('book_author')
    book_genre = request.GET.get('book_genre')
    book_rating = request.GET.get('book_rating')

    sort_method = request.GET.get('sort')

    genres = Genre.objects.all().order_by('name')
    searched = False
    most_popular = False

    if is_valid_queryparam(book_title):
        qs = qs.filter(title__icontains=book_title).order_by('title')
        searched = True
    elif is_valid_queryparam(book_author):
        qs = qs.filter(author__last_name__icontains=book_author) | qs.filter(author__first_name__icontains=book_author)
        qs = qs.order_by('title')
        searched = True
    if is_valid_queryparam(book_genre):
        qs = qs.filter(genre__name=book_genre)

    if is_valid_queryparam(sort_method):
        if sort_method == 'popularity':
            qs = qs.order_by('-rating')
            most_popular = True
        else:
            qs = qs.order_by(sort_method)

    context = {
        'bookList': qs,
        'genres': genres,
        'searched': searched,
        'genre': book_genre,
        'popularity_ranking': most_popular,
    }

    return render(request, 'books/library.html', context)
