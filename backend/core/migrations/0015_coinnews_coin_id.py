# Generated by Django 3.2.5 on 2021-08-24 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_delete_coincoinnews'),
    ]

    operations = [
        migrations.AddField(
            model_name='coinnews',
            name='coin_id',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
    ]