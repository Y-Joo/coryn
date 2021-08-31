from django.urls import path
from . import views

urlpatterns = [
    path('now/', views.CoinPriceView.as_view()),
    path('candle/minute/', views.CoinCandleMinuteView.as_view()),
    path('candle/hour/', views.CoinCandleHourView.as_view()),
    path('candle/day/', views.CoinCandleDayView.as_view()),
    path('candle/week/', views.CoinCandleWeekView.as_view()),
    path('candle/minute/<str:coin_ticker>/', views.CoinCandleMinuteView.as_view()),
    path('candle/hour/<str:coin_ticker>/', views.CoinCandleHourView.as_view()),
    path('candle/day/<str:coin_ticker>/', views.CoinCandleDayView.as_view()),
    path('candle/week/<str:coin_ticker>/', views.CoinCandleWeekView.as_view()),
]
