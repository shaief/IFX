# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-02-18 21:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Identity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source_type', models.CharField(choices=[('WIKIDATA', 'WIKIDATA'), ('WIKIPEDIA', 'WIKIPEDIA'), ('VIAF', 'VAIF')], default='VIAF', max_length=300)),
                ('source_value', models.CharField(blank=True, max_length=300, null=True)),
                ('status', models.CharField(choices=[('NEW', 'NEW'), ('ACCEPTED', 'ACCEPTED'), ('REJECTED', 'REJECTED'), ('UNDER_DISCUSSION', 'UNDER_DISCUSSION')], default='NEW', max_length=300)),
                ('notes', models.TextField(blank=True, null=True)),
                ('score', models.IntegerField(blank=True, null=True)),
                ('object_id', models.PositiveIntegerField(null=True, verbose_name='related object')),
                ('content_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType', verbose_name='content person')),
            ],
        ),
    ]
