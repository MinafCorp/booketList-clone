# Generated by Django 4.2.6 on 2023-10-28 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0003_auto_20231028_0825'),
        ('wishlist', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wishlist',
            name='buku',
            field=models.ManyToManyField(related_name='wishlists', to='book.book'),
        ),
    ]
