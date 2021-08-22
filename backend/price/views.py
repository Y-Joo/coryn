from django.http import JsonResponse
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import CoinPriceSerializer
from core.models import Coin
from core.models import CoinPrice
from core.modules.get_price import get_current_price
from core.modules import get_minute_candle


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


class CoinCandleMinuteView(APIView):

    def get(self, request, unit, coin_ticker):
        obj = Coin.objects.get(ticker=coin_ticker)
        queryset = CoinPrice.objects.get(coin_id=obj.__dict__['id'])
        serializer_class = CoinPriceSerializer(queryset)

        high = serializer_class.data['minute_high']
        low = serializer_class.data['minute_low']
        open = serializer_class.data['minute_open']
        close = serializer_class.data['minute_close']


        return JsonResponse({'high': high, 'low': low, 'open': open, 'close': close}, safe=False)

    def put(self, request, unit):
        queryset = Coin.objects.all().values("ticker", "id")

        coin_candles = get_minute_candle(queryset)
        coins = CoinPrice.objects.all()
        coin_price_serializer = CoinPriceSerializer(coins, coin_candles, many=True, partial=True)
        if coin_price_serializer.is_valid():
            coin_price_serializer.save()
        return Response(status=status.HTTP_200_OK)