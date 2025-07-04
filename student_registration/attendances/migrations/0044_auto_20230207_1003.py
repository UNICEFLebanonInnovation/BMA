# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2023-02-07 10:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendances', '0043_auto_20230123_1309'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='msccattendancechild',
            options={'ordering': ['id'], 'verbose_name': 'Child Attendance'},
        ),
        migrations.AlterField(
            model_name='msccattendancechild',
            name='attended',
            field=models.CharField(blank=True, choices=[('', '----------'), ('Yes', 'Yes'), ('No', 'No')], max_length=10, null=True, verbose_name='Child Attended?'),
        ),
    ]
