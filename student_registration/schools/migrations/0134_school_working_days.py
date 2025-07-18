# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2023-04-05 14:56
from __future__ import unicode_literals

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schools', '0133_auto_20221206_1532'),
    ]

    operations = [
        migrations.AddField(
            model_name='school',
            name='working_days',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, choices=[('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday'), ('Friday', 'Friday'), ('Saturday', 'Saturday'), ('Sunday', 'Friday')], max_length=100, null=True), blank=True, null=True, size=None, verbose_name='Working Days'),
        ),
    ]
