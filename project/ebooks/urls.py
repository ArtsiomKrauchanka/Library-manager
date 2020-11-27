from django.urls import path
from .views import elibrary, ebook_details, ebook_filter_view, download_ebook

urlpatterns = [
    path('elibrary/', elibrary, name='elibrary'),
    path('elibrary/search-ebook/', ebook_filter_view, name='filter_ebook'),
    path('ebook_details/<uuid:pk>/', ebook_details, name='ebook_details'),
    path('ebook_details/download/<uuid:pk>/', download_ebook, name='download_ebook'),
]