# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-02-23 06:58
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('editing_logs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='logitem',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]