# Generated by Django 3.0.5 on 2020-11-27 16:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ebooks', '0002_auto_20201127_1334'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ebook',
            old_name='pdf_download_count',
            new_name='download_count',
        ),
        migrations.RemoveField(
            model_name='ebook',
            name='txt_download_count',
        ),
    ]
