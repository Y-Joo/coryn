# Generated by Django 3.2.5 on 2021-08-04 14:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0002_auto_20210804_2332'),
    ]

    operations = [
        migrations.RenameField(
            model_name='coin_news',
            old_name='coin_id',
            new_name='coin',
        ),
        migrations.RenameField(
            model_name='coin_price',
            old_name='coin_id',
            new_name='coin',
        ),
    ]
