from django.urls import path
from .views import elibrary, ebook_details, ebook_filter_view

urlpatterns = [
    path('elibrary/', elibrary, name='elibrary'),
    path('elibrary/search-ebook/', ebook_filter_view, name='filter_ebook'),
    path('ebook_details/<uuid:pk>/', ebook_details, name='ebook_details'),
]