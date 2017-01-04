# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('instamedia', '0002_auto_20170104_0923'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instagramimage',
            name='remote_id',
            field=models.CharField(max_length=255, null=True, blank=True),
            preserve_default=True,
        ),
    ]
