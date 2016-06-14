# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-14 07:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conference', '0009_auto_20160610_1138'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slot',
            name='kind',
            field=models.CharField(choices=[(b'BREAKFAST', b'Breakfast and registration'), (b'COFFEE', b'Coffee & Snack Break'), (b'LUNCH', b'Lunch'), (b'TALK', b'Talk'), (b'OTHER', b'Other')], max_length=100),
        ),
    ]