# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2023-08-08 16:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mscc', '0055_auto_20230710_1610'),
    ]

    operations = [
        migrations.AlterField(
            model_name='youthassessment',
            name='future_path',
            field=models.CharField(blank=True, choices=[('', '----------'), ('Transition to FE', 'Transition to FE'), ('Repeat the school year', 'Repeat the school year'), ('Refer to a UNICEF Youth Programme (skills tranining, CBT, GIL...)', 'Refer to a UNICEF Youth Programme (skills tranining, CBT, GIL...)'), ('Transition to TVET', 'Transition to TVET'), ('Internship or volunteering opportunity', 'Internship or volunteering opportunity')], max_length=200, null=True, verbose_name='What is the recommended future path for the adolescent?'),
        ),
    ]
