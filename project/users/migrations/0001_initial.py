# Generated by Django 2.2.17 on 2021-01-16 18:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='default.jpg', upload_to='profile_pics')),
                ('favourite_book', models.CharField(default='', max_length=150)),
                ('favourite_genre', models.CharField(default='', max_length=150)),
                ('mobile_phone', models.CharField(default='', max_length=9)),
                ('book_list', models.ManyToManyField(blank=True, to='books.BookInstance')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
