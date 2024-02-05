from django.urls import path
from django.urls import re_path
from .views import *

urlpatterns = [
    # path('books/', BookAPI.as_view(), name='all_books'),
    # path('books/<int:id>', BookAPI.as_view(), name='book_details'),

    # handling both 'books/' and 'books/{id}' 
    re_path(r'^books/(?P<id>\d+)?$', BookAPI.as_view()),  
]
