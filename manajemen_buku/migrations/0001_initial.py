# Generated by Django 4.2.6 on 2023-10-29 08:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Publish',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ISBN', models.IntegerField(blank=True, null=True, unique=True)),
                ('title', models.TextField(blank=True, null=True, verbose_name='Book-Title')),
                ('author', models.TextField(blank=True, null=True)),
                ('year_of_publication', models.IntegerField(blank=True, null=True, verbose_name='Year-Of-Publication')),
                ('publisher', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='book_images/')),
                ('authorUser', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='user.author')),
            ],
        ),
    ]