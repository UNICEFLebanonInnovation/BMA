# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2025-05-06 19:43
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mscc', '0075_lego'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='lego',
            new_name='LegoService',
        ),
    ]
