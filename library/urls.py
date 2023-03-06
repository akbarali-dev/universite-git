from django.urls import path
from .views import books_list, book_detail, book_create

urlpatterns = [
    path('', books_list, name="books"),
    path('byid/<int:pk>/', book_detail, name="bookById"),
    path('create/', book_create, name="book_create"),
]
