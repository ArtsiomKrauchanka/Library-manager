from django.urls import path
from .views import library, bookDetails

urlpatterns = [

    path('library', library, name='library'),
    path('book_details/<uuid:pk>/', bookDetails, name='bookDetails')

]