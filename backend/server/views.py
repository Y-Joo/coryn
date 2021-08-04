from django.http import JsonResponse
from django.shortcuts import render, redirect
from rest_framework import viewsets
from .serializers import CoinSerializer, CoinNewsSerializer, CoinPriceSerializer
from .models import Coin, CoinPrice, CoinNews
from rest_framework import permissions
from .upbit_api_test import crawl_coin_name

class CoinView(viewsets.ModelViewSet):

