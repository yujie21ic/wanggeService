# Generated by Django 2.0.4 on 2018-05-07 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0004_auto_20180505_1936'),
    ]

    operations = [
        migrations.AddField(
            model_name='stockcode',
            name='decimalpoint',
            field=models.SmallIntegerField(default=2, verbose_name='价格小数位数'),
        ),
        migrations.AddField(
            model_name='stockcode',
            name='volunit',
            field=models.IntegerField(default=100, verbose_name='每次交易最小成交单位'),
        ),
    ]
