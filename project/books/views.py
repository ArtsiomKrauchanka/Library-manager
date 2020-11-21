from django.shortcuts import render, redirect

def library(request):
    return render(request, 'books/library.html', {'title': 'Your library','library_selcted_class':'nav-selected', 'show_extras':"no"})
