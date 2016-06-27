# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('publications', '0002_publication_featured_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='publication',
            name='featured',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='publication',
            name='featured_image',
            field=models.ImageField(null=True, upload_to=b'images/plants', blank=True),
            preserve_default=True,
        ),
    ]
