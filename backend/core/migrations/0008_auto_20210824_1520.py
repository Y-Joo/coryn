# Generated by Django 3.2.5 on 2021-08-24 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_delete_coincoinnews'),
    ]

    operations = [
        migrations.CreateModel(
            name='CoinCoinNews',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('coin_id', models.BigIntegerField()),
                ('coin_news_id', models.BigIntegerField()),
            ],
            options={
                'db_table': 'coin_coin_news',
            },
        ),
        migrations.RemoveField(
            model_name='coin',
            name='coin_news',
        ),
    ]
