# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-01-17 12:25
from __future__ import unicode_literals

from django.db import migrations
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields
import wagtail.wagtailimages.blocks
import wagtailblocks_cards.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('team_rooster', '0003_auto_20180112_1428'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teamrooster',
            name='team_name',
        ),
        migrations.AlterField(
            model_name='teamrooster',
            name='staff',
            field=wagtail.wagtailcore.fields.StreamField((('staff', wagtailblocks_cards.blocks.CardsBlock(wagtail.wagtailcore.blocks.StructBlock((('photo', wagtail.wagtailimages.blocks.ImageChooserBlock(required=False)), ('name', wagtail.wagtailcore.blocks.CharBlock(required=True)), ('vorname', wagtail.wagtailcore.blocks.CharBlock(required=True)), ('position', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[('headcouch', 'Headcouch'), ('assistenz', 'Assistenz-Coach'), ('betreuer', 'Betreuer')], icon='cup')))), icon='plus')),), blank=True),
        ),
    ]