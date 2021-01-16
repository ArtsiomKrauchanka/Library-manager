from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User
import datetime

import uuid  # Required for unique book instances


# Create your models here.

class Genre(models.Model):
    name = models.CharField(max_length=200, help_text="Enter a book genre (e.g. Science Fiction, French Poetry etc.)")

    def __str__(self):
        return self.name


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def get_absolute_url(self):
        return reverse('author-detail', args=[str(self.id)])

    def __str__(self):
        return '%s, %s' % (self.last_name, self.first_name)


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)
    summary = models.TextField(max_length=1000, help_text="Enter a brief description of the book")
    isbn = models.CharField('ISBN', max_length=13,
                            help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>')
    genre = models.ManyToManyField(Genre, help_text="Select a genre for this book")
    image = models.ImageField(default='book_default.jpg', upload_to='books_pics')
    rating = models.FloatField(default=0)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book-detail', args=[str(self.id)])

    def get_enabled_star(self):
        return range(int(self.rating))

    def get_disabled_star(self):
        disabled_star = 5 - int(self.rating)
        if float(int(self.rating)) - self.rating != 0.0:
            disabled_star = 4 - int(self.rating)
        print(disabled_star)
        return range(disabled_star)

    def is_half_star_active(self):
        return True if float(int(self.rating)) - self.rating != 0.0 else False


class BookInstance(models.Model):
    book = models.ForeignKey(Book, on_delete=models.SET_NULL, null=True)
    imprint = models.CharField(max_length=200)
    on_loan_start = models.DateField(null=True, blank=True)
    on_loan_end = models.DateField(null=True, blank=True)
    due_back = models.DateField(null=True, blank=True)
    on_loan_duration = models.IntegerField(default=4, null=False, help_text="Months")
    created_date = models.DateTimeField(default=timezone.now)

    LOAN_STATUS = (
        ('m', 'Maintenance'),
        ('o', 'On loan'),
        ('a', 'Available'),
        ('r', 'Reserved'),
    )

    status = models.CharField(max_length=1, choices=LOAN_STATUS, blank=True, default='m', help_text='Book availability')

    class Meta:
        ordering = ["due_back"]

    def __str__(self):
        return '%s (%s)' % (self.id, self.book.title)

    def get_cost(self):
        return (datetime.datetime.today().date() - self.on_loan_end).days * 2.53

    def get_days_expired(self):
        return (datetime.datetime.today().date() - self.on_loan_end).days


class Opinion(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='opinions')
    rating = models.IntegerField(default=5)

    class Meta:
        ordering = ['-date_posted']

    def __str__(self):
        return f'Opinion: {self.title}, by {self.author.username}'
