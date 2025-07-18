# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2025-07-02 14:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendances', '0062_auto_20241022_1812'),
    ]

    operations = [
        migrations.AlterField(
            model_name='msccattendance',
            name='education_program',
            field=models.CharField(blank=True, choices=[('BLN Level 1', 'BLN Level 1'), ('BLN Level 2', 'BLN Level 2'), ('BLN Level 3', 'BLN Level 3'), ('ABLN Level 1', 'ABLN Level 1'), ('ABLN Level 2', 'ABLN Level 2'), ('YBLN Level 1', 'YBLN Level 1'), ('YBLN Level 2', 'YBLN Level 2'), ('YFS Level 1', 'YFS Level 1'), ('YFS Level 2', 'YFS Level 2'), ('CBECE Level 1', 'CBECE Level 1'), ('CBECE Level 2', 'CBECE Level 2'), ('CBECE Level 3', 'CBECE Level 3'), ('RS Grade 7', 'RS Grade 7'), ('RS Grade 8', 'RS Grade 8'), ('RS Grade 9', 'RS Grade 9'), ('ECD', 'ECD'), ('YFS Level 1 - RS Grade 9', 'YFS Level 1 - RS Grade 9'), ('YFS Level 2 - RS Grade 9', 'YFS Level 2 - RS Grade 9')], max_length=200, null=True, verbose_name='Education Program'),
        ),
    ]
