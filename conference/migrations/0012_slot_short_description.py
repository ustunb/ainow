# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-14 07:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conference', '0011_auto_20160614_0851'),
    ]

    operations = [
        migrations.AddField(
            model_name='slot',
            name='short_description',
            field=models.TextField(blank=True, help_text=b"Extra text to display under this slot's name in the  schedule. Useful if you need a description but don't want to associate a whole presentation with it."),
        ),
    ]
