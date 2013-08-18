# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Migration(SchemaMigration):

    depends_on = (
        ("channels", "0001_initial"),
    )

    def forwards(self, orm):
        # Adding model 'Timeline'
        db.create_table(u'timelinejs_timeline', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('headline', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('type', self.gf('django.db.models.fields.CharField')(default='default', max_length=50)),
            ('start_date', self.gf('django.db.models.fields.DateField')(blank=True)),
            ('text', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('asset_media', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('asset_credit', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('asset_caption', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('json', self.gf('jsonfield.fields.JSONField')(null=True, blank=True)),
            ('source', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
            ('channel', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['channels.Channel'], null=True, on_delete=models.SET_NULL, blank=True)),
        ))
        db.send_create_signal(u'timelinejs', ['Timeline'])

        # Adding model 'TimelineContainer'
        db.create_table(u'timelinejs_timelinecontainer', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('container', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='timelinecontainer_container', null=True, on_delete=models.SET_NULL, to=orm['containers.Container'])),
            ('timeline', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='timelinecontainer_timeline', null=True, on_delete=models.SET_NULL, to=orm['timelinejs.Timeline'])),
        ))
        db.send_create_signal(u'timelinejs', ['TimelineContainer'])

        # Adding model 'TimelineEvent'
        db.create_table(u'timelinejs_timelineevent', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('timeline', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['timelinejs.Timeline'])),
            ('start_date', self.gf('django.db.models.fields.DateField')()),
            ('end_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('headline', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('text', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('asset_media', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('asset_credit', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('asset_caption', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('asset_thumbnail', self.gf('django.db.models.fields.CharField')(max_length=500, null=True, blank=True)),
            ('type', self.gf('django.db.models.fields.CharField')(default='date', max_length=255, null=True, blank=True)),
            ('classname', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('value', self.gf('django.db.models.fields.CharField')(max_length=140, null=True, blank=True)),
            ('tag', self.gf('django.db.models.fields.CharField')(max_length=140, null=True, blank=True)),
        ))
        db.send_create_signal(u'timelinejs', ['TimelineEvent'])

        # Adding model 'TimelineOptions'
        db.create_table(u'timelinejs_timelineoptions', (
            ('timeline', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['timelinejs.Timeline'], unique=True, primary_key=True)),
            ('width', self.gf('django.db.models.fields.CharField')(default='100%', max_length=10)),
            ('height', self.gf('django.db.models.fields.CharField')(default='600', max_length=10)),
            ('embed_id', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
            ('start_at_end', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('start_at_slide', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('start_zoom_adjust', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('hash_bookmark', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('font', self.gf('django.db.models.fields.CharField')(default='Bevan-PotanoSans', max_length=50)),
            ('debug', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('lang', self.gf('django.db.models.fields.CharField')(default='en', max_length=6)),
            ('maptype', self.gf('django.db.models.fields.CharField')(default='watercolor', max_length=50)),
        ))
        db.send_create_signal(u'timelinejs', ['TimelineOptions'])


    def backwards(self, orm):
        # Deleting model 'Timeline'
        db.delete_table(u'timelinejs_timeline')

        # Deleting model 'TimelineContainer'
        db.delete_table(u'timelinejs_timelinecontainer')

        # Deleting model 'TimelineEvent'
        db.delete_table(u'timelinejs_timelineevent')

        # Deleting model 'TimelineOptions'
        db.delete_table(u'timelinejs_timelineoptions')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'%s.%s' % (User._meta.app_label, User._meta.module_name): {
            'Meta': {'object_name': User.__name__},
        },
        u'channels.channel': {
            'Meta': {'ordering': "['name', 'parent__id', 'published']", 'unique_together': "(('site', 'long_slug', 'slug', 'parent'),)", 'object_name': 'Channel'},
            'date_available': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'null': 'True', 'db_index': 'True'}),
            'date_insert': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_update': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'group': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'homepage': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'include_in_main_rss': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'long_slug': ('django.db.models.fields.SlugField', [], {'max_length': '250'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'order': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'parent': ('mptt.fields.TreeForeignKey', [], {'blank': 'True', 'related_name': "'subchannel'", 'null': 'True', 'to': u"orm['channels.Channel']"}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'db_index': 'True'}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'show_in_menu': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': u"orm['sites.Site']"}),
            'site_domain': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'site_iid': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True', 'max_length': '4', 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '150'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['%s.%s']" % (User._meta.app_label, User._meta.object_name)})
        },
        u'containers.container': {
            'Meta': {'ordering': "['-date_available', 'title', 'channel_long_slug']", 'unique_together': "(('site', 'child_class', 'channel_long_slug', 'slug'),)", 'object_name': 'Container'},
            'channel': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['channels.Channel']"}),
            'channel_long_slug': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'channel_name': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '140', 'null': 'True', 'blank': 'True'}),
            'child_app_label': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'child_class': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'child_module': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '120', 'null': 'True', 'blank': 'True'}),
            'date_available': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'null': 'True', 'db_index': 'True'}),
            'date_insert': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_update': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'hat': ('django.db.models.fields.CharField', [], {'max_length': '140', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'images': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['images.Image']", 'null': 'True', 'through': u"orm['containers.ContainerImage']", 'blank': 'True'}),
            'main_image': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'containers_container_mainimage'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': u"orm['images.Image']"}),
            'main_image_caption': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'db_index': 'True'}),
            'short_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'show_on_root_channel': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': u"orm['sites.Site']"}),
            'site_domain': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'site_iid': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True', 'max_length': '4', 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '150'}),
            'sources': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['sources.Source']", 'null': 'True', 'through': u"orm['containers.ContainerSource']", 'blank': 'True'}),
            'tags': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '4000', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '140', 'db_index': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['%s.%s']" % (User._meta.app_label, User._meta.object_name)})
        },
        u'containers.containerimage': {
            'Meta': {'ordering': "('order',)", 'object_name': 'ContainerImage'},
            'caption': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'container': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['containers.Container']", 'null': 'True', 'on_delete': 'models.SET_NULL', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['images.Image']", 'null': 'True', 'on_delete': 'models.SET_NULL', 'blank': 'True'}),
            'order': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'})
        },
        u'containers.containersource': {
            'Meta': {'ordering': "('order',)", 'object_name': 'ContainerSource'},
            'container': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['containers.Container']", 'null': 'True', 'on_delete': 'models.SET_NULL', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'source': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'containersource_sources'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': u"orm['sources.Source']"})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'images.image': {
            'Meta': {'object_name': 'Image'},
            'archive': ('django.db.models.fields.files.FileField', [], {'max_length': '255'}),
            'crop_example': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'crop_x1': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'crop_x2': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'crop_y1': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'crop_y2': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'date_available': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'null': 'True', 'db_index': 'True'}),
            'date_insert': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_update': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'fit_in': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'flip': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'flop': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'halign': ('django.db.models.fields.CharField', [], {'default': 'False', 'max_length': '6', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'db_index': 'True'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': u"orm['sites.Site']"}),
            'site_domain': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'site_iid': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True', 'max_length': '4', 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '150'}),
            'smart': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'source': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sources.Source']", 'null': 'True', 'blank': 'True'}),
            'tags': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '4000', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '140', 'db_index': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['%s.%s']" % (User._meta.app_label, User._meta.object_name)}),
            'valign': ('django.db.models.fields.CharField', [], {'default': 'False', 'max_length': '6', 'null': 'True', 'blank': 'True'})
        },
        u'sites.site': {
            'Meta': {'ordering': "('domain',)", 'object_name': 'Site', 'db_table': "'django_site'"},
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'sources.source': {
            'Meta': {'unique_together': "(('site', 'slug'),)", 'object_name': 'Source'},
            'date_available': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'null': 'True', 'db_index': 'True'}),
            'date_insert': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_update': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'feed': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'db_index': 'True'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': u"orm['sites.Site']"}),
            'site_domain': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'site_iid': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True', 'max_length': '4', 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '150'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['%s.%s']" % (User._meta.app_label, User._meta.object_name)})
        },
        u'timelinejs.timeline': {
            'Meta': {'object_name': 'Timeline'},
            'asset_caption': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'asset_credit': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'asset_media': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'channel': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['channels.Channel']", 'null': 'True', 'on_delete': 'models.SET_NULL', 'blank': 'True'}),
            'containers': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'timeline_container'", 'to': u"orm['containers.Container']", 'through': u"orm['timelinejs.TimelineContainer']", 'blank': 'True', 'symmetrical': 'False', 'null': 'True'}),
            'headline': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'json': ('jsonfield.fields.JSONField', [], {'null': 'True', 'blank': 'True'}),
            'source': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'start_date': ('django.db.models.fields.DateField', [], {'blank': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'default': "'default'", 'max_length': '50'})
        },
        u'timelinejs.timelinecontainer': {
            'Meta': {'object_name': 'TimelineContainer'},
            'container': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'timelinecontainer_container'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': u"orm['containers.Container']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'timeline': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'timelinecontainer_timeline'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': u"orm['timelinejs.Timeline']"})
        },
        u'timelinejs.timelineevent': {
            'Meta': {'object_name': 'TimelineEvent'},
            'asset_caption': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'asset_credit': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'asset_media': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'asset_thumbnail': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'classname': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'end_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'headline': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'start_date': ('django.db.models.fields.DateField', [], {}),
            'tag': ('django.db.models.fields.CharField', [], {'max_length': '140', 'null': 'True', 'blank': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'timeline': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['timelinejs.Timeline']"}),
            'type': ('django.db.models.fields.CharField', [], {'default': "'date'", 'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'value': ('django.db.models.fields.CharField', [], {'max_length': '140', 'null': 'True', 'blank': 'True'})
        },
        u'timelinejs.timelineoptions': {
            'Meta': {'object_name': 'TimelineOptions'},
            'debug': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'embed_id': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'font': ('django.db.models.fields.CharField', [], {'default': "'Bevan-PotanoSans'", 'max_length': '50'}),
            'hash_bookmark': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'height': ('django.db.models.fields.CharField', [], {'default': "'600'", 'max_length': '10'}),
            'lang': ('django.db.models.fields.CharField', [], {'default': "'en'", 'max_length': '6'}),
            'maptype': ('django.db.models.fields.CharField', [], {'default': "'watercolor'", 'max_length': '50'}),
            'start_at_end': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'start_at_slide': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'start_zoom_adjust': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'timeline': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['timelinejs.Timeline']", 'unique': 'True', 'primary_key': 'True'}),
            'width': ('django.db.models.fields.CharField', [], {'default': "'100%'", 'max_length': '10'})
        }
    }

    complete_apps = ['timelinejs']