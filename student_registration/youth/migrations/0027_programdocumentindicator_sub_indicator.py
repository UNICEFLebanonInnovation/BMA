# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2025-06-25 12:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('youth', '0026_auto_20250612_1428'),
    ]

    operations = [
        migrations.AddField(
            model_name='programdocumentindicator',
            name='Sub_indicator',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sub_indicator', to='youth.SubProgram', verbose_name='Sub Indicator'),
        ),
    ]
