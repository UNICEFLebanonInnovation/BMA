# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2020-10-12 06:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clm', '0157_auto_20201012_0858'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bln',
            name='registration_level',
            field=models.CharField(blank=True, choices=[('', '----------'), ('level_one', '\u0627\u0644\u0645\u0633\u062a\u0648\u0649 \u0627\u0644\u0623\u0648\u0644'), ('level_two', '\u0627\u0644\u0645\u0633\u062a\u0648\u0649 \u0627\u0644\u062b\u0627\u0646\u064a'), ('level_three', '\u0627\u0644\u0645\u0633\u062a\u0648\u0649 \u0627\u0644\u062b\u0627\u0644\u062b')], max_length=100, null=True, verbose_name='\u0645\u0633\u062a\u0648\u0649 \u0627\u0644\u062a\u0633\u062c\u064a\u0644'),
        ),
    ]
