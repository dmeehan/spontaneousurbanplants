# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_newsitem_featured'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsitem',
            name='featured_image',
            field=models.ImageField(null=True, upload_to=b'images/news', blank=True),
            preserve_default=True,
        ),
    ]
