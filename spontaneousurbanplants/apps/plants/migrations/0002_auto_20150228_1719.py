# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import positions.fields


class Migration(migrations.Migration):

    dependencies = [
        ('plants', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
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
        migrations.AddField(
            model_name='plant',
            name='categories',
            field=models.ManyToManyField(to='plants.Category', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='attribute',
            name='hashtag',
            field=models.CharField(help_text=b'A unique hashtag indentifying this attribute. Do not include #.', unique=True, max_length=255),
            preserve_default=True,
        ),
    ]
