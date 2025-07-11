# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2023-05-09 16:08
from __future__ import unicode_literals

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schools', '0142_auto_20230505_0944'),
    ]

    operations = [
        migrations.AlterField(
            model_name='school',
            name='working_days',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, choices=[('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday'), ('Friday', 'Friday'), ('Saturday', 'Saturday'), ('Sunday', 'Sunday')], max_length=100, null=True), blank=True, null=True, size=None, verbose_name='Working Days'),
        ),
    ]
