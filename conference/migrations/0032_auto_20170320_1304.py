# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2017-03-20 13:04
from __future__ import unicode_literals

import autoslug.fields
from django.db import migrations, models
import django.db.models.deletion
import markitup.fields


class Migration(migrations.Migration):

    dependencies = [
        ('conference', '0031_auto_20170228_1231'),
    ]

    operations = [
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(blank=True, help_text=b'Text that will be shown to the user for this session if no presentations are associated with it instead.', max_length=1024)),
                ('slug', autoslug.fields.AutoSlugField(editable=True, help_text=b'Used to make a nice url for the page that displays this session.', populate_from=b'name', unique=True)),
                ('short_description', markitup.fields.MarkupField(blank=True, help_text=b"Extra text to display under this session's name in the  schedule. Useful if you need a description but don't want to associate a whole presentation with it.", no_rendered_field=True)),
                ('kind', models.CharField(choices=[(b'TALK', b'Talk'), (b'OTHER', b'Other')], max_length=100)),
                ('_short_description_rendered', models.TextField(blank=True, editable=False)),
                ('room', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sessions', to='conference.Room')),
            ],
            options={
                'ordering': ['slot__start'],
            },
        ),
        migrations.RemoveField(
            model_name='presentation',
            name='schedule',
        ),
        migrations.RemoveField(
            model_name='presentation',
            name='slot',
        ),
        migrations.RemoveField(
            model_name='slot',
            name='_short_description_rendered',
        ),
        migrations.RemoveField(
            model_name='slot',
            name='kind',
        ),
        migrations.RemoveField(
            model_name='slot',
            name='name',
        ),
        migrations.RemoveField(
            model_name='slot',
            name='room',
        ),
        migrations.RemoveField(
            model_name='slot',
            name='short_description',
        ),
        migrations.AlterField(
            model_name='slot',
            name='schedule',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='slots', to='conference.Schedule'),
        ),
        migrations.AddField(
            model_name='session',
            name='slot',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sessions', to='conference.Slot'),
        ),
        migrations.AddField(
            model_name='presentation',
            name='session',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='session', to='conference.Session'),
        ),
    ]