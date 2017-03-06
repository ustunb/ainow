# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2017-03-06 12:12
from __future__ import unicode_literals

from django.db import migrations
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0013_auto_20170306_1200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='themes',
            field=wagtail.wagtailcore.fields.StreamField([('heading', wagtail.wagtailcore.blocks.CharBlock()), ('theme', wagtail.wagtailcore.blocks.StructBlock([('heading', wagtail.wagtailcore.blocks.CharBlock(required=True)), ('text', wagtail.wagtailcore.blocks.RichTextBlock())]))], default=[]),
        ),
    ]
