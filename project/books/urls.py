from django.urls import path
from .views import library, book_details

urlpatterns = [
    path('library/', library, name='library'),
    path('bookDetails/<int:pk>/', book_details, name='bookDetails'),
]