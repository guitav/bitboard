# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-18 21:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bitboard', '0011_auto_20171018_2153'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cryptocompare',
            name='coin_id',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='cryptocompare',
            name='sort_order',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
