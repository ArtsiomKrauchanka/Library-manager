from django.urls import path
from .views import library
from .views import bookDetails

urlpatterns = [
    path('library', library, name='library'),
    path('bookDetails/<int:pk>/', bookDetails, name='bookDetails')
]