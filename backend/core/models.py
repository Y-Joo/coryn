from django.db import models


class CoinNews(models.Model):
    id = models.BigAutoField(primary_key=True)
    type = models.IntegerField()
    title = models.TextField(blank=True, null=True)
    source = models.TextField(blank=True, null=True)
    link = models.TextField(blank=True, null=True, unique=True)
    upload_date = models.DateTimeField(blank=True, null=True)
    release_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'coin_news'


class Coin(models.Model):
    id = models.BigAutoField(primary_key=True)
    coin_name = models.CharField(blank=True, null=True, max_length=100)
    kr_name = models.CharField(blank=True, null=True, max_length=100)
    ticker = models.CharField(blank=True, null=True, max_length=100)

    coin_newses = models.ManyToManyField(CoinNews)

    class Meta:
        db_table = 'coin'


class CoinPrice(models.Model):
    id = models.BigAutoField(primary_key=True)
    price = models.DecimalField(decimal_places=2, null=True, max_digits=20)
    day_change = models.DecimalField(decimal_places=2, null=True, max_digits=20)
    minute_high = models.TextField(blank=True, null=True)
    minute_low = models.TextField(blank=True, null=True)
    minute_open = models.TextField(blank=True, null=True)
    minute_close = models.TextField(blank=True, null=True)
    hour_high = models.TextField(blank=True, null=True)
    hour_low = models.TextField(blank=True, null=True)
    hour_open = models.TextField(blank=True, null=True)
    hour_close = models.TextField(blank=True, null=True)
    day_high = models.TextField(blank=True, null=True)
    day_low = models.TextField(blank=True, null=True)
    day_open = models.TextField(blank=True, null=True)
    day_close = models.TextField(blank=True, null=True)
    week_high = models.TextField(blank=True, null=True)
    week_low = models.TextField(blank=True, null=True)
    week_open = models.TextField(blank=True, null=True)
    week_close = models.TextField(blank=True, null=True)
    coin = models.ForeignKey(Coin, related_name='coin_price', on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = 'coin_price'
