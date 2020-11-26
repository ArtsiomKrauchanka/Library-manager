from django.db import models
from books.models import Book
import uuid

def ebook_directory_path(instance, filename):
    return f'ebooks/{instance.book.title}/{filename}'

class Ebook(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    book = models.OneToOneField(Book, on_delete=models.CASCADE)
    txt_book = models.FileField(blank=True, null=True, upload_to=ebook_directory_path)
    pdf_book = models.FileField(blank=True, null=True, upload_to=ebook_directory_path)