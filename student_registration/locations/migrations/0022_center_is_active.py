# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2024-10-03 17:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0021_auto_20240722_1626'),
    ]

    operations = [
        migrations.AddField(
            model_name='center',
            name='is_active',
            field=models.BooleanField(default=False, verbose_name='is active'),
        ),
    ]
