# Generated by Django 3.2.5 on 2021-08-24 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_remove_coin_coin_news'),
    ]

    operations = [
        migrations.AddField(
            model_name='coin',
            name='coin_news',
            field=models.ManyToManyField(to='core.CoinNews'),
        ),
    ]
