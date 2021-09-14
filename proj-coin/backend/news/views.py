from django.http import JsonResponse
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import CoinNewsSerializer
from core.models import Coin
from core.models import CoinNews
from core.modules.news.crawler_google import CrawlerGoogle
from core.modules.news.crawler_coinmarketcal import CrawlerCoinMarketCal
import collections

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
                coin = Coin.objects.get(id=coin_id)
                coin_news = CoinNews.objects.get(link=item['link'])
                coin.coin_newses.add(coin_news)
                print(serializer_class.errors)
                print('not save!')
        return Response(status=status.HTTP_200_OK)

    def get(self, request):
        queryset = CoinNews.objects.all().order_by('-upload_date')[:100]
        serializer_class = CoinNewsSerializer(data=queryset, many=True)
        serializer_class.is_valid()
        return JsonResponse(serializer_class.data, safe=False)

    def delete(self, request):
        CoinNews.objects.all().delete()
        return Response(status=status.HTTP_200_OK)


class CoinGoodNewsView(APIView):
    def put(self, request):
        coin_name_list = Coin.objects.all().values('ticker', 'id')
        coin_dict = collections.defaultdict()
        for item in coin_name_list:
            coin_dict[item['ticker'].split('-')[1]] = item['id']
        crawler = CrawlerCoinMarketCal(coin_dict)
        queryset, coin_id_list = crawler.get_coin_news_list()
        for item, coin_id in zip(queryset, coin_id_list):
            serializer_class = CoinNewsSerializer(data=item, partial=True)
            if serializer_class.is_valid():
                serializer_class.save()
                coin = Coin.objects.get(id=coin_id)
                coin_news = CoinNews.objects.get(link=item['link'])
                coin.coin_newses.add(coin_news)
                print('save!')
            else:
                coin = Coin.objects.get(id=coin_id)
                coin_news = CoinNews.objects.get(link=item['link'])
                coin.coin_newses.add(coin_news)
                print(serializer_class.errors)
                print('not save!')
        return Response(status=status.HTTP_200_OK)

    def get(self, request):
        queryset = CoinNews.objects.filter(type=1)
        serializer_class = CoinNewsSerializer(data=queryset, many=True)
        serializer_class.is_valid()
        return JsonResponse(serializer_class.data, safe=False)
