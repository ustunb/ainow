# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2016-11-17 15:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conference', '0032_remove_organiser_organiser_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='presentation',
            name='slide_link',
            field=models.URLField(blank=True, help_text=b"The URL for the presentation's slides.<br>If it can be embded then we will otherwise a link will be displayed", max_length=1024),
        ),
    ]
