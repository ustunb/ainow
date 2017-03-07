# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2017-03-07 16:30
from __future__ import unicode_literals

import cms.blocks
from django.db import migrations, models
import django.db.models.deletion
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields
import wagtail.wagtailimages.blocks


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtaildocs', '0007_merge'),
        ('conference', '0029_standingcommittee'),
        ('wagtailcore', '0032_add_bulk_delete_page_permission'),
        ('wagtailimages', '0016_deprecate_rendition_filter_relation'),
    ]

    operations = [
        migrations.CreateModel(
            name='Events',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('body', wagtail.wagtailcore.fields.RichTextField()),
                ('start', models.DateTimeField(verbose_name='Start date/time')),
                ('end', models.DateTimeField(verbose_name='End date/time')),
                ('location', models.CharField(blank=True, max_length=1024)),
                ('schedule', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='conference.Schedule')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='EventsIndexPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='HomePage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('content', wagtail.wagtailcore.fields.StreamField([('mission', cms.blocks.MissionBlock()), ('heading', cms.blocks.HeadingBlock()), ('divider', cms.blocks.DividerBlock()), ('video', cms.blocks.YouTubeBlock()), ('features', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock([(b'heading', wagtail.wagtailcore.blocks.CharBlock(required=True)), (b'text', wagtail.wagtailcore.blocks.RichTextBlock()), (b'links', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock([(b'text', wagtail.wagtailcore.blocks.CharBlock(required=True)), (b'page', wagtail.wagtailcore.blocks.PageChooserBlock())])))]), icon='list-ul', template='cms/blocks/features.html')), ('columns', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock([(b'heading', wagtail.wagtailcore.blocks.CharBlock(required=True)), (b'text', wagtail.wagtailcore.blocks.RichTextBlock())]), icon='list-ul', template='cms/blocks/columns.html'))], default=[])),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='PeoplePage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('content', wagtail.wagtailcore.fields.StreamField([('heading', cms.blocks.HeadingBlock()), ('text', cms.blocks.TextBlock()), ('people', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock([(b'name', wagtail.wagtailcore.blocks.CharBlock(required=True)), (b'position', wagtail.wagtailcore.blocks.CharBlock()), (b'organisation', wagtail.wagtailcore.blocks.CharBlock()), (b'image', wagtail.wagtailimages.blocks.ImageChooserBlock())]), icon='group', template='cms/blocks/people.html')), ('divider', cms.blocks.DividerBlock())], default=[])),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('position', models.CharField(blank=True, max_length=1024)),
                ('organisation', models.CharField(blank=True, max_length=1024)),
                ('twitter', models.CharField(blank=True, max_length=15)),
                ('body', wagtail.wagtailcore.fields.RichTextField(blank=True)),
                ('image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='wagtailimages.Image')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='Research',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('excerpt', wagtail.wagtailcore.fields.RichTextField(blank=True)),
                ('intro', wagtail.wagtailcore.fields.RichTextField(blank=True)),
                ('external_link', models.URLField(blank=True, verbose_name='External link')),
                ('image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='wagtailimages.Image')),
                ('research_file', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtaildocs.Document')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='ResearchPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('content', wagtail.wagtailcore.fields.StreamField([('heading', cms.blocks.HeadingBlock()), ('text', cms.blocks.TextBlock()), ('links', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock([(b'title', cms.blocks.HeadingBlock()), (b'subtitle', wagtail.wagtailcore.blocks.CharBlock()), (b'description', wagtail.wagtailcore.blocks.RichTextBlock()), (b'thumbnail', wagtail.wagtailimages.blocks.ImageChooserBlock(required=False)), (b'page', wagtail.wagtailcore.blocks.PageChooserBlock()), (b'external_link', wagtail.wagtailcore.blocks.URLBlock())]), icon='link', template='cms/blocks/featured_links.html')), ('divider', cms.blocks.DividerBlock())], default=[])),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='SimplePage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('name', models.CharField(blank=True, help_text='An internal name for this page, to help identify it.', max_length=1024)),
                ('body', wagtail.wagtailcore.fields.RichTextField(blank=True)),
                ('order', models.PositiveIntegerField(default=0)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]
