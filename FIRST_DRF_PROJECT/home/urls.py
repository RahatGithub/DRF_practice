from django.urls import path, include
from django.urls import re_path
from .views import *

urlpatterns = [
    path('books/', BooksAPI.as_view()),
    re_path(r'^books/$', search_book),
]


