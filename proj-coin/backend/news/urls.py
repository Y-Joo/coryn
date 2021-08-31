from django.urls import path
from . import views

urlpatterns = [
    path('', views.CoinNewsView.as_view()),
    path('good/', views.CoinGoodNewsView.as_view())
]
