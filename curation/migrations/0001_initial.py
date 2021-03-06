# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-02-23 06:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300, verbose_name='title')),
            ],
            options={
                'verbose_name': 'collection',
                'verbose_name_plural': 'collections',
            },
        ),
        migrations.CreateModel(
            name='CollectionMovie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ordinal', models.IntegerField(default=100)),
                ('collection', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='movies', to='curation.Collection')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='collections', to='movies.Movie')),
            ],
        ),
    ]
