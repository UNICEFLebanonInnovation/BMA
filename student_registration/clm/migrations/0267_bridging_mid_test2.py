# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2024-05-02 15:30
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clm', '0266_bridging_mid_test1'),
    ]

    operations = [
        migrations.AddField(
            model_name='bridging',
            name='mid_test2',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True),
        ),
    ]
