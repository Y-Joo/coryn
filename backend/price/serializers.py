from rest_framework import serializers
from core.models import CoinPrice


class CoinPriceListSerializer(serializers.ListSerializer):
    def update(self, instance, validated_data):
        # Maps for id->instance and id->data item.
        coin_mapping = {coin.coin: coin for coin in instance}
        data_mapping = {item['coin']: item for item in validated_data}

        # Perform creations and updates.
        ret = []
        for coin_id, data in data_mapping.items():
            coin = coin_mapping.get(coin_id, None)
            if coin is None:
                ret.append(self.child.create(data))
            else:
                ret.append(self.child.update(coin, data))

        # Perform deletions.
        for coin_id, coin in coin_mapping.items():
            if coin_id not in data_mapping:
                coin.delete()
        return ret


class CoinPriceSerializer(serializers.ModelSerializer):
    class Meta:
        list_serializer_class = CoinPriceListSerializer
        model = CoinPrice
        fields = '__all__'
