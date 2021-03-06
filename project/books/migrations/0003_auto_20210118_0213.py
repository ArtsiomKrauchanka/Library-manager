# Generated by Django 3.0.5 on 2021-01-18 01:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_auto_20210118_0153'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookinstance',
            name='status',
            field=models.CharField(blank=True, choices=[('Maintenance', 'm'), ('On loan', 'o'), ('Available', 'a'), ('Reserved', 'r')], default='Maintenance', help_text='Book availability', max_length=11),
        ),
    ]
