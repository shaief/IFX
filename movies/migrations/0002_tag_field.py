# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-07 13:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag_Field',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lang', models.CharField(max_length=300)),
                ('title', models.CharField(max_length=300)),
                ('field', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.Field')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.Tag')),
            ],
        ),
    ]