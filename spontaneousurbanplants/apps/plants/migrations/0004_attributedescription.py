# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('plants', '0003_auto_20150228_1742'),
    ]

    operations = [
        migrations.CreateModel(
            name='AttributeDescription',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.TextField(blank=True)),
                ('visible', models.BooleanField(default=True)),
                ('attribute', models.ForeignKey(to='plants.Attribute')),
                ('plant', models.ForeignKey(to='plants.Plant')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
