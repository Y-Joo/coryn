# Generated by Django 3.2.5 on 2021-08-24 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0019_coin_coin_newses'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coinnews',
            name='link',
            field=models.CharField(blank=True, max_length=255, null=True, unique=True),
        ),
    ]