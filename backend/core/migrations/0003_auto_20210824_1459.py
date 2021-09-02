# Generated by Django 3.2.5 on 2021-08-24 05:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20210823_1545'),
    ]

    operations = [
        migrations.AddField(
            model_name='coin',
            name='coin_news',
            field=models.ManyToManyField(to='core.CoinNews'),
        ),
        migrations.AddField(
            model_name='coinprice',
            name='coin',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='coin_price', to='core.coin'),
        ),
        migrations.AlterField(
            model_name='coinnews',
            name='link',
            field=models.TextField(blank=True, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='coinprice',
            name='day_change',
            field=models.DecimalField(decimal_places=2, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='coinprice',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=20, null=True),
        ),
    ]