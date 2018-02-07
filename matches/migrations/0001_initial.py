# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-02-05 14:10
from __future__ import unicode_literals

import colorfield.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0040_page_draft_title'),
        ('team_rooster', '0009_auto_20180128_1156'),
    ]

    operations = [
        migrations.CreateModel(
            name='Match',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('match_number', models.PositiveSmallIntegerField()),
                ('team_1_color', colorfield.fields.ColorField(default='#FFFFFF', max_length=18)),
                ('team_1_score', models.PositiveSmallIntegerField()),
                ('team_2_color', colorfield.fields.ColorField(default='#0066ff', max_length=18)),
                ('team_2_score', models.PositiveSmallIntegerField()),
                ('match_starts_at', models.DateTimeField()),
                ('team_1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='team_rooster.TeamRooster')),
                ('team_2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='team_rooster.TeamRooster')),
            ],
            options={
                'verbose_name_plural': 'matches',
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='Matches',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('introduction', models.TextField(blank=True, help_text='Text to describe the page')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]