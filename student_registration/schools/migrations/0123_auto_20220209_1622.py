# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2022-02-09 16:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schools', '0122_auto_20220119_1347'),
    ]

    operations = [
        migrations.AddField(
            model_name='clmround',
            name='current_round_bridging',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='clmround',
            name='end_date_bridging',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='clmround',
            name='end_date_bridging_edit',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='clmround',
            name='start_date_bridging',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='clmround',
            name='start_date_bridging_edit',
            field=models.DateField(blank=True, null=True),
        ),
    ]
