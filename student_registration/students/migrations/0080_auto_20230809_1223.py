# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2023-08-09 12:23
from __future__ import unicode_literals

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0079_auto_20230510_1313'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='subjects_provided',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, choices=[('arabic', 'Arabic'), ('math', 'Math'), ('english', 'English'), ('french', 'French'), ('PSS / Counsellor', 'PSS / Counsellor'), ('Physical Education', 'Physical Education'), ('Art', 'Art')], max_length=200, null=True), blank=True, null=True, size=None, verbose_name='Subjects provided'),
        ),
    ]
