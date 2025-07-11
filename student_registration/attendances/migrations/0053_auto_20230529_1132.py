# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2023-05-29 11:32
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('attendances', '0052_auto_20230412_1308'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='clmattendance',
            options={'ordering': ['attendance_date'], 'verbose_name': 'CLM Attendances by School by Day'},
        ),
        migrations.AlterModelOptions(
            name='clmattendancestudent',
            options={'ordering': ['id'], 'verbose_name': 'CLM Student Attendance'},
        ),
        migrations.AlterModelOptions(
            name='clmstudentabsences',
            options={'ordering': ['id'], 'verbose_name': 'CLM Student Absences'},
        ),
        migrations.AlterModelOptions(
            name='clmstudenttotalattendance',
            options={'ordering': ['id'], 'verbose_name': 'CLM Student Total Attendance'},
        ),
        migrations.AlterModelOptions(
            name='msccattendance',
            options={'ordering': ['attendance_date'], 'verbose_name': 'MSCC Attendances by Day'},
        ),
        migrations.AlterModelOptions(
            name='msccattendancechild',
            options={'ordering': ['id'], 'verbose_name': 'MSCC Child Attendance'},
        ),
    ]
