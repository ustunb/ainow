# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2017-03-07 16:51
from __future__ import unicode_literals

import cms.blocks
from django.db import migrations
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields
import wagtail.wagtailimages.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='researchpage',
            name='content',
            field=wagtail.wagtailcore.fields.StreamField([('heading', cms.blocks.HeadingBlock()), ('text', cms.blocks.TextBlock()), ('links', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock([(b'title', cms.blocks.HeadingBlock()), (b'subtitle', wagtail.wagtailcore.blocks.CharBlock()), (b'description', wagtail.wagtailcore.blocks.RichTextBlock()), (b'thumbnail', wagtail.wagtailimages.blocks.ImageChooserBlock(required=False)), (b'page', wagtail.wagtailcore.blocks.PageChooserBlock(required=False)), (b'external_link', wagtail.wagtailcore.blocks.URLBlock(required=False))]), icon='link', template='cms/blocks/featured_links.html')), ('divider', cms.blocks.DividerBlock())], default=[]),
        ),
    ]
