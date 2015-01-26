# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import positions.fields


class Migration(migrations.Migration):

    dependencies = [
        ('instamedia', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attribute',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('hashtag', models.CharField(help_text=b'A unique hashtag indentifying this plant. Do not include #.', unique=True, max_length=255)),
                ('description', models.TextField(blank=True)),
                ('icon', models.ImageField(null=True, upload_to=b'images/icons', blank=True)),
                ('visible', models.BooleanField(default=True)),
                ('order', positions.fields.PositionField(default=-1)),
            ],
            options={
                'ordering': ['order'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Plant',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('latin_name', models.CharField(max_length=255)),
                ('common_name', models.CharField(max_length=255)),
                ('hashtag', models.CharField(help_text=b'A unique hashtag indentifying this plant. Do not include #.', unique=True, max_length=100)),
                ('description', models.TextField(blank=True)),
                ('icon', models.ImageField(null=True, upload_to=b'images/icons', blank=True)),
                ('visible', models.BooleanField(default=True)),
                ('order', positions.fields.PositionField(default=-1)),
                ('attributes', models.ManyToManyField(to='plants.Attribute', null=True, blank=True)),
                ('images', models.ManyToManyField(to='instamedia.InstagramImage', null=True, blank=True)),
            ],
            options={
                'ordering': ['order', 'latin_name'],
            },
            bases=(models.Model,),
        ),
    ]
