# Generated by Django 3.2.3 on 2021-06-04 08:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0003_alter_book_published'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='slud',
            new_name='slug',
        ),
    ]