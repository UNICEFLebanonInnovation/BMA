# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2023-04-28 13:30
from __future__ import unicode_literals

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0075_auto_20230427_1513'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacher',
            name='subject_provided',
        ),
        migrations.AddField(
            model_name='teacher',
            name='subjects_provided',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, choices=[('arabic', 'Arabic'), ('math', 'Math'), ('english', 'English'), ('french', 'French')], max_length=200, null=True), blank=True, null=True, size=None, verbose_name='Subjects provided'),
        ),
        migrations.AddField(
            model_name='teacher',
            name='teaching_hours_dirasa',
            field=models.IntegerField(blank=True, null=True, verbose_name='Number of teaching hours in Dirasa'),
        ),
        migrations.AddField(
            model_name='teacher',
            name='teaching_hours_private_school',
            field=models.IntegerField(blank=True, null=True, verbose_name='Number of teaching hours in private school'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='registration_level',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, choices=[('Level one', 'Level one'), ('Level two', 'Level two'), ('Level three', 'Level three'), ('Level four', 'Level four'), ('Level five', 'Level five'), ('Level six', 'Level six')], max_length=200, null=True), blank=True, null=True, size=None, verbose_name='Dirasa Grade level'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='teacher_assignment',
            field=models.CharField(blank=True, choices=[('Dirasa only', 'Dirasa only'), ('Private and Dirasa', 'Private and Dirasa')], max_length=100, null=True, verbose_name='Teacher Assignment'),
        ),
    ]
