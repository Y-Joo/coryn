# Generated by Django 3.2.5 on 2021-08-24 07:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_remove_coinnews_coin_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coin',
            name='coin_newses',
        ),
        migrations.AddField(
            model_name='coinnews',
            name='coin',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='core.coin'),
        ),
    ]
