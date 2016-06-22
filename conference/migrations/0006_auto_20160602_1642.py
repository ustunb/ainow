# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-02 15:42
from __future__ import unicode_literals

import autoslug.fields
import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('conference', '0005_auto_20160531_1732'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendee',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2016, 6, 2, 15, 42, 26, 893150, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='attendee',
            name='updated',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2016, 6, 2, 15, 42, 31, 788666, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='presentation',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2016, 6, 2, 15, 42, 33, 532947, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='presentation',
            name='updated',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2016, 6, 2, 15, 42, 35, 261047, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='schedule',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2016, 6, 2, 15, 42, 36, 837118, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='schedule',
            name='updated',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2016, 6, 2, 15, 42, 38, 332693, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='speaker',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2016, 6, 2, 15, 42, 39, 829105, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='speaker',
            name='updated',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2016, 6, 2, 15, 42, 41, 651659, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='attendee',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=True, help_text=b'Used to make a nice url for the page that displays this person.', populate_from=b'name', unique=True),
        ),
        migrations.AlterField(
            model_name='presentation',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=True, help_text=b'Used to make a nice url for the page that displays this presentation.', populate_from=b'title', unique=True),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=True, help_text=b'Used to make a nice url for the page that displays this schedule.', populate_from=b'name', unique=True),
        ),
        migrations.AlterField(
            model_name='speaker',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=True, help_text=b'Used to make a nice url for the page that displays this person.', populate_from=b'name', unique=True),
        ),
    ]
