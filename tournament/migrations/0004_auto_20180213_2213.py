# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-02-13 21:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tournament', '0003_auto_20180213_2203'),
    ]

    operations = [
        migrations.AlterField(
            model_name='groupstagetournamentmodel',
            name='number',
            field=models.PositiveSmallIntegerField(verbose_name='Match №:'),
        ),
    ]
