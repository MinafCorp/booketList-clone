from django.urls import path, include
from manajemen_buku.views import add_books_ajax, delete_books_ajax, get_books, get_books_json, hide_books_ajax, manajemen_buku
from manajemen_buku.views import manajemen_buku
from manajemen_buku.views import get_books_json, add_books_ajax


app_name = 'manajemen_buku'

urlpatterns = [
    path('', manajemen_buku, name='manajemen_buku'),
    path('create-item-ajax/', add_books_ajax, name='add_books_ajax'),
    path('delete-item-ajax/<int:item_id>/', delete_books_ajax, name='delete_books_ajax'),
    path('get-books-ajax/', get_books_json, name='get_books_json'),
    path('delete-books-ajax/<int:item_id>/', delete_books_ajax, name='delete_books_ajax'),
    path('create-books-ajax/', add_books_ajax, name='add_books_ajax'),
    path('hide-books-ajax/<int:item_id>/', hide_books_ajax, name='hide_books_ajax'),
    path('get-books/', get_books, name='get_books'),

    
]