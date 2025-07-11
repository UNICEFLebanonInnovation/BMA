# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2022-01-17 11:37
from __future__ import unicode_literals

from django.conf import settings
import django.contrib.postgres.fields
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        # ('schools', '0122_auto_20220117_1137'),
        ('clm', '0217_auto_20220117_1010'),
    ]

    operations = [
        migrations.AddField(
            model_name='inclusion',
            name='caregiver_trained_parental_engagement',
            field=models.CharField(blank=True, choices=[('Mother Only', 'Mother Only'), ('Father Only', 'Father Only'), ('Both Mother and Father', 'Both Mother and Father'), ('None', '\u0644\u0627\u0634\u064a\u0621'), ('Other', '\u0622\u062e\u0631'), ('Not begun yet', 'Not begun yet')], max_length=100, null=True, verbose_name='Have the Caregivers been trained on the Parental Engagement Curriculum? '),
        ),
        migrations.AddField(
            model_name='inclusion',
            name='child_dropout',
            field=models.CharField(blank=True, choices=[(1, '\u0646\u0639\u0645'), (0, '\u0643\u0644\u0627')], max_length=10, null=True, verbose_name='Has the child dropped out of the program?'),
        ),
        migrations.AddField(
            model_name='inclusion',
            name='child_dropout_other',
            field=models.TextField(blank=True, null=True, verbose_name='\u064a\u0631\u062c\u0649 \u0627\u0644\u062a\u062d\u062f\u064a\u062f'),
        ),
    ]
