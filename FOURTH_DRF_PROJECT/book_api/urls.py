from django.urls import path
from .views import *

urlpatterns = [

    path('', BookAPI.as_view()),  # endpoint: api/books
    path('/<int:id>', BookAPI.as_view()), # endpoint: api/books/{id}

    # path('authors', AuthorAPI.as_view()),
    # path('authors/<int:id>', AuthorAPI.as_view()),

    # path('publications', PublicationAPI.as_view()),
    # path('publications/<int:id>', PublicationAPI.as_view()),

    
]
