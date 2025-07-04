# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2020-10-28 15:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clm', '0163_auto_20201028_1655'),
    ]

    operations = [
        migrations.AlterField(
            model_name='abln',
            name='Followup_session_modality',
            field=models.CharField(blank=True, choices=[('online', '\u0639\u0646 \u0637\u0631\u064a\u0642 \u0627\u062a\u0635\u0627\u0644 Whatsapp'), ('phone', '\u0639\u0646 \u0637\u0631\u064a\u0642 \u0627\u0644\u0623\u062a\u0635\u0627\u0644 \u0627\u0644\u0647\u0627\u062a\u0641\u064a'), ('offline', ' \u0639\u0646 \u0637\u0631\u064a\u0642 \u0627\u0644\u0627\u062a\u0635\u0627\u0644 \u0627\u0644\u0645\u0628\u0627\u0634\u0631(\u0644\u064a\u0633 \u0639\u0628\u0631 \u0627\u0644\u0623\u0646\u062a\u0631\u0646\u062a)')], max_length=100, null=True, verbose_name='Please the modality used per each session'),
        ),
        migrations.AlterField(
            model_name='abln',
            name='covid_session_modality',
            field=models.CharField(blank=True, choices=[('online', '\u0639\u0646 \u0637\u0631\u064a\u0642 \u0627\u062a\u0635\u0627\u0644 Whatsapp'), ('phone', '\u0639\u0646 \u0637\u0631\u064a\u0642 \u0627\u0644\u0623\u062a\u0635\u0627\u0644 \u0627\u0644\u0647\u0627\u062a\u0641\u064a'), ('offline', ' \u0639\u0646 \u0637\u0631\u064a\u0642 \u0627\u0644\u0627\u062a\u0635\u0627\u0644 \u0627\u0644\u0645\u0628\u0627\u0634\u0631(\u0644\u064a\u0633 \u0639\u0628\u0631 \u0627\u0644\u0623\u0646\u062a\u0631\u0646\u062a)')], max_length=100, null=True, verbose_name='Please the modality used per each session'),
        ),
        migrations.AlterField(
            model_name='abln',
            name='pss_session_modality',
            field=models.CharField(blank=True, choices=[('online', '\u0639\u0646 \u0637\u0631\u064a\u0642 \u0627\u062a\u0635\u0627\u0644 Whatsapp'), ('phone', '\u0639\u0646 \u0637\u0631\u064a\u0642 \u0627\u0644\u0623\u062a\u0635\u0627\u0644 \u0627\u0644\u0647\u0627\u062a\u0641\u064a'), ('offline', ' \u0639\u0646 \u0637\u0631\u064a\u0642 \u0627\u0644\u0627\u062a\u0635\u0627\u0644 \u0627\u0644\u0645\u0628\u0627\u0634\u0631(\u0644\u064a\u0633 \u0639\u0628\u0631 \u0627\u0644\u0623\u0646\u062a\u0631\u0646\u062a)')], max_length=100, null=True, verbose_name='Please the modality used per each session'),
        ),
        migrations.AlterField(
            model_name='bln',
            name='Followup_session_modality',
            field=models.CharField(blank=True, choices=[('online', '\u0639\u0646 \u0637\u0631\u064a\u0642 \u0627\u062a\u0635\u0627\u0644 Whatsapp'), ('phone', '\u0639\u0646 \u0637\u0631\u064a\u0642 \u0627\u0644\u0623\u062a\u0635\u0627\u0644 \u0627\u0644\u0647\u0627\u062a\u0641\u064a'), ('offline', ' \u0639\u0646 \u0637\u0631\u064a\u0642 \u0627\u0644\u0627\u062a\u0635\u0627\u0644 \u0627\u0644\u0645\u0628\u0627\u0634\u0631(\u0644\u064a\u0633 \u0639\u0628\u0631 \u0627\u0644\u0623\u0646\u062a\u0631\u0646\u062a)')], max_length=100, null=True, verbose_name='Please the modality used per each session'),
        ),
        migrations.AlterField(
            model_name='bln',
            name='covid_session_modality',
            field=models.CharField(blank=True, choices=[('online', '\u0639\u0646 \u0637\u0631\u064a\u0642 \u0627\u062a\u0635\u0627\u0644 Whatsapp'), ('phone', '\u0639\u0646 \u0637\u0631\u064a\u0642 \u0627\u0644\u0623\u062a\u0635\u0627\u0644 \u0627\u0644\u0647\u0627\u062a\u0641\u064a'), ('offline', ' \u0639\u0646 \u0637\u0631\u064a\u0642 \u0627\u0644\u0627\u062a\u0635\u0627\u0644 \u0627\u0644\u0645\u0628\u0627\u0634\u0631(\u0644\u064a\u0633 \u0639\u0628\u0631 \u0627\u0644\u0623\u0646\u062a\u0631\u0646\u062a)')], max_length=100, null=True, verbose_name='Please the modality used per each session'),
        ),
        migrations.AlterField(
            model_name='bln',
            name='pss_session_modality',
            field=models.CharField(blank=True, choices=[('online', '\u0639\u0646 \u0637\u0631\u064a\u0642 \u0627\u062a\u0635\u0627\u0644 Whatsapp'), ('phone', '\u0639\u0646 \u0637\u0631\u064a\u0642 \u0627\u0644\u0623\u062a\u0635\u0627\u0644 \u0627\u0644\u0647\u0627\u062a\u0641\u064a'), ('offline', ' \u0639\u0646 \u0637\u0631\u064a\u0642 \u0627\u0644\u0627\u062a\u0635\u0627\u0644 \u0627\u0644\u0645\u0628\u0627\u0634\u0631(\u0644\u064a\u0633 \u0639\u0628\u0631 \u0627\u0644\u0623\u0646\u062a\u0631\u0646\u062a)')], max_length=100, null=True, verbose_name='Please the modality used per each session'),
        ),
        migrations.AlterField(
            model_name='cbece',
            name='Followup_session_modality',
            field=models.CharField(blank=True, choices=[('online', '\u0639\u0646 \u0637\u0631\u064a\u0642 \u0627\u062a\u0635\u0627\u0644 Whatsapp'), ('phone', '\u0639\u0646 \u0637\u0631\u064a\u0642 \u0627\u0644\u0623\u062a\u0635\u0627\u0644 \u0627\u0644\u0647\u0627\u062a\u0641\u064a'), ('offline', ' \u0639\u0646 \u0637\u0631\u064a\u0642 \u0627\u0644\u0627\u062a\u0635\u0627\u0644 \u0627\u0644\u0645\u0628\u0627\u0634\u0631(\u0644\u064a\u0633 \u0639\u0628\u0631 \u0627\u0644\u0623\u0646\u062a\u0631\u0646\u062a)')], max_length=100, null=True, verbose_name='Please the modality used per each session'),
        ),
        migrations.AlterField(
            model_name='cbece',
            name='covid_session_modality',
            field=models.CharField(blank=True, choices=[('online', '\u0639\u0646 \u0637\u0631\u064a\u0642 \u0627\u062a\u0635\u0627\u0644 Whatsapp'), ('phone', '\u0639\u0646 \u0637\u0631\u064a\u0642 \u0627\u0644\u0623\u062a\u0635\u0627\u0644 \u0627\u0644\u0647\u0627\u062a\u0641\u064a'), ('offline', ' \u0639\u0646 \u0637\u0631\u064a\u0642 \u0627\u0644\u0627\u062a\u0635\u0627\u0644 \u0627\u0644\u0645\u0628\u0627\u0634\u0631(\u0644\u064a\u0633 \u0639\u0628\u0631 \u0627\u0644\u0623\u0646\u062a\u0631\u0646\u062a)')], max_length=100, null=True, verbose_name='Please the modality used per each session'),
        ),
        migrations.AlterField(
            model_name='cbece',
            name='pss_session_modality',
            field=models.CharField(blank=True, choices=[('online', '\u0639\u0646 \u0637\u0631\u064a\u0642 \u0627\u062a\u0635\u0627\u0644 Whatsapp'), ('phone', '\u0639\u0646 \u0637\u0631\u064a\u0642 \u0627\u0644\u0623\u062a\u0635\u0627\u0644 \u0627\u0644\u0647\u0627\u062a\u0641\u064a'), ('offline', ' \u0639\u0646 \u0637\u0631\u064a\u0642 \u0627\u0644\u0627\u062a\u0635\u0627\u0644 \u0627\u0644\u0645\u0628\u0627\u0634\u0631(\u0644\u064a\u0633 \u0639\u0628\u0631 \u0627\u0644\u0623\u0646\u062a\u0631\u0646\u062a)')], max_length=100, null=True, verbose_name='Please the modality used per each session'),
        ),
        migrations.AlterField(
            model_name='rs',
            name='Followup_session_modality',
            field=models.CharField(blank=True, choices=[('online', '\u0639\u0646 \u0637\u0631\u064a\u0642 \u0627\u062a\u0635\u0627\u0644 Whatsapp'), ('phone', '\u0639\u0646 \u0637\u0631\u064a\u0642 \u0627\u0644\u0623\u062a\u0635\u0627\u0644 \u0627\u0644\u0647\u0627\u062a\u0641\u064a'), ('offline', ' \u0639\u0646 \u0637\u0631\u064a\u0642 \u0627\u0644\u0627\u062a\u0635\u0627\u0644 \u0627\u0644\u0645\u0628\u0627\u0634\u0631(\u0644\u064a\u0633 \u0639\u0628\u0631 \u0627\u0644\u0623\u0646\u062a\u0631\u0646\u062a)')], max_length=100, null=True, verbose_name='Please the modality used per each session'),
        ),
        migrations.AlterField(
            model_name='rs',
            name='covid_session_modality',
            field=models.CharField(blank=True, choices=[('online', '\u0639\u0646 \u0637\u0631\u064a\u0642 \u0627\u062a\u0635\u0627\u0644 Whatsapp'), ('phone', '\u0639\u0646 \u0637\u0631\u064a\u0642 \u0627\u0644\u0623\u062a\u0635\u0627\u0644 \u0627\u0644\u0647\u0627\u062a\u0641\u064a'), ('offline', ' \u0639\u0646 \u0637\u0631\u064a\u0642 \u0627\u0644\u0627\u062a\u0635\u0627\u0644 \u0627\u0644\u0645\u0628\u0627\u0634\u0631(\u0644\u064a\u0633 \u0639\u0628\u0631 \u0627\u0644\u0623\u0646\u062a\u0631\u0646\u062a)')], max_length=100, null=True, verbose_name='Please the modality used per each session'),
        ),
        migrations.AlterField(
            model_name='rs',
            name='pss_session_modality',
            field=models.CharField(blank=True, choices=[('online', '\u0639\u0646 \u0637\u0631\u064a\u0642 \u0627\u062a\u0635\u0627\u0644 Whatsapp'), ('phone', '\u0639\u0646 \u0637\u0631\u064a\u0642 \u0627\u0644\u0623\u062a\u0635\u0627\u0644 \u0627\u0644\u0647\u0627\u062a\u0641\u064a'), ('offline', ' \u0639\u0646 \u0637\u0631\u064a\u0642 \u0627\u0644\u0627\u062a\u0635\u0627\u0644 \u0627\u0644\u0645\u0628\u0627\u0634\u0631(\u0644\u064a\u0633 \u0639\u0628\u0631 \u0627\u0644\u0623\u0646\u062a\u0631\u0646\u062a)')], max_length=100, null=True, verbose_name='Please the modality used per each session'),
        ),
    ]
