from django.http import JsonResponse
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import CoinNewsSerializer
from core.models import Coin
from core.models import CoinNews
from core.modules.news.crawler_google import CrawlerGoogle
from core.modules.news import crawler_coinmarketcal


class CoinNewsView(APIView):
    def put(self, request):
        coin_name_list = Coin.objects.all().values('coin_name', 'id')
        crawler = CrawlerGoogle()
        queryset, coin_id_list = crawler.get_coin_news_from_coin_names(coin_name_list)
        for item, coin_id in zip(queryset, coin_id_list):
            serializer_class = CoinNewsSerializer(data=item, partial=True)
            if serializer_class.is_valid():
                serializer_class.save()
                coin = Coin.objects.get(id=coin_id)
                coin_news = CoinNews.objects.get(link=item['link'])
                coin.coin_newses.add(coin_news)
                print('save!')
            else:
                print(serializer_class.errors)
                print('not save!')
        return Response(status=status.HTTP_200_OK)

    def get(self, request):
        queryset = CoinNews.objects.all()
        serializer_class = CoinNewsSerializer(data=queryset, many=True)
        serializer_class.is_valid()
        return JsonResponse(serializer_class.data, safe=False)


class CoinGoodNewsView(APIView):
    def put(self, request):
        coin_name_list = Coin.objects.all().values('coin_name', 'id')
        queryset, coin_id_list = crawler_coinmarketcal(coin_name_list)
        for item, coin_id in zip(queryset, coin_id_list):
            serializer_class = CoinNewsSerializer(data=item, partial=True)
            if serializer_class.is_valid():
                serializer_class.save()
                coin = Coin.objects.get(id=coin_id)
                coin_news = CoinNews.objects.get(link=item['link'])
                coin.coin_newses.add(coin_news)
                print('save!')
            else:
                print(serializer_class.errors)
                print('not save!')
        return Response(status=status.HTTP_200_OK)
