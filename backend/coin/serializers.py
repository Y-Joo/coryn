from rest_framework import serializers
from core.models import Coin
from core.models import CoinPrice
from core.models import CoinNews


class CoinPriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoinPrice
        fields = '__all__'


class CoinNewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoinNews
        fields = '__all__'


class CoinSerializer(serializers.ModelSerializer):
    coin_price = CoinPriceSerializer(many=True)
    coin_news = CoinNewsSerializer(many=True)

    class Meta:
        model = Coin
        fields = '__all__'