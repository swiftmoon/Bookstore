from django.shortcuts import render, redirect, get_object_or_404
from .models import Book
from .forms import BookCreateForm
from django.http import HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator


def index(request):
    shelf = Book.objects.order_by('-id')
    # Set UP paginator
    paginate = Paginator(Book.objects.all(), 4)
    page = request.GET.get('page')
    books = paginate.get_page(page)

    return render(request, 'main/index.html', {'shelf': shelf, 'books': books})


def Upload(request):
    upload = BookCreateForm()
    if request.method == 'POST':
        upload = BookCreateForm(request.POST, request.FILES)
        if upload.is_valid():
            upload.save()
            next_ = request.POST.get('next', '/')
            return HttpResponseRedirect(next_)
    else:
        return render(request, 'main/upload_form.html',
                      {'form': upload}
                      )


def update_book(request, book_id):
    username = get_object_or_404(Book, id=book_id)
    form = BookCreateForm(instance=username)
    if request.method == "POST":
        form = BookCreateForm(request.POST, request.FILES, instance=username)
        if form.is_valid():
            form.save()
            next_ = request.POST.get('next', '/')
            return HttpResponseRedirect(next_)

    return render(request, 'main/upload_form.html',
                  {'form': form}
                  )


def delete_book(request, book_id):
    book_id = int(book_id)
    try:
        book_sel = Book.objects.get(id=book_id)
    except Book.DoesNotExist:
        return redirect('main:index')
    book_sel.delete()
    return redirect('main:index')
