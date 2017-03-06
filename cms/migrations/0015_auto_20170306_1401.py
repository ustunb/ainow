# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2017-03-06 14:01
from __future__ import unicode_literals

from django.db import migrations
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0014_auto_20170306_1212'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homepage',
            name='features',
        ),
        migrations.RemoveField(
            model_name='homepage',
            name='mission',
        ),
        migrations.RemoveField(
            model_name='homepage',
            name='themes',
        ),
        migrations.AddField(
            model_name='homepage',
            name='content',
            field=wagtail.wagtailcore.fields.StreamField([('mission', wagtail.wagtailcore.blocks.RichTextBlock(icon='edit')), ('heading', wagtail.wagtailcore.blocks.CharBlock(icon='title')), ('features', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock([('heading', wagtail.wagtailcore.blocks.CharBlock(required=True)), ('text', wagtail.wagtailcore.blocks.RichTextBlock()), ('links', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock([('text', wagtail.wagtailcore.blocks.CharBlock(required=True)), ('page', wagtail.wagtailcore.blocks.PageChooserBlock())], template='cms/blocks/link.html')))], icon='doc-full'), icon='list-ul', template='cms/blocks/features.html')), ('columns', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock([('heading', wagtail.wagtailcore.blocks.CharBlock(required=True)), ('text', wagtail.wagtailcore.blocks.RichTextBlock())], icon='doc-full'), icon='list-ul', template='cms/blocks/columns.html'))], default=[]),
        ),
    ]
