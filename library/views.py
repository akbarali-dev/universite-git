from django.shortcuts import render, redirect
from .models import Book
from .forms import BookForm


def book_detail(request, pk):
    try:
        book = Book.objects.get(pk=pk)
        # if book.count > 0:

        return render(request, "library/book.html", {
            "book": book,
            "check": book is None
        })

    except:
        return render(request, "library/book.html", {
            "check": True
        }, status=404)


def books_list(request):
    search = request.GET.get("search")
    if search is None:
        books = Book.objects.all()
    else:
        books = Book.objects.filter(tite__contains=search)
    return render(request, "library/books.html", {
        "books": books,
        "search": search
    })


def book_create(request):
    if request.method == 'GET':
        form = BookForm()
    else:
        form = BookForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Book.objects.create(
                tite=data["title"],
                author=data["author"],
                count=data["count"],
            )
        return redirect("books")

    return render(request, "library/book-create.html", {
        "form": form,
    })
