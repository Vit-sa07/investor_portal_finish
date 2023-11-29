from django.urls import path
from .views import CryptListView, CryptDetailView, CoinLoreTickerView

urlpatterns = [
    path("", CryptListView.as_view(), name="crypt-list"),
    path("<int:pk>/", CryptDetailView.as_view(), name="crypt-detail"),
    path("coinlore/tickers/", CoinLoreTickerView.as_view(), name='coinlore-tickers'),
]
