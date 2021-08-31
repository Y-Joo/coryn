from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.CoinListView.as_view()),
    path('detail/<str:coin_ticker>/', views.CoinDetailView.as_view())
]