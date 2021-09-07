from rest_framework import serializers
from core.models import Coin
from core.models import CoinNews
from core.models import CoinCoinNewses


class CoinCoinNewsesSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoinCoinNewses
        fields = '__all__'


class CoinNewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoinNews
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        try:
            coin_coin_newses = CoinCoinNewses.objects.filter(coinnews=representation['id'])
            coin_coin_newses_serializer = CoinCoinNewsesSerializer(data=coin_coin_newses, many=True)
            coin_coin_newses_serializer.is_valid()
            coins = []
            for coin_coin_news in coin_coin_newses_serializer.data:
                coin = Coin.objects.get(id=coin_coin_news['coin'])
                print(coin)
                coins.append(coin.coin_name)
            representation['coins'] = coins
        except Exception as e:
            representation['coins'] = []

        return representation