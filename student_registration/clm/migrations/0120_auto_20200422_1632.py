# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2020-04-22 13:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clm', '0119_auto_20200415_1939'),
    ]

    operations = [
        migrations.AlterField(
            model_name='abln',
            name='phone_number_confirm',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Phone number confirm'),
        ),
        migrations.AlterField(
            model_name='abln',
            name='phone_owner',
            field=models.CharField(blank=True, choices=[('main_caregiver', '\u0648\u0644\u064a \u0627\u0644\u0623\u0645\u0631'), ('family member', '\u0623\u062d\u062f \u0627\u0641\u0631\u0627\u062f \u0627\u0644\u0639\u0627\u0626\u0644\u0629'), ('neighbors', '\u0627\u0644\u062c\u064a\u0627\u0631\u0627\u0646'), ('shawish', '\u0627\u0644\u0634\u0627\u0648\u064a\u0634')], max_length=100, null=True, verbose_name='\u0645\u0646 \u0627\u0644\u0634\u062e\u0635 \u0627\u0644\u0630\u064a \u064a\u062c\u064a\u0628 \u0639\u0644\u0649 \u0647\u0630\u0627 \u0627\u0644\u0631\u0642\u0645\u061f'),
        ),
        migrations.AlterField(
            model_name='abln',
            name='second_phone_number',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='\u0631\u0642\u0645 \u0627\u0644\u0647\u0627\u062a\u0641 \u0627\u0644\u062b\u0627\u0646\u0648\u064a'),
        ),
        migrations.AlterField(
            model_name='abln',
            name='second_phone_number_confirm',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='\u062a\u0623\u0643\u064a\u062f \u0631\u0642\u0645 \u0627\u0644\u0647\u0627\u062a\u0641 \u0627\u0644\u062b\u0627\u0646\u0648\u064a'),
        ),
        migrations.AlterField(
            model_name='abln',
            name='second_phone_owner',
            field=models.CharField(blank=True, choices=[('main_caregiver', '\u0648\u0644\u064a \u0627\u0644\u0623\u0645\u0631'), ('family member', '\u0623\u062d\u062f \u0627\u0641\u0631\u0627\u062f \u0627\u0644\u0639\u0627\u0626\u0644\u0629'), ('neighbors', '\u0627\u0644\u062c\u064a\u0627\u0631\u0627\u0646'), ('shawish', '\u0627\u0644\u0634\u0627\u0648\u064a\u0634')], max_length=100, null=True, verbose_name='\u0645\u0646 \u0627\u0644\u0634\u062e\u0635 \u0627\u0644\u0630\u064a \u064a\u062c\u064a\u0628 \u0639\u0644\u0649 \u0647\u0630\u0627 \u0627\u0644\u0631\u0642\u0645\u061f'),
        ),
        migrations.AlterField(
            model_name='bln',
            name='phone_number_confirm',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Phone number confirm'),
        ),
        migrations.AlterField(
            model_name='bln',
            name='phone_owner',
            field=models.CharField(blank=True, choices=[('main_caregiver', '\u0648\u0644\u064a \u0627\u0644\u0623\u0645\u0631'), ('family member', '\u0623\u062d\u062f \u0627\u0641\u0631\u0627\u062f \u0627\u0644\u0639\u0627\u0626\u0644\u0629'), ('neighbors', '\u0627\u0644\u062c\u064a\u0627\u0631\u0627\u0646'), ('shawish', '\u0627\u0644\u0634\u0627\u0648\u064a\u0634')], max_length=100, null=True, verbose_name='\u0645\u0646 \u0627\u0644\u0634\u062e\u0635 \u0627\u0644\u0630\u064a \u064a\u062c\u064a\u0628 \u0639\u0644\u0649 \u0647\u0630\u0627 \u0627\u0644\u0631\u0642\u0645\u061f'),
        ),
        migrations.AlterField(
            model_name='bln',
            name='second_phone_number',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='\u0631\u0642\u0645 \u0627\u0644\u0647\u0627\u062a\u0641 \u0627\u0644\u062b\u0627\u0646\u0648\u064a'),
        ),
        migrations.AlterField(
            model_name='bln',
            name='second_phone_number_confirm',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='\u062a\u0623\u0643\u064a\u062f \u0631\u0642\u0645 \u0627\u0644\u0647\u0627\u062a\u0641 \u0627\u0644\u062b\u0627\u0646\u0648\u064a'),
        ),
        migrations.AlterField(
            model_name='bln',
            name='second_phone_owner',
            field=models.CharField(blank=True, choices=[('main_caregiver', '\u0648\u0644\u064a \u0627\u0644\u0623\u0645\u0631'), ('family member', '\u0623\u062d\u062f \u0627\u0641\u0631\u0627\u062f \u0627\u0644\u0639\u0627\u0626\u0644\u0629'), ('neighbors', '\u0627\u0644\u062c\u064a\u0627\u0631\u0627\u0646'), ('shawish', '\u0627\u0644\u0634\u0627\u0648\u064a\u0634')], max_length=100, null=True, verbose_name='\u0645\u0646 \u0627\u0644\u0634\u062e\u0635 \u0627\u0644\u0630\u064a \u064a\u062c\u064a\u0628 \u0639\u0644\u0649 \u0647\u0630\u0627 \u0627\u0644\u0631\u0642\u0645\u061f'),
        ),
        migrations.AlterField(
            model_name='cbece',
            name='phone_number_confirm',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Phone number confirm'),
        ),
        migrations.AlterField(
            model_name='inclusion',
            name='phone_number_confirm',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Phone number confirm'),
        ),
        migrations.AlterField(
            model_name='inclusion',
            name='phone_owner',
            field=models.CharField(choices=[('main_caregiver', '\u0648\u0644\u064a \u0627\u0644\u0623\u0645\u0631'), ('family member', '\u0623\u062d\u062f \u0627\u0641\u0631\u0627\u062f \u0627\u0644\u0639\u0627\u0626\u0644\u0629'), ('neighbors', '\u0627\u0644\u062c\u064a\u0627\u0631\u0627\u0646'), ('shawish', '\u0627\u0644\u0634\u0627\u0648\u064a\u0634')], max_length=100, null=True, verbose_name='\u0645\u0646 \u0627\u0644\u0634\u062e\u0635 \u0627\u0644\u0630\u064a \u064a\u062c\u064a\u0628 \u0639\u0644\u0649 \u0647\u0630\u0627 \u0627\u0644\u0631\u0642\u0645\u061f'),
        ),
        migrations.AlterField(
            model_name='inclusion',
            name='second_phone_number',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='\u0631\u0642\u0645 \u0627\u0644\u0647\u0627\u062a\u0641 \u0627\u0644\u062b\u0627\u0646\u0648\u064a'),
        ),
        migrations.AlterField(
            model_name='inclusion',
            name='second_phone_number_confirm',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='\u062a\u0623\u0643\u064a\u062f \u0631\u0642\u0645 \u0627\u0644\u0647\u0627\u062a\u0641 \u0627\u0644\u062b\u0627\u0646\u0648\u064a'),
        ),
        migrations.AlterField(
            model_name='inclusion',
            name='second_phone_owner',
            field=models.CharField(blank=True, choices=[('main_caregiver', '\u0648\u0644\u064a \u0627\u0644\u0623\u0645\u0631'), ('family member', '\u0623\u062d\u062f \u0627\u0641\u0631\u0627\u062f \u0627\u0644\u0639\u0627\u0626\u0644\u0629'), ('neighbors', '\u0627\u0644\u062c\u064a\u0627\u0631\u0627\u0646'), ('shawish', '\u0627\u0644\u0634\u0627\u0648\u064a\u0634')], max_length=100, null=True, verbose_name='\u0645\u0646 \u0627\u0644\u0634\u062e\u0635 \u0627\u0644\u0630\u064a \u064a\u062c\u064a\u0628 \u0639\u0644\u0649 \u0647\u0630\u0627 \u0627\u0644\u0631\u0642\u0645\u061f'),
        ),
        migrations.AlterField(
            model_name='rs',
            name='phone_number_confirm',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Phone number confirm'),
        ),
    ]
