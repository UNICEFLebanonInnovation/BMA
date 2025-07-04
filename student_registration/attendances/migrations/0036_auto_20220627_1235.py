# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2022-06-27 12:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendances', '0035_clmattendance_clmattendancestudent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clmattendance',
            name='close_reason',
            field=models.CharField(blank=True, choices=[('', '----------'), ('public_holiday', '\u0639\u0637\u0644\u0629 \u0631\u0633\u0645\u064a\u0629'), ('school_holiday', '\u0639\u0637\u0644\u0629 \u0645\u062f\u0631\u0633\u064a\u0629'), ('strike', '\u0627\u0636\u0631\u0627\u0628'), ('weekly_holiday', '\u0639\u0637\u0644\u0629 \u0646\u0647\u0627\u064a\u0629 \u0627\u0644\u0627\u0633\u0628\u0648\u0639'), ('roads_closed', 'Roads Closed')], max_length=50, null=True, verbose_name='Day off reason'),
        ),
    ]
