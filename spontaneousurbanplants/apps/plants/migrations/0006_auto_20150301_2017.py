# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('plants', '0005_remove_plant_images'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['order']},
        ),
        migrations.AlterField(
            model_name='plant',
            name='carbon',
            field=models.FloatField(help_text=b'CO2 sequestration per plant in pounds', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='plant',
            name='energy',
            field=models.FloatField(help_text=b'Energy savings per plant in kWh', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='plant',
            name='stormwater',
            field=models.FloatField(help_text=b'Stormwater retention per plant in gallons', null=True, blank=True),
            preserve_default=True,
        ),
    ]
