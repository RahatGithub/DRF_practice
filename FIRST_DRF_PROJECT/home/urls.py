from django.urls import path, include
# from django.urls import re_path
from .views import *

urlpatterns = [
    path('books', BooksAPI.as_view(), name='list_all_books'),
    path('books/<int:id>', BooksAPI.as_view(), name='fetch_a_book'),
    # re_path(r'^books/$', search_book, name='search_book'),
]