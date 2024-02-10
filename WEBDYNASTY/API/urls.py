from django.urls import path
from .views import *

urlpatterns = [
    path('users', CreateUserView.as_view()),

    path('stations', StationView.as_view()),
    path('stations/<int:id>/trains', StationTrainView.as_view()),

    path('wallets/<int:id>', WalletView.as_view()),

    path('trains', CreateTrainView.as_view()),

    path('tickets', CreateTicketView.as_view()),

]