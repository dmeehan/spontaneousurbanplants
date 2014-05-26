# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Attribute.order'
        db.add_column(u'plants_attribute', 'order',
                      self.gf('django.db.models.fields.IntegerField')(default=-1),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Attribute.order'
        db.delete_column(u'plants_attribute', 'order')


    models = {
        u'plants.attribute': {
            'Meta': {'object_name': 'Attribute'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'hashtag': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'icon': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'order': ('django.db.models.fields.IntegerField', [], {'default': '-1'})
        },
        u'plants.plant': {
            'Meta': {'object_name': 'Plant'},
            'attributes': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['plants.Attribute']", 'null': 'True', 'blank': 'True'}),
            'common_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'hashtag': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'icon': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latin_name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['plants']