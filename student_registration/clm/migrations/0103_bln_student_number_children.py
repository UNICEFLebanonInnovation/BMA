# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2020-03-25 11:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clm', '0102_merge_20200325_1336'),
    ]

    operations = [
        migrations.AddField(
            model_name='bln',
            name='student_number_children',
            field=models.IntegerField(blank=True, choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12), (13, 13), (14, 14), (15, 15), (16, 16), (17, 17), (18, 18), (19, 19)], null=True, verbose_name='\u062d\u062f\u062f \u0639\u062f\u062f \u0627\u0644\u0623\u0637\u0641\u0627\u0644'),
        ),
    ]
