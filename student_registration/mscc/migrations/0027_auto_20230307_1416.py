# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2023-03-07 14:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mscc', '0026_merge_20230307_1047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='followupservice',
            name='caregiver_attended',
            field=models.CharField(blank=True, choices=[('', '----------'), ('Mother Only', 'Mother Only'), ('Father Only', 'Father Only'), ('Mother & Father', 'Mother & Father'), ('Other', 'Other')], max_length=100, null=True, verbose_name='Who attended the meetings'),
        ),
    ]
