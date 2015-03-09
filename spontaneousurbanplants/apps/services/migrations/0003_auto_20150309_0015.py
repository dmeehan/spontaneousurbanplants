# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0002_service_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='text',
            field=models.TextField(blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='service',
            name='text_html',
            field=models.TextField(editable=False, blank=True),
            preserve_default=True,
        ),
    ]
