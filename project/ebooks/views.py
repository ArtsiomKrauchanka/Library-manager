from django.shortcuts import render, redirect, get_object_or_404
from .models import Ebook
from books.models import Genre
from books.forms import OpinionCreateForm

def elibrary(request):
    ebook_list = Ebook.objects.all().order_by('book__title')
    genres = Genre.objects.all().order_by('name')
    
    context = {
        'title': 'Available ebooks',
        'library_class': 'nav-selected',
        'show_extras': 'no', 
        'ebook_list': ebook_list,
        'genres': genres,
    }
    return render(request, 'ebooks/elibrary.html', context)

def ebook_details(request, pk):
    ebook = get_object_or_404(Ebook, id=pk)
    opinions = ebook.book.opinions.all()
    new_opinion = None

    # Opinion posted
    if request.method == 'POST' and not opinions.filter(author=request.user).exists():
        opinion_create_form = OpinionCreateForm(data=request.POST)
        if opinion_create_form.is_valid():
            new_opinion = opinion_create_form.save(commit=False)
            new_opinion.book = ebook.book
            new_opinion.author = request.user
            opinion_create_form.save()
    else:
        opinion_create_form = OpinionCreateForm()

    return render(request, 'ebooks/ebook_details.html', {'title': 'Book details', 'ebook': ebook})


def is_valid_queryparam(param):
    return param != '' and param is not None

def ebook_filter_view(request):
    qs = Ebook.objects.all()
    ebook_title = request.GET.get('ebook_title')
    ebook_genre = request.GET.get('ebook_genre')
    
    genres = Genre.objects.all().order_by('name')
    searched = False

    if is_valid_queryparam(ebook_title):
        qs = qs.filter(book__title__icontains=ebook_title).order_by('book__title')
        searched = True
    if is_valid_queryparam(ebook_genre):
        qs = qs.filter(book__genre__name=ebook_genre)
    
    context = {
        'ebook_list': qs,
        'genres': genres,
        'searched': searched,
        'genre': ebook_genre,
    }

    return render(request, 'ebooks/elibrary.html', context)