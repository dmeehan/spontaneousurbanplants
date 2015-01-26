# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='InstagramImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('remote_id', models.CharField(unique=True, max_length=255)),
                ('caption', models.TextField(blank=True)),
                ('raw_tags', models.TextField(verbose_name=b'remote tags', blank=True)),
                ('username', models.CharField(max_length=255, null=True, blank=True)),
                ('remote_thumbnail_url', models.URLField(blank=True)),
                ('remote_low_resolution_url', models.URLField(blank=True)),
                ('remote_standard_resolution_url', models.URLField(blank=True)),
                ('location_name', models.CharField(max_length=255, blank=True)),
                ('location_id', models.IntegerField(null=True, blank=True)),
                ('coordinates', django.contrib.gis.db.models.fields.PointField(srid=4326, null=True, blank=True)),
                ('created', models.DateTimeField()),
                ('updated', models.DateTimeField()),
                ('last_synced', models.DateTimeField()),
                ('verified', models.BooleanField(default=False)),
                ('image_file', models.ImageField(null=True, upload_to=b'images/instagram', blank=True)),
            ],
            options={
                'ordering': ['-updated'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='InstagramTag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('sync', models.BooleanField(default=True, help_text=b'Sync existing instagram images with this tag to local database.')),
                ('subscribe', models.BooleanField(default=False, help_text=b'Subscribe to realtime updates for this tag.')),
                ('moderate', models.BooleanField(default=True, help_text=b'If true, new images will default to unverified.')),
                ('subscription_id', models.IntegerField(null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='instagramimage',
            name='tags',
            field=models.ManyToManyField(to='instamedia.InstagramTag', null=True, blank=True),
            preserve_default=True,
        ),
    ]
