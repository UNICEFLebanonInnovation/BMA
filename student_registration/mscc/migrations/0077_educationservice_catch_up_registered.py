# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2025-06-27 16:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mscc', '0076_auto_20250506_1943'),
    ]

    operations = [
        migrations.AddField(
            model_name='educationservice',
            name='catch_up_registered',
            field=models.CharField(blank=True, choices=[('Yes-New Comers programme', 'Yes-New Comers programme'), ('Yes-Undocumented programme', 'Yes-Undocumented programme'), ('No', 'No')], max_length=200, null=True, verbose_name='Is the child registered in catch-up program'),
        ),
    ]
