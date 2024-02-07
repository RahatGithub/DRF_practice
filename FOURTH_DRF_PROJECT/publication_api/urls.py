from django.urls import path
from .views import *

urlpatterns = [

    path('', PublicationAPI.as_view()),  # endpoint: api/publications
    path('/<int:id>', PublicationAPI.as_view()), # endpoint: api/publications/{id}
    
]
