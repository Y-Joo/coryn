from rest_framework import serializers
from core.models import CoinNews


class CoinNewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoinNews
        fields = '__all__'
