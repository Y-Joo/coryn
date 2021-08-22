from django.urls import path
import views

urlpatterns = [
    path('now/', views.CoinPriceView.as_view()),
    path('candle/minute/<str:coin_ticker>/', views.CoinCandleView.as_view()),
    path('candle/hour/<str:coin_ticker>/', views.CoinCandleView.as_view()),
    path('candle/day/<str:coin_ticker>/', views.CoinCandleView.as_view()),
    path('candle/week/<str:coin_ticker>/', views.CoinCandleView.as_view()),
]
