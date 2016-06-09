# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-02 13:16
from __future__ import unicode_literals

from django.db import migrations, models
import markitup.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FAQPage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(help_text=b'Used to make a nice url for the page that displays this.')),
                ('name', models.CharField(blank=True, help_text=b'An internal name for this page, to help identify it.', max_length=1024)),
                ('title', models.CharField(max_length=1024)),
                ('introduction', markitup.fields.MarkupField(blank=True, no_rendered_field=True)),
                ('_introduction_rendered', models.TextField(blank=True, editable=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='FAQQuestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('question', models.CharField(max_length=1024)),
                ('answer', markitup.fields.MarkupField(no_rendered_field=True)),
                ('_answer_rendered', models.TextField(blank=True, editable=False)),
                ('pages', models.ManyToManyField(blank=True, related_name='questions', to='faq.FAQPage')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]