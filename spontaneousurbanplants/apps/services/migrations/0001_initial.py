# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import positions.fields


class Migration(migrations.Migration):

    dependencies = [
        ('plants', '0007_auto_20150301_2023'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('order', positions.fields.PositionField(default=-1)),
                ('attribute', models.ForeignKey(to='plants.Attribute')),
            ],
            options={
                'ordering': ['order'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ServicesContent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255)),
                ('text', models.TextField(blank=True)),
                ('text_html', models.TextField(editable=False, blank=True)),
                ('visible', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'services text',
                'verbose_name_plural': 'services text',
            },
            bases=(models.Model,),
        ),
    ]
