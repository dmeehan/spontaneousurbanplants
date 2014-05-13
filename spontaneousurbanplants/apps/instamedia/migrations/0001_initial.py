# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'InstagramImage'
        db.create_table(u'instamedia_instagramimage', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('remote_id', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255)),
            ('caption', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('raw_tags', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('remote_thumbnail_url', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('remote_low_resolution_url', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('remote_standard_resolution_url', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('location_name', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('location_id', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('coordinates', self.gf('django.contrib.gis.db.models.fields.PointField')(null=True, blank=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')()),
            ('updated', self.gf('django.db.models.fields.DateTimeField')()),
            ('last_synced', self.gf('django.db.models.fields.DateTimeField')()),
            ('verified', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('image_file', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal(u'instamedia', ['InstagramImage'])

        # Adding M2M table for field tags on 'InstagramImage'
        m2m_table_name = db.shorten_name(u'instamedia_instagramimage_tags')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('instagramimage', models.ForeignKey(orm[u'instamedia.instagramimage'], null=False)),
            ('instagramtag', models.ForeignKey(orm[u'instamedia.instagramtag'], null=False))
        ))
        db.create_unique(m2m_table_name, ['instagramimage_id', 'instagramtag_id'])

        # Adding model 'InstagramTag'
        db.create_table(u'instamedia_instagramtag', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('sync', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('subscribe', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('moderate', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('subscription_id', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'instamedia', ['InstagramTag'])


    def backwards(self, orm):
        # Deleting model 'InstagramImage'
        db.delete_table(u'instamedia_instagramimage')

        # Removing M2M table for field tags on 'InstagramImage'
        db.delete_table(db.shorten_name(u'instamedia_instagramimage_tags'))

        # Deleting model 'InstagramTag'
        db.delete_table(u'instamedia_instagramtag')


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
        }
    }

    complete_apps = ['instamedia']