# flake8: noqa
# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'RedactorText.redactor_settings'
        db.add_column('cmsplugin_redactortext', 'redactor_settings',
                      self.gf('django.db.models.fields.TextField')(default='{     buttons: [\'formatting\',  \'bold\', \'italic\', \'deleted\',     \'unorderedlist\', \'orderedlist\', \'outdent\', \'indent\',     \'image\', \'video\', \'file\', \'table\', \'link\', \'alignment\',     \'horizontalrule\'],     toolbarFixed: true,     toolbarFixedBox: true,     toolbarExternal: \'[data-id="redactor-toolbar"]\',     imageUpload: image_upload_url,     imageGetJson: image_get_json_url }\' '),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'RedactorText.redactor_settings'
        db.delete_column('cmsplugin_redactortext', 'redactor_settings')


    models = {
        'cms.cmsplugin': {
            'Meta': {'object_name': 'CMSPlugin'},
            'changed_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 8, 15, 0, 0)'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '15', 'db_index': 'True'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.CMSPlugin']", 'null': 'True', 'blank': 'True'}),
            'placeholder': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.Placeholder']", 'null': 'True'}),
            'plugin_type': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'}),
            'position': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
        },
        'cms.placeholder': {
            'Meta': {'object_name': 'Placeholder'},
            'default_width': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slot': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'})
        },
        'djangocms_text_redactor.redactortext': {
            'Meta': {'object_name': 'RedactorText', 'db_table': "'cmsplugin_redactortext'", '_ormbases': ['cms.CMSPlugin']},
            'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'content': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'redactor_settings': ('django.db.models.fields.TextField', [], {'default': '\'{     buttons: [\\\'formatting\\\',  \\\'bold\\\', \\\'italic\\\', \\\'deleted\\\',     \\\'unorderedlist\\\', \\\'orderedlist\\\', \\\'outdent\\\', \\\'indent\\\',     \\\'image\\\', \\\'video\\\', \\\'file\\\', \\\'table\\\', \\\'link\\\', \\\'alignment\\\',     \\\'horizontalrule\\\'],     toolbarFixed: true,     toolbarFixedBox: true,     toolbarExternal: \\\'[data-id="redactor-toolbar"]\\\',     imageUpload: image_upload_url,     imageGetJson: image_get_json_url }\\\' \''})
        }
    }

    complete_apps = ['djangocms_text_redactor']
