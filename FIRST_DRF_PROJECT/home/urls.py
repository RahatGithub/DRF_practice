from django.urls import path, include
from django.urls import re_path
from .views import *

urlpatterns = [
    # path('api/books', home, name="book-list"), 
    # path('books', search_book, name="search-book"),
    path('books', BooksAPI.as_view()),
    # re_path(r'^books/\?author=([^\&]+)&sort=([^\&]+)&order=(asc|desc)&limit=(\d+)$', search_book),
    # re_path(r'^books/\?author=([^\&]+)', search_book)
    re_path(r'^books/$', search_book),
]
