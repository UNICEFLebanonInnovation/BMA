# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2024-08-09 11:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('youth', '0016_auto_20240725_1832'),
    ]

    operations = [
        migrations.AddField(
            model_name='programdocument',
            name='donors',
            field=models.ManyToManyField(blank=True, to='youth.Donor', verbose_name='Donors'),
        ),
    ]
