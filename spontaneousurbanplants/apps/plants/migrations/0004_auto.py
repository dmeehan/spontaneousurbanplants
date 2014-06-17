# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding M2M table for field images on 'Plant'
        m2m_table_name = db.shorten_name(u'plants_plant_images')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('plant', models.ForeignKey(orm[u'plants.plant'], null=False)),
            ('instagramimage', models.ForeignKey(orm[u'instamedia.instagramimage'], null=False))
        ))
        db.create_unique(m2m_table_name, ['plant_id', 'instagramimage_id'])


    def backwards(self, orm):
        # Removing M2M table for field images on 'Plant'
        db.delete_table(db.shorten_name(u'plants_plant_images'))


    models = {
        u'instamedia.instagramimage': {
            'Meta': {'ordering': "['-updated']", 'object_name': 'InstagramImage'},
            'caption': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'coordinates': ('django.contrib.gis.db.models.fields.PointField', [], {'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image_file': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'last_synced': ('django.db.models.fields.DateTimeField', [], {}),
            'location_id': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'location_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'raw_tags': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'remote_id': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'remote_low_resolution_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'remote_standard_resolution_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'remote_thumbnail_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['instamedia.InstagramTag']", 'null': 'True', 'blank': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'verified': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        u'instamedia.instagramtag': {
            'Meta': {'object_name': 'InstagramTag'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'moderate': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'subscribe': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'subscription_id': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'sync': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        },
        u'plants.attribute': {
            'Meta': {'ordering': "['order']", 'object_name': 'Attribute'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'hashtag': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'icon': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'order': ('django.db.models.fields.IntegerField', [], {'default': '-1'}),
            'visible': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        },
        u'plants.plant': {
            'Meta': {'object_name': 'Plant'},
            'attributes': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['plants.Attribute']", 'null': 'True', 'blank': 'True'}),
            'common_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'hashtag': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'icon': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'images': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['instamedia.InstagramImage']", 'null': 'True', 'blank': 'True'}),
            'latin_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'order': ('django.db.models.fields.IntegerField', [], {'default': '-1'}),
            'visible': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        }
    }

    complete_apps = ['plants']