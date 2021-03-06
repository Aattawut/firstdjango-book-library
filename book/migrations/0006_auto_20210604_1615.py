# Generated by Django 3.2.3 on 2021-06-04 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0005_bookcomment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='author',
            options={'verbose_name_plural': 'Author'},
        ),
        migrations.AlterModelOptions(
            name='book',
            options={'ordering': ['-created'], 'verbose_name_plural': 'Book'},
        ),
        migrations.AlterModelOptions(
            name='bookcomment',
            options={'ordering': ['id'], 'verbose_name_plural': 'Book Comment'},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Category'},
        ),
        migrations.AddField(
            model_name='book',
            name='level',
            field=models.CharField(blank=True, choices=[('B', 'Basic'), ('M', 'Medium'), ('A', 'advance')], max_length=5, null=True),
        ),
    ]
