from rest_framework import serializers
from core.models import CoinNews


class CoinNewsListSerializer(serializers.ListSerializer):
    def update(self, instance, validated_data):
        # Maps for id->instance and id->data item.
        coin_mapping = {coin.link: coin for coin in instance}
        data_mapping = {item['link']: item for item in validated_data}

        # Perform creations and updates.
        ret = []
        for link, data in data_mapping.items():
            coin = coin_mapping.get(link, None)
            if coin is None:
                ret.append(self.child.create(data))
            else:
                ret.append(self.child.update(coin, data))

        # Perform deletions.
        for link, coin in coin_mapping.items():
            if link not in data_mapping:
                coin.delete()
        return ret


class CoinNewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoinNews
        fields = '__all__'
