from django.urls import path
from .views import *

urlpatterns = [

    # handling POST BOOKS, FETCH ALL BOOKS and SEARCH BOOKS
    path('books', BookAPI.as_view(), name='all_books'),
    
    # handling FETCH A BOOK and UPDATE A BOOK 
    path('books/<int:id>', BookAPI.as_view(), name='book_details'),

    
]
