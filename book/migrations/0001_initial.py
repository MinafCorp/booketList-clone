# Generated by Django 4.2.6 on 2023-10-26 03:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('ISBN', models.IntegerField(blank=True, null=True, unique=True)),
                ('title', models.TextField(blank=True, null=True, verbose_name='Book-Title')),
                ('author', models.TextField(blank=True, null=True, verbose_name='Book-Author')),
                ('year_of_publication', models.IntegerField(blank=True, null=True, verbose_name='Year-Of-Publication')),
                ('publisher', models.TextField(blank=True, null=True)),
                ('image_url_s', models.URLField(blank=True, null=True, verbose_name='Image-URL-S')),
                ('image_url_m', models.URLField(blank=True, null=True, verbose_name='Image-URL-M')),
                ('image_url_l', models.URLField(blank=True, null=True, verbose_name='Image-URL-L')),
            ],
        ),
    ]