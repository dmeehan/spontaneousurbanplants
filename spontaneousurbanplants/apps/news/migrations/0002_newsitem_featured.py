# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsitem',
            name='featured',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
