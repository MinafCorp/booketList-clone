from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from user.models import Reader
from .models import Wishlist
from book.models import Book
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist
from .forms import WishlistSearchForm

@login_required
def add_to_wishlist(request, book_id):
    if request.method == "POST":
        try:
            book = Book.objects.get(pk=book_id)
            reader = request.user.reader
            wishlist, created = Wishlist.objects.get_or_create(pengguna=reader)
            if book not in wishlist.buku.all():
                wishlist.buku.add(book)
                return JsonResponse({"success": True, "message": "Berhasil ditambahkan ke wishlist"}, status=200)
            else:
                wishlist.buku.remove(book)
                return JsonResponse({"success": True, "message": "Berhasil dihapus dari wishlist"}, status=200)
        except Book.DoesNotExist:
            return JsonResponse({"success": False, "message": "Buku tidak ditemukan"}, status=404)
        except Reader.DoesNotExist:
            return JsonResponse({"success": False, "message": "Pengguna tidak ditemukan"}, status=404)
    return JsonResponse({"success": False, "message": "Error"}, status=400)

def show_wishlist(request):
    reader_instance = Reader.objects.get(user=request.user)
    wishlist_instance = Wishlist.objects.get(pengguna=reader_instance)
    wishlisted_books = wishlist_instance.buku.all()
    return render(request, 'wishlist.html', {'wishlist_books': wishlisted_books})

@login_required(login_url="user:login")
def delete_wishlist_book(request, book_id):
    if request.method == 'POST':
        try:
            reader_instance = Reader.objects.get(user=request.user)
            # Ambil objek wishlist yang berhubungan dengan user yang sedang login
            wishlist = Wishlist.objects.get(pengguna=reader_instance)
            
            # Cari buku yang ingin dihapus berdasarkan book_id
            book_to_remove = Book.objects.get(pk=book_id)
            
            # Hapus buku dari wishlist
            wishlist.buku.remove(book_to_remove)
            
            return JsonResponse({'status': 'ok'})
        except ObjectDoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Object not found'}, status=404)
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=500)
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=400)


@login_required
def search_wishlist(request):
    form = WishlistSearchForm(request.GET)
    if form.is_valid():
        title_search = form.cleaned_data['bookTitleSearch']
        year_filter = form.cleaned_data['yearFilter']
        reader = request.user.reader

        # Dapatkan buku yang ada di wishlist user yang sedang login
        user_wishlist_books = Wishlist.objects.filter(pengguna=reader).values_list('buku', flat=True)
        books = Book.objects.filter(pk__in=user_wishlist_books, title__icontains=title_search)

        if year_filter == '<1990':
            books = books.filter(year_of_publication__lt=1990)
        elif year_filter == '1990-2000':
            books = books.filter(year_of_publication__gte=1990, year_of_publication__lte=2000)
        elif year_filter == '>2000':
            books = books.filter(year_of_publication__gt=2000)

        books_data = [
            {
                'pk': book.pk,
                'title': book.title,
                'image_url_l': book.image_url_l,
                'author': book.author,
                'year': book.year_of_publication,
            }
            for book in books
        ]
        return JsonResponse({'books': books_data})
    return JsonResponse({'error': 'Invalid form submission'}, status=400)

