# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2023-03-31 13:44
from __future__ import unicode_literals

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0072_auto_20230223_1523'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacher',
            name='training',
        ),
        migrations.AddField(
            model_name='teacher',
            name='extra_coaching_specify',
            field=models.TextField(blank=True, null=True, verbose_name='Please specify'),
        ),
        migrations.AddField(
            model_name='teacher',
            name='teacher_assignment',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, choices=[('full_time', 'Full time'), ('part_time_mix_private', 'Part time, Mix private'), ('part_time_sbp_only', 'Part time, SBP only')], max_length=50, null=True), blank=True, null=True, size=None, verbose_name='Teacher Assignment'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='grade_level',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, choices=[('Grade 1', 'Grade 1'), ('Grade 2', 'Grade 2'), ('Grade 3', 'Grade 3'), ('Grade 4', 'Grade 4'), ('Grade 5', 'Grade 5'), ('Grade 6', 'Grade 6')], max_length=50, null=True), blank=True, null=True, size=None, verbose_name='Grade level'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='trainings',
            field=models.ManyToManyField(blank=True, to='students.Training', verbose_name='Topics of teacher training'),
        ),
    ]
