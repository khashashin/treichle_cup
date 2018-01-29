# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-01-28 10:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0040_page_draft_title'),
        ('home', '0003_homepage_teams_page'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homepage',
            name='teams_page',
        ),
        migrations.AddField(
            model_name='homepage',
            name='matches_section',
            field=models.ForeignKey(blank=True, help_text='Choose a page to link to for the Matches Page', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.Page', verbose_name='Choose '),
        ),
        migrations.AddField(
            model_name='homepage',
            name='matches_section_title',
            field=models.CharField(blank=True, help_text='Title to display above the next matches', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='news_section',
            field=models.ForeignKey(blank=True, help_text='Choose a page to link to for the News Page.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.Page', verbose_name='News'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='news_section_title',
            field=models.CharField(blank=True, help_text='Title to display above the News section on Home page', max_length=255, null=True),
        ),
    ]