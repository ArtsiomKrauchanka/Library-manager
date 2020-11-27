import uuid
from django.db import models
from django.contrib.auth.models import User
from books.models import BookInstance


class Payment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    book_instance = models.ForeignKey(BookInstance, on_delete=models.SET_NULL, null=True)
    day_exceeded = models.IntegerField()
    value = models.FloatField()

    def __str__(self):
        return f'Payments id:{id} '


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    favourite_book = models.CharField(default='', max_length=150)
    favourite_genre = models.CharField(default='', max_length=150)
    mobile_phone = models.CharField(default='', max_length=9)
    book_list = models.ManyToManyField(BookInstance, blank=True)
    payments = models.ManyToManyField(Payment, blank=True)

    def __str__(self):
        return f'Profile username:{self.user.username} '
