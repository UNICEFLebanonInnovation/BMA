# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2022-03-03 16:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clm', '0235_auto_20220303_1520'),
    ]

    operations = [
        migrations.AlterField(
            model_name='outreach',
            name='education_status',
            field=models.CharField(blank=True, choices=[('', '----------'), ('No Registered in any school before', '\u0644\u0645 \u064a\u0633\u062c\u0644 \u0627\u0628\u062f\u0627 \u0641\u064a \u0627\u0644\u0645\u062f\u0631\u0633\u0629 \u0645\u0646 \u0642\u0628\u0644'), ('Was registered in BLN program', '\u0643\u0627\u0646 \u0645\u0633\u062c\u0644 \u0641\u064a \u0628\u0631\u0646\u0627\u0645\u062c BLN'), ('Was registered in formal school and didnt continue', '\u0643\u0627\u0646 \u0645\u0633\u062c\u0644 \u0641\u064a \u0627\u0644\u0645\u062f\u0631\u0633\u0629 \u0646\u0638\u0627\u0645\u064a\u0629 \u0648\u0644\u0645 \u064a\u0643\u0645\u0644'), ('Was registered in CBECE program', 'CBECE \u0643\u0627\u0646 \u0645\u0633\u062c\u0644 \u0641\u064a \u0628\u0631\u0646\u0627\u0645\u062c'), ('Was registered in ALP program and didnt continue', 'ALP \u0643\u0627\u0646 \u0645\u0633\u062c\u0644 \u0641\u064a \u0628\u0631\u0646\u0627\u0645\u062c ')], max_length=100, null=True, verbose_name='\u0627\u0644\u0648\u0636\u0639 \u0627\u0644\u062f\u0631\u0627\u0633\u064a \u0644\u0644\u0637\u0641\u0644 \u0639\u0646\u062f \u0627\u0644\u062a\u0633\u062c\u064a\u0644 \u0641\u064a \u0627\u0644\u062f\u0648\u0631\u0629'),
        ),
        migrations.AlterField(
            model_name='outreach',
            name='source_of_identification',
            field=models.CharField(blank=True, choices=[('', '----------'), ('CP partner referral', 'CP partner referral'), ('Awarness Session', 'Awarness Session'), ('Child parents', 'Child parents'), ('From Profiling Database', 'From Profiling Database'), ('Referred by the municipality / Other formal sources', 'Referred by the municipality / Other formal sources'), ('From Displaced Community', 'From Displaced Community'), ('From Hosted Community', 'From Hosted Community'), ('From Other NGO', 'From Other NGO'), ('School Director', 'School Director'), ('RIMS', 'RIMS')], max_length=100, null=True, verbose_name='\u0645\u0635\u062f\u0631 \u0627\u062d\u0627\u0644\u0629 \u0627\u0644\u0637\u0641\u0644  \u0625\u0644\u0649 \u0628\u0631\u0646\u0627\u0645\u062c ABLN'),
        ),
    ]
