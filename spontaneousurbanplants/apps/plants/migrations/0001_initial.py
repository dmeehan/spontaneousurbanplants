# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Attribute'
        db.create_table(u'plants_attribute', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('hashtag', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('icon', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal(u'plants', ['Attribute'])

        # Adding model 'Plant'
        db.create_table(u'plants_plant', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('latin_name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('common_name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('hashtag', self.gf('django.db.models.fields.CharField')(unique=True, max_length=100)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('icon', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal(u'plants', ['Plant'])

        # Adding M2M table for field attributes on 'Plant'
        m2m_table_name = db.shorten_name(u'plants_plant_attributes')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('plant', models.ForeignKey(orm[u'plants.plant'], null=False)),
            ('attribute', models.ForeignKey(orm[u'plants.attribute'], null=False))
        ))
        db.create_unique(m2m_table_name, ['plant_id', 'attribute_id'])


    def backwards(self, orm):
        # Deleting model 'Attribute'
        db.delete_table(u'plants_attribute')

        # Deleting model 'Plant'
        db.delete_table(u'plants_plant')

        # Removing M2M table for field attributes on 'Plant'
        db.delete_table(db.shorten_name(u'plants_plant_attributes'))


    models = {
        u'plants.attribute': {
            'Meta': {'object_name': 'Attribute'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'hashtag': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'icon': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
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