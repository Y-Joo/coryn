from django.http import JsonResponse
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import CoinNewsSerializer
from core.models import Coin
from core.models import CoinNews
from core.modules.crawl_google import CrawlerGoogle


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