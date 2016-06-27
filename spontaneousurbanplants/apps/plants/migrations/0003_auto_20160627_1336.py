# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('plants', '0002_auto_20150314_1924'),
    ]

    operations = [
        migrations.AddField(
            model_name='plant',
            name='featured',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='plant',
            name='featured_image',
            field=models.ImageField(null=True, upload_to=b'images/plants', blank=True),
            preserve_default=True,
        ),
    ]
