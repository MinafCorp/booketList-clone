

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('book', '0001_initial'),
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Wishlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('buku', models.ManyToManyField(related_name='wishlists', to='book.book')),
                ('pengguna', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='wishlist', to='user.reader')),
            ],
        ),
    ]
