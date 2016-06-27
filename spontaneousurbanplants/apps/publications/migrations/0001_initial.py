# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import positions.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Publication',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255)),
                ('subtitle', models.CharField(max_length=255, blank=True)),
                ('author', models.CharField(max_length=255, blank=True)),
                ('coauthor', models.CharField(max_length=255, blank=True)),
                ('description', models.TextField(blank=True)),
                ('product_detail', models.TextField(blank=True)),
                ('image', models.ImageField(null=True, upload_to=b'images/publications', blank=True)),
                ('purchase_link', models.URLField(max_length=255, blank=True)),
                ('facebook_link', models.URLField(max_length=255, blank=True)),
                ('twitter_link', models.URLField(max_length=255, blank=True)),
                ('instagram_link', models.URLField(max_length=255, blank=True)),
                ('slug', models.SlugField()),
                ('description_html', models.TextField(editable=False, blank=True)),
                ('product_detail_html', models.TextField(editable=False, blank=True)),
                ('order', positions.fields.PositionField(default=-1)),
            ],
            options={
                'ordering': ['order'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PublicationLink',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255, blank=True)),
                ('url', models.URLField(max_length=255)),
                ('order', positions.fields.PositionField(default=-1)),
                ('publication', models.ForeignKey(to='publications.Publication')),
            ],
            options={
                'ordering': ['order'],
            },
            bases=(models.Model,),
        ),
    ]
