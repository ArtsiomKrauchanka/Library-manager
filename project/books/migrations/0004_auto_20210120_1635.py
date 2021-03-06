# Generated by Django 3.1.5 on 2021-01-20 15:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('books', '0003_auto_20210118_0213'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bookinstance',
            options={'ordering': ['created_date']},
        ),
        migrations.RemoveField(
            model_name='bookinstance',
            name='due_back',
        ),
        migrations.RemoveField(
            model_name='bookinstance',
            name='on_loan_duration',
        ),
        migrations.RemoveField(
            model_name='bookinstance',
            name='on_loan_end',
        ),
        migrations.RemoveField(
            model_name='bookinstance',
            name='on_loan_start',
        ),
        migrations.AlterField(
            model_name='bookinstance',
            name='status',
            field=models.CharField(blank=True, choices=[('M', 'Maintenance'), ('O', 'On loan'), ('A', 'Available'), ('R', 'Reserved')], default='M', help_text='Book availability', max_length=11),
        ),
        migrations.AlterField(
            model_name='genre',
            name='name',
            field=models.CharField(help_text='Enter a book genre (e.g. Science Fiction, French Poetry etc.)', max_length=200, unique=True),
        ),
        migrations.CreateModel(
            name='BookReservation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reservation_date', models.DateField(auto_now_add=True)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.bookinstance')),
                ('booker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['reservation_date'],
            },
        ),
        migrations.CreateModel(
            name='BookRental',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('on_loan_start', models.DateField(auto_now_add=True)),
                ('on_loan_duration', models.IntegerField(default=4, help_text='Months')),
                ('on_loan_end', models.DateField(blank=True, null=True)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.bookinstance')),
                ('booker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['on_loan_start'],
            },
        ),
    ]
