from django.urls import path
import views

urlpatterns = [
    path('list/', views.CoinListView.as_view()),
    path('detail/<str:coin_ticker>/', views.CoinDetailView.as_view())
]