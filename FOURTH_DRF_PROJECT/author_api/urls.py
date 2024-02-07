from django.urls import path
from .views import *

urlpatterns = [

    path('', AuthorAPI.as_view()),  # endpoint: api/authors
    path('/<int:id>', AuthorAPI.as_view()), # endpoint: api/authors/{id}
    
]
