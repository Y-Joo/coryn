from django.http import JsonResponse
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import CoinSerializer, CoinPriceSerializer, CoinNewsSerializer
from .models import Coin, CoinNews, CoinPrice
from server.modules.upbit_api_test import crawl_coin_name, get_current_price


class CoinUpdateView(APIView):
    @staticmethod
    def get_object(tic):
        try:
            return Coin.objects.get(ticker=tic)
        except Coin.DoesNotExist:
            return None

    def get(self, request):
        coins = crawl_coin_name()
        for coin in coins:
            _coin = self.get_object(coin['ticker'])
            if not _coin:
                coin_serializer = CoinSerializer(data=coin, partial=True)
            else:
                coin_serializer = CoinSerializer(_coin, coin, partial=True)
            if coin_serializer.is_valid():
                coin_serializer.save()
        return Response(status=status.HTTP_200_OK)


class CoinListView(APIView):
    def get(self, request):
        queryset = Coin.objects.all().values("kr_name", "ticker", "coin_name", "id")
        serializer_class = CoinSerializer(queryset, many=True, partial=True)
        return JsonResponse(serializer_class.data, safe=False)


class CoinPriceUpdateView(APIView):
    @staticmethod
    def get_object(pk):
        try:
            return CoinPrice.objects.get(coin_id=pk)
        except CoinPrice.DoesNotExist:
            return None

    def get(self, request):
        queryset = Coin.objects.all().values("ticker", "id")
        price_list = get_current_price(queryset)
        for price in price_list:
            coin = self.get_object(price['coin'])
            if not coin:
                coin_price_serializer = CoinPriceSerializer(data=price, partial=True)
            else:
                coin_price_serializer = CoinPriceSerializer(coin, price, partial=True)
            if coin_price_serializer.is_valid():
                coin_price_serializer.save()
        return Response(status=status.HTTP_200_OK)



