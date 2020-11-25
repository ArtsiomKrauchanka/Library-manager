from django.urls import path
from .views import library, bookDetails, book_filter_view

urlpatterns = [
    path('library/', library, name='library'),
    path('library/search-book/', book_filter_view, name='filter_book'),
    path('book_details/<uuid:pk>/', bookDetails, name='bookDetails'),
]