# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2017-03-06 10:22
from __future__ import unicode_literals

from django.db import migrations
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0010_auto_20170220_1525'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='mission',
            field=wagtail.wagtailcore.fields.RichTextField(blank=True),
        ),
    ]
