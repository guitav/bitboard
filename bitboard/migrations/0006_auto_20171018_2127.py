# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-18 21:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bitboard', '0005_auto_20171018_2101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cryptocompare',
            name='fully_premined',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='cryptocompare',
            name='pre_mined_valued',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='cryptocompare',
            name='sponsored',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='cryptocompare',
            name='total_coins_free_float',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
