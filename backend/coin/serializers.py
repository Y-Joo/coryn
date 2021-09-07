from rest_framework import serializers
from core.models import Coin
from core.models import CoinPrice
from core.models import CoinNews


class CoinPriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoinPrice
        fields = '__all__'


class CoinCurrentPriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoinPrice
        fields = ['price', 'day_change']


class CoinNewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoinNews
        fields = '__all__'


class CoinSerializer(serializers.ModelSerializer):
    coin_price = CoinPriceSerializer(many=True)
    coin_newses = CoinNewsSerializer(many=True)

    class Meta:
        model = Coin
        fields = '__all__'


class CoinListSerializer(serializers.ModelSerializer):
    coin_price = CoinCurrentPriceSerializer(many=True)

    class Meta:
        model = Coin
        fields = '__all__'
