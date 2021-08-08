from django.http import JsonResponse
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import CoinSerializer, CoinPriceSerializer, CoinNewsSerializer
from .models import Coin, CoinNews, CoinPrice
from server.modules.get_coin_list import crawl_coin_name
from server.modules.get_price import get_current_price
from server.modules.get_candle import get_minute_candle


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
        queryset = Coin.objects.all()
        serializer_class = CoinSerializer(data=queryset, many=True, partial=True)
        serializer_class.is_valid()
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


class CoinCandleUpdateView(APIView):
    @staticmethod
    def get_object(pk):
        try:
            return CoinPrice.objects.get(coin_id=pk)
        except CoinPrice.DoesNotExist:
            return None

    def get(self, request):
        queryset = Coin.objects.all().values("ticker", "id")
        coin_candles = get_minute_candle(queryset)
        for candles in coin_candles:
            coin = self.get_object(candles['coin'])
            if not coin:
                coin_price_serializer = CoinPriceSerializer(data=candles, partial=True)
            else:
                coin_price_serializer = CoinPriceSerializer(coin, candles, partial=True)
            if coin_price_serializer.is_valid():
                coin_price_serializer.save()
        return Response(status=status.HTTP_200_OK)



