# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import positions.fields


class Migration(migrations.Migration):

    dependencies = [
        ('instamedia', '0001_initial'),
        ('plants', '0001_initial'),
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
                'verbose_name_plural': 'categories',
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='plant',
            name='images',
        ),
        migrations.AddField(
            model_name='plant',
            name='carbon',
            field=models.FloatField(help_text=b'CO2 sequestration per plant in pounds', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='plant',
            name='categories',
            field=models.ManyToManyField(to='plants.Category', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='plant',
            name='energy',
            field=models.FloatField(help_text=b'Energy savings per plant in kWh', null=True, blank=True),
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
            name='lead_image',
            field=models.ForeignKey(blank=True, to='instamedia.InstagramImage', null=True),
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
            name='seasonality_chart',
            field=models.ImageField(null=True, upload_to=b'images/plants', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='plant',
            name='stormwater',
            field=models.FloatField(help_text=b'Stormwater retention per plant in gallons', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='attribute',
            name='hashtag',
            field=models.CharField(help_text=b'A unique hashtag indentifying this attribute. Do not include #.', unique=True, max_length=255),
            preserve_default=True,
        ),
    ]
