# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('publications', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='publication',
            name='featured_image',
            field=models.ImageField(null=True, upload_to=b'images/publications', blank=True),
            preserve_default=True,
        ),
    ]
