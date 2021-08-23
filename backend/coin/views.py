from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.shortcuts import get_list_or_404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import CoinSerializer
from core.models import Coin
from core.modules.get_coin_list import crawl_coin_name


class CoinListView(APIView):
    def get(self, request):
        queryset = get_list_or_404(Coin)
        serializer_class = CoinSerializer(data=queryset, many=True, partial=True)
        serializer_class.is_valid()
        return JsonResponse(serializer_class.data, safe=False)

    def put(self, request):
        coins = crawl_coin_name()
        for coin in coins:
            _coin = get_object_or_404(Coin, ticker=coin['ticker'])
            if not _coin:
                coin_serializer = CoinSerializer(data=coin, partial=True)
            else:
                coin_serializer = CoinSerializer(_coin, coin, partial=True)
            if coin_serializer.is_valid():
                coin_serializer.save()
        return Response(status=status.HTTP_200_OK)


class CoinDetailView(APIView):
    def get(self, request, coin_ticker):
        queryset = Coin.objects.filter(ticker=coin_ticker)
        serializer_class = CoinSerializer(data=queryset, many=True, partial=True)
        serializer_class.is_valid()
        return JsonResponse(serializer_class.data, safe=False)
