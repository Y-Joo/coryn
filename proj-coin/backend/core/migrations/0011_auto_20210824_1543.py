# Generated by Django 3.2.5 on 2021-08-24 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_rename_coin_newss_coin_coin_newses'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coincoinnews',
            name='coin_id',
            field=models.BigIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='coincoinnews',
            name='coin_news_id',
            field=models.BigIntegerField(blank=True, null=True),
        ),
    ]