# Generated by Django 3.0.5 on 2021-01-20 21:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0006_auto_20210120_2213'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookrental',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.BookInstance'),
        ),
    ]