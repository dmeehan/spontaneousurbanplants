# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('plants', '0002_auto_20150228_1719'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['order'], 'verbose_name_plural': 'categories'},
        ),
        migrations.AddField(
            model_name='plant',
            name='carbon',
            field=models.FloatField(help_text=b'CO2 sequestration in pounds', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='plant',
            name='energy',
            field=models.FloatField(help_text=b'Energy savings in kWh', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='plant',
            name='flowers',
            field=models.TextField(blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='plant',
            name='habitat',
            field=models.TextField(blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='plant',
            name='origin',
            field=models.CharField(max_length=255, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='plant',
            name='stormwater',
            field=models.FloatField(help_text=b'Stormwater retention in gallons', null=True, blank=True),
            preserve_default=True,
        ),
    ]
