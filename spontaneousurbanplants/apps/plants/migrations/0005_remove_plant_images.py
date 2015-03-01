# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('plants', '0004_attributedescription'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='plant',
            name='images',
        ),
    ]
