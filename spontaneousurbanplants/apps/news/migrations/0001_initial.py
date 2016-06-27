# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
import positions.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NewsItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255)),
                ('excerpt', models.TextField(blank=True)),
                ('body', models.TextField()),
                ('excerpt_html', models.TextField(editable=False, blank=True)),
                ('body_html', models.TextField(editable=False, blank=True)),
                ('date_published', models.DateTimeField(default=datetime.datetime.now)),
                ('slug', models.SlugField(unique_for_date=b'date_published')),
                ('status', models.PositiveSmallIntegerField(default=3, help_text=b'Only content with published status will be publicly displayed.', choices=[(1, b'Published'), (2, b'Hidden'), (3, b'Draft')])),
            ],
            options={
                'ordering': ['-date_published'],
                'get_latest_by': 'date_published',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='NewsItemImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image_file', models.ImageField(upload_to=b'images/news')),
                ('title', models.CharField(max_length=255, blank=True)),
                ('caption', models.TextField(null=True, blank=True)),
                ('visible', models.BooleanField(default=True, help_text=b'This image is publicly available.')),
                ('order', positions.fields.PositionField(default=-1)),
                ('is_main', models.BooleanField(default=False, verbose_name=b'Main image')),
                ('news_item', models.ForeignKey(to='news.NewsItem')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
