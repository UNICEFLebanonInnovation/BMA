# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2025-07-01 16:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0025_auto_20241030_1235'),
    ]

    operations = [
        migrations.AlterField(
            model_name='center',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True, verbose_name='Email'),
        ),
    ]
