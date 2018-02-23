# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-02-23 06:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields.json


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Suggestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField(choices=[(1, 'pending'), (5, 'error'), (10, 'no results'), (11, 'too many results'), (100, 'found (unverified)'), (200, 'verified'), (500, 'rejected')], verbose_name='status')),
                ('object_id', models.PositiveIntegerField()),
                ('query', models.CharField(max_length=300, verbose_name='query string')),
                ('source', models.IntegerField(choices=[(1, 'WikiData'), (2, 'Wikipedia'), (3, 'VAIF')], verbose_name='source')),
                ('source_key', models.CharField(max_length=500, null=True)),
                ('source_url', models.URLField(null=True)),
                ('result', django_extensions.db.fields.json.JSONField(default=dict, null=True)),
                ('error_message', models.TextField(null=True)),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType', verbose_name='entity type')),
            ],
            options={
                'verbose_name': 'suggestion',
                'verbose_name_plural': 'suggestions',
            },
        ),
    ]
