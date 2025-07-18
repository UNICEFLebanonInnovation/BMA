# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2020-03-23 14:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clm', '0095_auto_20200323_1606'),
    ]

    operations = [
        migrations.AddField(
            model_name='abln',
            name='arabic',
            field=models.TextField(blank=True, null=True, verbose_name='\u0627\u0644\u0631\u062c\u0627\u0621 \u0625\u062f\u062e\u0627\u0644 \u0645\u062c\u0645\u0648\u0639 \u0627\u0644\u0646\u062a\u064a\u062c\u0629 \u0644\u0647\u0630\u0647 \u0627\u0644\u0645\u0627\u062f\u0629'),
        ),
        migrations.AddField(
            model_name='abln',
            name='attended_math',
            field=models.CharField(blank=True, choices=[('yes', '\u0646\u0639\u0645'), ('no', '\u0643\u0644\u0627')], max_length=100, null=True, verbose_name='\u0623\u062a\u0645 \u0625\u0645\u062a\u062d\u0627\u0646 \u0645\u0627\u062f\u0629 \u0627\u0644\u0631\u064a\u0627\u0636\u064a\u0627\u062a'),
        ),
        migrations.AddField(
            model_name='abln',
            name='attended_psychomotor',
            field=models.CharField(blank=True, choices=[('yes', '\u0646\u0639\u0645'), ('no', '\u0643\u0644\u0627')], max_length=100, null=True, verbose_name='\u062a\u0637\u0648\u0631 \u0641\u0646\u064a \u0625\u0628\u062f\u0627\u0639\u064a'),
        ),
        migrations.AddField(
            model_name='abln',
            name='attended_social',
            field=models.CharField(blank=True, choices=[('yes', '\u0646\u0639\u0645'), ('no', '\u0643\u0644\u0627')], max_length=100, null=True, verbose_name='\u0627\u0644\u062a\u0637\u0648\u0631 \u0627\u0644\u0627\u062c\u062a\u0645\u0627\u0639\u064a / \u0627\u0644\u0639\u0627\u0637\u0641\u064a'),
        ),
        migrations.AddField(
            model_name='abln',
            name='math',
            field=models.TextField(blank=True, null=True, verbose_name='\u0627\u0644\u0631\u062c\u0627\u0621 \u0625\u062f\u062e\u0627\u0644 \u0645\u062c\u0645\u0648\u0639 \u0627\u0644\u0646\u062a\u064a\u062c\u0629 \u0644\u0647\u0630\u0647 \u0627\u0644\u0645\u0627\u062f\u0629'),
        ),
        migrations.AddField(
            model_name='abln',
            name='psychomotor',
            field=models.TextField(blank=True, null=True, verbose_name='\u0627\u0644\u0631\u062c\u0627\u0621 \u0625\u062f\u062e\u0627\u0644 \u0645\u062c\u0645\u0648\u0639 \u0627\u0644\u0646\u062a\u064a\u062c\u0629 \u0644\u0647\u0630\u0647 \u0627\u0644\u0645\u0627\u062f\u0629'),
        ),
        migrations.AddField(
            model_name='abln',
            name='social',
            field=models.TextField(blank=True, null=True, verbose_name='\u0627\u0644\u0631\u062c\u0627\u0621 \u0625\u062f\u062e\u0627\u0644 \u0645\u062c\u0645\u0648\u0639 \u0627\u0644\u0646\u062a\u064a\u062c\u0629 \u0644\u0647\u0630\u0647 \u0627\u0644\u0645\u0627\u062f\u0629'),
        ),
        migrations.AddField(
            model_name='bln',
            name='arabic',
            field=models.TextField(blank=True, null=True, verbose_name='\u0627\u0644\u0631\u062c\u0627\u0621 \u0625\u062f\u062e\u0627\u0644 \u0645\u062c\u0645\u0648\u0639 \u0627\u0644\u0646\u062a\u064a\u062c\u0629 \u0644\u0647\u0630\u0647 \u0627\u0644\u0645\u0627\u062f\u0629'),
        ),
        migrations.AddField(
            model_name='bln',
            name='attended_math',
            field=models.CharField(blank=True, choices=[('yes', '\u0646\u0639\u0645'), ('no', '\u0643\u0644\u0627')], max_length=100, null=True, verbose_name='\u0623\u062a\u0645 \u0625\u0645\u062a\u062d\u0627\u0646 \u0645\u0627\u062f\u0629 \u0627\u0644\u0631\u064a\u0627\u0636\u064a\u0627\u062a'),
        ),
        migrations.AddField(
            model_name='bln',
            name='attended_psychomotor',
            field=models.CharField(blank=True, choices=[('yes', '\u0646\u0639\u0645'), ('no', '\u0643\u0644\u0627')], max_length=100, null=True, verbose_name='\u062a\u0637\u0648\u0631 \u0641\u0646\u064a \u0625\u0628\u062f\u0627\u0639\u064a'),
        ),
        migrations.AddField(
            model_name='bln',
            name='attended_social',
            field=models.CharField(blank=True, choices=[('yes', '\u0646\u0639\u0645'), ('no', '\u0643\u0644\u0627')], max_length=100, null=True, verbose_name='\u0627\u0644\u062a\u0637\u0648\u0631 \u0627\u0644\u0627\u062c\u062a\u0645\u0627\u0639\u064a / \u0627\u0644\u0639\u0627\u0637\u0641\u064a'),
        ),
        migrations.AddField(
            model_name='bln',
            name='math',
            field=models.TextField(blank=True, null=True, verbose_name='\u0627\u0644\u0631\u062c\u0627\u0621 \u0625\u062f\u062e\u0627\u0644 \u0645\u062c\u0645\u0648\u0639 \u0627\u0644\u0646\u062a\u064a\u062c\u0629 \u0644\u0647\u0630\u0647 \u0627\u0644\u0645\u0627\u062f\u0629'),
        ),
        migrations.AddField(
            model_name='bln',
            name='psychomotor',
            field=models.TextField(blank=True, null=True, verbose_name='\u0627\u0644\u0631\u062c\u0627\u0621 \u0625\u062f\u062e\u0627\u0644 \u0645\u062c\u0645\u0648\u0639 \u0627\u0644\u0646\u062a\u064a\u062c\u0629 \u0644\u0647\u0630\u0647 \u0627\u0644\u0645\u0627\u062f\u0629'),
        ),
        migrations.AddField(
            model_name='bln',
            name='social',
            field=models.TextField(blank=True, null=True, verbose_name='\u0627\u0644\u0631\u062c\u0627\u0621 \u0625\u062f\u062e\u0627\u0644 \u0645\u062c\u0645\u0648\u0639 \u0627\u0644\u0646\u062a\u064a\u062c\u0629 \u0644\u0647\u0630\u0647 \u0627\u0644\u0645\u0627\u062f\u0629'),
        ),
        migrations.AddField(
            model_name='cbece',
            name='arabic',
            field=models.TextField(blank=True, null=True, verbose_name='\u0627\u0644\u0631\u062c\u0627\u0621 \u0625\u062f\u062e\u0627\u0644 \u0645\u062c\u0645\u0648\u0639 \u0627\u0644\u0646\u062a\u064a\u062c\u0629 \u0644\u0647\u0630\u0647 \u0627\u0644\u0645\u0627\u062f\u0629'),
        ),
        migrations.AddField(
            model_name='cbece',
            name='attended_math',
            field=models.CharField(blank=True, choices=[('yes', '\u0646\u0639\u0645'), ('no', '\u0643\u0644\u0627')], max_length=100, null=True, verbose_name='\u0623\u062a\u0645 \u0625\u0645\u062a\u062d\u0627\u0646 \u0645\u0627\u062f\u0629 \u0627\u0644\u0631\u064a\u0627\u0636\u064a\u0627\u062a'),
        ),
        migrations.AddField(
            model_name='cbece',
            name='attended_psychomotor',
            field=models.CharField(blank=True, choices=[('yes', '\u0646\u0639\u0645'), ('no', '\u0643\u0644\u0627')], max_length=100, null=True, verbose_name='\u062a\u0637\u0648\u0631 \u0641\u0646\u064a \u0625\u0628\u062f\u0627\u0639\u064a'),
        ),
        migrations.AddField(
            model_name='cbece',
            name='attended_social',
            field=models.CharField(blank=True, choices=[('yes', '\u0646\u0639\u0645'), ('no', '\u0643\u0644\u0627')], max_length=100, null=True, verbose_name='\u0627\u0644\u062a\u0637\u0648\u0631 \u0627\u0644\u0627\u062c\u062a\u0645\u0627\u0639\u064a / \u0627\u0644\u0639\u0627\u0637\u0641\u064a'),
        ),
        migrations.AddField(
            model_name='cbece',
            name='math',
            field=models.TextField(blank=True, null=True, verbose_name='\u0627\u0644\u0631\u062c\u0627\u0621 \u0625\u062f\u062e\u0627\u0644 \u0645\u062c\u0645\u0648\u0639 \u0627\u0644\u0646\u062a\u064a\u062c\u0629 \u0644\u0647\u0630\u0647 \u0627\u0644\u0645\u0627\u062f\u0629'),
        ),
        migrations.AddField(
            model_name='cbece',
            name='psychomotor',
            field=models.TextField(blank=True, null=True, verbose_name='\u0627\u0644\u0631\u062c\u0627\u0621 \u0625\u062f\u062e\u0627\u0644 \u0645\u062c\u0645\u0648\u0639 \u0627\u0644\u0646\u062a\u064a\u062c\u0629 \u0644\u0647\u0630\u0647 \u0627\u0644\u0645\u0627\u062f\u0629'),
        ),
        migrations.AddField(
            model_name='cbece',
            name='social',
            field=models.TextField(blank=True, null=True, verbose_name='\u0627\u0644\u0631\u062c\u0627\u0621 \u0625\u062f\u062e\u0627\u0644 \u0645\u062c\u0645\u0648\u0639 \u0627\u0644\u0646\u062a\u064a\u062c\u0629 \u0644\u0647\u0630\u0647 \u0627\u0644\u0645\u0627\u062f\u0629'),
        ),
        migrations.AddField(
            model_name='rs',
            name='arabic',
            field=models.TextField(blank=True, null=True, verbose_name='\u0627\u0644\u0631\u062c\u0627\u0621 \u0625\u062f\u062e\u0627\u0644 \u0645\u062c\u0645\u0648\u0639 \u0627\u0644\u0646\u062a\u064a\u062c\u0629 \u0644\u0647\u0630\u0647 \u0627\u0644\u0645\u0627\u062f\u0629'),
        ),
        migrations.AddField(
            model_name='rs',
            name='attended_math',
            field=models.CharField(blank=True, choices=[('yes', '\u0646\u0639\u0645'), ('no', '\u0643\u0644\u0627')], max_length=100, null=True, verbose_name='\u0623\u062a\u0645 \u0625\u0645\u062a\u062d\u0627\u0646 \u0645\u0627\u062f\u0629 \u0627\u0644\u0631\u064a\u0627\u0636\u064a\u0627\u062a'),
        ),
        migrations.AddField(
            model_name='rs',
            name='attended_psychomotor',
            field=models.CharField(blank=True, choices=[('yes', '\u0646\u0639\u0645'), ('no', '\u0643\u0644\u0627')], max_length=100, null=True, verbose_name='\u062a\u0637\u0648\u0631 \u0641\u0646\u064a \u0625\u0628\u062f\u0627\u0639\u064a'),
        ),
        migrations.AddField(
            model_name='rs',
            name='attended_social',
            field=models.CharField(blank=True, choices=[('yes', '\u0646\u0639\u0645'), ('no', '\u0643\u0644\u0627')], max_length=100, null=True, verbose_name='\u0627\u0644\u062a\u0637\u0648\u0631 \u0627\u0644\u0627\u062c\u062a\u0645\u0627\u0639\u064a / \u0627\u0644\u0639\u0627\u0637\u0641\u064a'),
        ),
        migrations.AddField(
            model_name='rs',
            name='math',
            field=models.TextField(blank=True, null=True, verbose_name='\u0627\u0644\u0631\u062c\u0627\u0621 \u0625\u062f\u062e\u0627\u0644 \u0645\u062c\u0645\u0648\u0639 \u0627\u0644\u0646\u062a\u064a\u062c\u0629 \u0644\u0647\u0630\u0647 \u0627\u0644\u0645\u0627\u062f\u0629'),
        ),
        migrations.AddField(
            model_name='rs',
            name='psychomotor',
            field=models.TextField(blank=True, null=True, verbose_name='\u0627\u0644\u0631\u062c\u0627\u0621 \u0625\u062f\u062e\u0627\u0644 \u0645\u062c\u0645\u0648\u0639 \u0627\u0644\u0646\u062a\u064a\u062c\u0629 \u0644\u0647\u0630\u0647 \u0627\u0644\u0645\u0627\u062f\u0629'),
        ),
        migrations.AddField(
            model_name='rs',
            name='social',
            field=models.TextField(blank=True, null=True, verbose_name='\u0627\u0644\u0631\u062c\u0627\u0621 \u0625\u062f\u062e\u0627\u0644 \u0645\u062c\u0645\u0648\u0639 \u0627\u0644\u0646\u062a\u064a\u062c\u0629 \u0644\u0647\u0630\u0647 \u0627\u0644\u0645\u0627\u062f\u0629'),
        ),
    ]
