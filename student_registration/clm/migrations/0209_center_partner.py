# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2021-04-19 11:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clm', '0208_auto_20210402_1425'),
    ]

    operations = [
        migrations.AddField(
            model_name='center',
            name='partner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='schools.PartnerOrganization', verbose_name='\u0627\u0644\u062c\u0645\u0639\u064a\u0629'),
        ),
    ]
