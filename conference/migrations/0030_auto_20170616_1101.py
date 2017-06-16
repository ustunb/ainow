# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2017-06-16 10:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conference', '0029_standingcommittee'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendee',
            name='three_words',
            field=models.CharField(blank=True, help_text=b'Three words to describe your work', max_length=1024),
        ),
        migrations.AddField(
            model_name='organiser',
            name='three_words',
            field=models.CharField(blank=True, help_text=b'Three words to describe your work', max_length=1024),
        ),
        migrations.AddField(
            model_name='speaker',
            name='three_words',
            field=models.CharField(blank=True, help_text=b'Three words to describe your work', max_length=1024),
        ),
        migrations.AddField(
            model_name='standingcommittee',
            name='three_words',
            field=models.CharField(blank=True, help_text=b'Three words to describe your work', max_length=1024),
        ),
    ]
