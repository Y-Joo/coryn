# Generated by Django 3.2.5 on 2021-08-24 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20210824_1520'),
    ]

    operations = [
        migrations.AddField(
            model_name='coin',
            name='coin_newss',
            field=models.ManyToManyField(to='core.CoinNews'),
        ),
    ]
