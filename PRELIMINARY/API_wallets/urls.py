from django.urls import path
from .views import *

urlpatterns = [
    path('<int:id>', WalletView.as_view()), # api/wallets/{wallet_id}
    
]
