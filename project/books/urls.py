from django.urls import path
from .views import library, bookDetails, book_search_view

urlpatterns = [
    path('library/', library, name='library'),
    path('library/search-book/', book_search_view, name='search_book'),
    path('book_details/<uuid:pk>/', bookDetails, name='bookDetails'),
]