# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Message'
        db.create_table(u'core_message', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('text', self.gf('django.db.models.fields.CharField')(max_length=1000)),
            ('author', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('date', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'core', ['Message'])

        # Adding model 'Order'
        db.create_table(u'core_order', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('text', self.gf('django.db.models.fields.CharField')(max_length=1000)),
            ('comment', self.gf('django.db.models.fields.CharField')(default='', max_length=500, blank=True)),
            ('crypto_order', self.gf('django.db.models.fields.related.OneToOneField')(related_name='order', unique=True, to=orm['django_cryptocoin.CryptoOrder'])),
        ))
        db.send_create_signal(u'core', ['Order'])


    def backwards(self, orm):
        # Deleting model 'Message'
        db.delete_table(u'core_message')

        # Deleting model 'Order'
        db.delete_table(u'core_order')


    models = {
        u'core.message': {
            'Meta': {'object_name': 'Message'},
            'author': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'date': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'text': ('django.db.models.fields.CharField', [], {'max_length': '1000'})
        },
        u'core.order': {
            'Meta': {'object_name': 'Order'},
            'comment': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '500', 'blank': 'True'}),
            'crypto_order': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'order'", 'unique': 'True', 'to': u"orm['django_cryptocoin.CryptoOrder']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'text': ('django.db.models.fields.CharField', [], {'max_length': '1000'})
        },
        u'django_cryptocoin.cryptoorder': {
            'Meta': {'object_name': 'CryptoOrder'},
            'addr': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'amount': ('django.db.models.fields.DecimalField', [], {'max_digits': '18', 'decimal_places': '8'}),
            'amount_received': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '18', 'decimal_places': '8'}),
            'amount_received_confirmed': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '18', 'decimal_places': '8'}),
            'currency': ('django.db.models.fields.CharField', [], {'default': "'btc'", 'max_length': '50'}),
            'date': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'processed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'redirect_to': ('django.db.models.fields.CharField', [], {'default': "'/'", 'max_length': '200'})
        }
    }

    complete_apps = ['core']