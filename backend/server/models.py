# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Coin(models.Model):
    id = models.BigAutoField(primary_key=True)
    coin_name = models.CharField(blank=True, null=True, max_length=100)
    kr_name = models.CharField(blank=True, null=True, max_length=100)
    ticker = models.CharField(blank=True, null=True, max_length=100)

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
    coin = models.ForeignKey(Coin, related_name='coin_price', on_delete=models.CASCADE)

    class Meta:
        db_table = 'coin_price'


class CoinNews(models.Model):
    id = models.BigAutoField(primary_key=True)
    type = models.IntegerField()
    title = models.CharField(blank=True, null=True, max_length=100)
    source = models.CharField(blank=True, null=True, max_length=100)
    link = models.CharField(blank=True, null=True, max_length=100)
    upload_date = models.DateTimeField()
    release_date = models.DateTimeField()

    coin = models.ForeignKey(Coin, related_name="coin_news", on_delete=models.CASCADE)

    class Meta:
        db_table = 'coin_news'
