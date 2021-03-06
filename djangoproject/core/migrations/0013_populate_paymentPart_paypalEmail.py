# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import DataMigration
from django.db import models

class Migration(DataMigration):

    def forwards(self, orm):
        "Write your forwards methods here."
        for part in orm.PaymentPart.objects.all() :
            user_info = orm.UserInfo.objects.get(user__id = part.programmer.id)
            part.paypalEmail = user_info.paypalEmail
            part.save()

    def backwards(self, orm):
        "Write your backwards methods here."
        pass

    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'core.issue': {
            'Meta': {'object_name': 'Issue'},
            'createdByUser': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'creationDate': ('django.db.models.fields.DateTimeField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_feedback': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_public_suggestion': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'key': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Project']", 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '400'}),
            'trackerURL': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        },
        'core.issuecomment': {
            'Meta': {'object_name': 'IssueComment'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'content': ('django.db.models.fields.TextField', [], {}),
            'creationDate': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'issue': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Issue']"})
        },
        'core.issuecommenthistevent': {
            'Meta': {'object_name': 'IssueCommentHistEvent'},
            'comment': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.IssueComment']"}),
            'content': ('django.db.models.fields.TextField', [], {}),
            'event': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'eventDate': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'core.issuewatch': {
            'Meta': {'object_name': 'IssueWatch'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'issue': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Issue']"}),
            'reason': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'core.offer': {
            'Meta': {'object_name': 'Offer'},
            'acceptanceCriteria': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'creationDate': ('django.db.models.fields.DateTimeField', [], {}),
            'expirationDate': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'issue': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Issue']"}),
            'lastChangeDate': ('django.db.models.fields.DateTimeField', [], {}),
            'no_forking': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'price': ('django.db.models.fields.DecimalField', [], {'max_digits': '9', 'decimal_places': '2'}),
            'require_release': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'sponsor': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        'core.offercomment': {
            'Meta': {'object_name': 'OfferComment'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'content': ('django.db.models.fields.TextField', [], {}),
            'creationDate': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'offer': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Offer']"})
        },
        'core.offercommenthistevent': {
            'Meta': {'object_name': 'OfferCommentHistEvent'},
            'comment': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.OfferComment']"}),
            'content': ('django.db.models.fields.TextField', [], {}),
            'event': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'eventDate': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'core.offerhistevent': {
            'Meta': {'object_name': 'OfferHistEvent'},
            'acceptanceCriteria': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'event': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'eventDate': ('django.db.models.fields.DateTimeField', [], {}),
            'expirationDate': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'no_forking': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'offer': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Offer']"}),
            'price': ('django.db.models.fields.DecimalField', [], {'max_digits': '9', 'decimal_places': '2'}),
            'require_release': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        'core.offerwatch': {
            'Meta': {'object_name': 'OfferWatch'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'offer': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Offer']"}),
            'reason': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'core.payment': {
            'Meta': {'object_name': 'Payment'},
            'confirm_key': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'creationDate': ('django.db.models.fields.DateTimeField', [], {}),
            'currency': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'fee': ('django.db.models.fields.DecimalField', [], {'max_digits': '9', 'decimal_places': '2'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lastChangeDate': ('django.db.models.fields.DateTimeField', [], {}),
            'offer': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Offer']"}),
            'paykey': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'total': ('django.db.models.fields.DecimalField', [], {'max_digits': '9', 'decimal_places': '2'})
        },
        'core.paymenthistevent': {
            'Meta': {'object_name': 'PaymentHistEvent'},
            'event': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'eventDate': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'payment': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Payment']"}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        'core.paymentpart': {
            'Meta': {'object_name': 'PaymentPart'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'payment': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Payment']"}),
            'paypalEmail': ('django.db.models.fields.EmailField', [], {'max_length': '256', 'null': 'True'}),
            'price': ('django.db.models.fields.DecimalField', [], {'max_digits': '9', 'decimal_places': '2'}),
            'programmer': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'realprice': ('django.db.models.fields.DecimalField', [], {'max_digits': '9', 'decimal_places': '2'})
        },
        'core.project': {
            'Meta': {'object_name': 'Project'},
            'createdByUser': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'creationDate': ('django.db.models.fields.DateTimeField', [], {}),
            'homeURL': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'trackerURL': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        },
        'core.solution': {
            'Meta': {'object_name': 'Solution'},
            'creationDate': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'issue': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Issue']"}),
            'lastChangeDate': ('django.db.models.fields.DateTimeField', [], {}),
            'programmer': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        'core.solutionhistevent': {
            'Meta': {'object_name': 'SolutionHistEvent'},
            'event': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'eventDate': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'solution': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Solution']"}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        'core.userinfo': {
            'Meta': {'object_name': 'UserInfo'},
            'about': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'brazilianPaypal': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_paypal_email_verified': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_primary_email_verified': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'paypalEmail': ('django.db.models.fields.EmailField', [], {'max_length': '256'}),
            'realName': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'receiveAllEmail': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'screenName': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'website': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['core']
    symmetrical = True
