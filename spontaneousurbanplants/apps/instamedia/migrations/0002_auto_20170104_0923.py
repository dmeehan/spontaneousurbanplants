# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('instamedia', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instagramimage',
            name='created',
            field=models.DateTimeField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='instagramimage',
            name='last_synced',
            field=models.DateTimeField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='instagramimage',
            name='remote_id',
            field=models.CharField(max_length=255, unique=True, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='instagramimage',
            name='remote_low_resolution_url',
            field=models.URLField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='instagramimage',
            name='remote_standard_resolution_url',
            field=models.URLField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='instagramimage',
            name='remote_thumbnail_url',
            field=models.URLField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='instagramimage',
            name='updated',
            field=models.DateTimeField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
