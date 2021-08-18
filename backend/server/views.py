import json
from django.http import JsonResponse
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import CoinSerializer, CoinPriceSerializer, CoinNewsSerializer,CoinPriceListSerializer
from .models import Coin, CoinNews, CoinPrice
from server.modules.get_coin_list import crawl_coin_name
from server.modules.get_price import get_current_price
from server.modules.get_candle import get_minute_candle, get_hour_candle, get_day_candle, get_week_candle
from server.modules.crawl_google import CrawlerGoogle


class CoinListView(APIView):
    @staticmethod
    def get_object(tic):
        try:
            return Coin.objects.get(ticker=tic)
        except Coin.DoesNotExist:
            return None

    def get(self, request):
        print('get coin List')
        queryset = Coin.objects.all()
        serializer_class = CoinSerializer(data=queryset, many=True, partial=True)
        serializer_class.is_valid()
        return JsonResponse(serializer_class.data, safe=False)

    def put(self, request):
        print('put coin List')
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


class CoinPriceView(APIView):
    @staticmethod
    def get_object(pk):
        try:
            return CoinPrice.objects.get(coin_id=pk)
        except CoinPrice.DoesNotExist:
            return None

    def put(self, request):
        queryset = Coin.objects.all().values("ticker", "id", "coin_price__day_open")
        price_list = get_current_price(queryset)
        current_prices = CoinPrice.objects.all()

        coin_price_serializer = CoinPriceSerializer(current_prices, price_list, partial=True, many=True)
        if coin_price_serializer.is_valid():
            coin_price_serializer.save()
            print('save!')

        return Response(status=status.HTTP_200_OK)


class CoinCandleView(APIView):
    @staticmethod
    def get_object(pk):
        try:
            return CoinPrice.objects.get(coin_id=pk)
        except CoinPrice.DoesNotExist:
            return None

    def get(self, request, unit, coin_ticker):
        obj = Coin.objects.get(ticker=coin_ticker)
        queryset = CoinPrice.objects.get(coin_id=obj.__dict__['id'])
        serializer_class = CoinPriceSerializer(queryset)
        if unit == 'minute':
            high = serializer_class.data['minute_high']
            low = serializer_class.data['minute_low']
            open = serializer_class.data['minute_open']
            close = serializer_class.data['minute_close']
        elif unit == 'hour':
            high = serializer_class.data['hour_high']
            low = serializer_class.data['hour_low']
            open = serializer_class.data['hour_open']
            close = serializer_class.data['hour_close']
        elif unit == 'day':
            high = serializer_class.data['day_high']
            low = serializer_class.data['day_low']
            open = serializer_class.data['day_open']
            close = serializer_class.data['day_close']
        elif unit == 'week':
            high = serializer_class.data['week_high']
            low = serializer_class.data['week_low']
            open = serializer_class.data['week_open']
            close = serializer_class.data['week_close']

        return JsonResponse({'high': high, 'low': low, 'open': open, 'close': close}, safe=False)

    def put(self, request, unit):
        queryset = Coin.objects.all().values("ticker", "id")
        if unit == 'minute':
            coin_candles = get_minute_candle(queryset)
        elif unit == 'hour':
            coin_candles = get_hour_candle(queryset)
        elif unit == 'day':
            coin_candles = get_day_candle(queryset)
        elif unit == 'week':
            coin_candles = get_week_candle(queryset)
        coins = CoinPrice.objects.all()
        coin_price_serializer = CoinPriceSerializer(coins, coin_candles, many=True, partial=True)
        if coin_price_serializer.is_valid():
            coin_price_serializer.save()
        return Response(status=status.HTTP_200_OK)


class CoinDetailView(APIView):
    def get(self, request, coin_ticker):
        queryset = Coin.objects.filter(ticker=coin_ticker)
        serializer_class = CoinSerializer(data=queryset, many=True, partial=True)
        serializer_class.is_valid()
        return JsonResponse(serializer_class.data, safe=False)


class CoinNewsView(APIView):
    def put(self, request):
        coin_name_list = Coin.objects.all().values('coin_name', 'id')
        crawler = CrawlerGoogle()
        queryset = crawler.crawl_coin_list(coin_name_list)
        serializer_class = CoinNewsSerializer(data=queryset, many=True, partial=True)
        if serializer_class.is_valid():
            serializer_class.save()
            print('save!')
        else:
            print(serializer_class.errors)
        return Response(status=status.HTTP_200_OK)

    def get(self, request):
        queryset = CoinNews.objects.all()
        serializer_class = CoinNewsSerializer(data=queryset, many=True)
        serializer_class.is_valid()
        return JsonResponse(serializer_class.data, safe=False)

