from django.urls import path
from .views import *

urlpatterns = [

    path('', BookAPI.as_view()),  # endpoint: api/books
    path('/<int:id>', BookAPI.as_view()), # endpoint: api/books/{id}

]
