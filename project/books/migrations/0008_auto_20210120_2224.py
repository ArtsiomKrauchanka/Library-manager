# Generated by Django 3.0.5 on 2021-01-20 21:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0007_auto_20210120_2220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookreservation',
            name='book',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='books.BookInstance'),
        ),
    ]
