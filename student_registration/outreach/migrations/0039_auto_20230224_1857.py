# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2023-02-24 18:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('outreach', '0038_auto_20230224_1840'),
    ]

    operations = [
        migrations.AlterField(
            model_name='outreachchild',
            name='child_notes',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]
