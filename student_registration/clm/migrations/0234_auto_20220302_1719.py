# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2022-03-02 17:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clm', '0233_auto_20220217_1004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='abln_fc',
            name='lesson_modality',
            field=models.CharField(blank=True, choices=[('', '----------'), ('Online', ' \u0639\u0646 \u0628\u0639\u062f (\u0627\u0648\u0646\u0644\u0627\u064a\u0646)'), ('Present', '\u062d\u0636\u0648\u0631\u064a'), ('Blended', '\u0645\u062f\u0645\u062c')], max_length=100, null=True, verbose_name='\u0627\u0644\u062f\u0631\u0633 \u0627\u0644\u062d\u0627\u0644\u064a'),
        ),
        migrations.AlterField(
            model_name='abln_fc',
            name='steps_acquire_competency',
            field=models.CharField(blank=True, choices=[('', '----------'), ('Re-explain', '\u0627\u0639\u0627\u062f\u0629 \u0627\u0644\u0634\u0631\u062d'), ('Extra Howmework', '\u0627\u0646\u0634\u0637\u0629 \u0627\u0636\u0627\u0641\u064a\u0629'), ('other', '\u0622\u062e\u0631')], max_length=100, null=True, verbose_name='\u0645\u0627 \u0647\u064a \u0627\u0644\u062e\u0637\u0648\u0627\u062a \u0627\u0644\u062a\u0627\u0644\u064a\u0629 \u0644\u0645\u0633\u0627\u0639\u062f\u0629 \u0627\u0644\u0637\u0641\u0644 \u0639\u0644\u0649 \u0627\u0643\u062a\u0633\u0627\u0628 \u0627\u0644\u0643\u0641\u0627\u064a\u0629 \u0627\u0644\u0645\u0633\u062a\u0647\u062f\u0641\u0629'),
        ),
        migrations.AlterField(
            model_name='bln_fc',
            name='lesson_modality',
            field=models.CharField(blank=True, choices=[('', '----------'), ('Online', ' \u0639\u0646 \u0628\u0639\u062f (\u0627\u0648\u0646\u0644\u0627\u064a\u0646)'), ('Present', '\u062d\u0636\u0648\u0631\u064a'), ('Blended', '\u0645\u062f\u0645\u062c')], max_length=100, null=True, verbose_name='\u0627\u0644\u062f\u0631\u0633 \u0627\u0644\u062d\u0627\u0644\u064a'),
        ),
        migrations.AlterField(
            model_name='bln_fc',
            name='steps_acquire_competency',
            field=models.CharField(blank=True, choices=[('', '----------'), ('Re-explain', '\u0627\u0639\u0627\u062f\u0629 \u0627\u0644\u0634\u0631\u062d'), ('Extra Howmework', '\u0627\u0646\u0634\u0637\u0629 \u0627\u0636\u0627\u0641\u064a\u0629'), ('other', '\u0622\u062e\u0631')], max_length=100, null=True, verbose_name='\u0645\u0627 \u0647\u064a \u0627\u0644\u062e\u0637\u0648\u0627\u062a \u0627\u0644\u062a\u0627\u0644\u064a\u0629 \u0644\u0645\u0633\u0627\u0639\u062f\u0629 \u0627\u0644\u0637\u0641\u0644 \u0639\u0644\u0649 \u0627\u0643\u062a\u0633\u0627\u0628 \u0627\u0644\u0643\u0641\u0627\u064a\u0629 \u0627\u0644\u0645\u0633\u062a\u0647\u062f\u0641\u0629'),
        ),
        migrations.AlterField(
            model_name='bridging',
            name='registration_level',
            field=models.CharField(blank=True, choices=[('', '----------'), ('level_one', '\u0627\u0644\u0645\u0633\u062a\u0648\u0649 \u0627\u0644\u0623\u0648\u0644'), ('level_two', '\u0627\u0644\u0645\u0633\u062a\u0648\u0649 \u0627\u0644\u062b\u0627\u0646\u064a'), ('level_three', '\u0627\u0644\u0645\u0633\u062a\u0648\u0649 \u0627\u0644\u062b\u0627\u0644\u062b'), ('level_four', '\u0627\u0644\u0645\u0633\u062a\u0648\u0649 \u0627\u0644\u0631\u0627\u0628\u0639')], max_length=100, null=True, verbose_name='\u0645\u0633\u062a\u0648\u0649 \u0627\u0644\u062a\u0633\u062c\u064a\u0644'),
        ),
        migrations.AlterField(
            model_name='cbece_fc',
            name='lesson_modality',
            field=models.CharField(blank=True, choices=[('', '----------'), ('Online', ' \u0639\u0646 \u0628\u0639\u062f (\u0627\u0648\u0646\u0644\u0627\u064a\u0646)'), ('Present', '\u062d\u0636\u0648\u0631\u064a'), ('Blended', '\u0645\u062f\u0645\u062c')], max_length=100, null=True, verbose_name='\u0627\u0644\u062f\u0631\u0633 \u0627\u0644\u062d\u0627\u0644\u064a'),
        ),
        migrations.AlterField(
            model_name='cbece_fc',
            name='steps_acquire_competency',
            field=models.CharField(blank=True, choices=[('', '----------'), ('Re-explain', '\u0627\u0639\u0627\u062f\u0629 \u0627\u0644\u0634\u0631\u062d'), ('Extra Howmework', '\u0627\u0646\u0634\u0637\u0629 \u0627\u0636\u0627\u0641\u064a\u0629'), ('other', '\u0622\u062e\u0631')], max_length=100, null=True, verbose_name='\u0645\u0627 \u0647\u064a \u0627\u0644\u062e\u0637\u0648\u0627\u062a \u0627\u0644\u062a\u0627\u0644\u064a\u0629 \u0644\u0645\u0633\u0627\u0639\u062f\u0629 \u0627\u0644\u0637\u0641\u0644 \u0639\u0644\u0649 \u0627\u0643\u062a\u0633\u0627\u0628 \u0627\u0644\u0643\u0641\u0627\u064a\u0629 \u0627\u0644\u0645\u0633\u062a\u0647\u062f\u0641\u0629'),
        ),
        migrations.AlterField(
            model_name='rs',
            name='registration_level',
            field=models.CharField(blank=True, choices=[('', '----------'), ('level_one', '\u0627\u0644\u0645\u0633\u062a\u0648\u0649 \u0627\u0644\u0623\u0648\u0644'), ('level_two', '\u0627\u0644\u0645\u0633\u062a\u0648\u0649 \u0627\u0644\u062b\u0627\u0646\u064a'), ('level_three', '\u0627\u0644\u0645\u0633\u062a\u0648\u0649 \u0627\u0644\u062b\u0627\u0644\u062b'), ('level_four', '\u0627\u0644\u0645\u0633\u062a\u0648\u0649 \u0627\u0644\u0631\u0627\u0628\u0639')], max_length=100, null=True, verbose_name=' \u0646\u062a\u064a\u062c\u0629 \u0627\u0644\u062a\u0639\u0644\u0645'),
        ),
        migrations.AlterField(
            model_name='rs_fc',
            name='fc_type',
            field=models.CharField(blank=True, choices=[('pre-arabic', 'Pre Arabic'), ('pre-math', 'Pre Math'), ('pre-language', 'Pre Language'), ('pre-science', 'Pre Science'), ('pre-biology', 'Pre Biology'), ('pre-chemistry', 'Pre Chemistry'), ('pre-physics', 'Pre Physics'), ('post-arabic', 'Post Arabic'), ('post-math', 'Post Math'), ('post-language', 'Post Language'), ('post-science', 'Post Science'), ('post-biology', 'Post Biology'), ('post-chemistry', 'Post Chemistry'), ('post-physics', 'Post Physics'), ('arabic', '\u0627\u0644\u0644\u063a\u0629 \u0627\u0644\u0639\u0631\u0628\u064a\u0629'), ('language', 'Language'), ('math', '\u0627\u0644\u0631\u064a\u0627\u0636\u064a\u0627\u062a'), ('science', '\u0627\u0644\u0639\u0644\u0648\u0645'), ('biology', '\u0639\u0644\u0648\u0645 \u0627\u0644\u062d\u064a\u0627\u0629'), ('chemistry', '\u0643\u064a\u0645\u064a\u0627\u0621'), ('physics', '\u0641\u064a\u0632\u064a\u0627\u0621')], max_length=50, null=True, verbose_name='\u0646\u0648\u0639 \u0627\u0644\u0639\u0645\u0644'),
        ),
        migrations.AlterField(
            model_name='rs_fc',
            name='lesson_modality',
            field=models.CharField(blank=True, choices=[('', '----------'), ('Online', ' \u0639\u0646 \u0628\u0639\u062f (\u0627\u0648\u0646\u0644\u0627\u064a\u0646)'), ('Present', '\u062d\u0636\u0648\u0631\u064a'), ('Blended', '\u0645\u062f\u0645\u062c')], max_length=100, null=True, verbose_name='\u0627\u0644\u062f\u0631\u0633 \u0627\u0644\u062d\u0627\u0644\u064a'),
        ),
        migrations.AlterField(
            model_name='rs_fc',
            name='steps_acquire_competency',
            field=models.CharField(blank=True, choices=[('', '----------'), ('Re-explain', '\u0627\u0639\u0627\u062f\u0629 \u0627\u0644\u0634\u0631\u062d'), ('Extra Howmework', '\u0627\u0646\u0634\u0637\u0629 \u0627\u0636\u0627\u0641\u064a\u0629'), ('other', '\u0622\u062e\u0631')], max_length=100, null=True, verbose_name='\u0645\u0627 \u0647\u064a \u0627\u0644\u062e\u0637\u0648\u0627\u062a \u0627\u0644\u062a\u0627\u0644\u064a\u0629 \u0644\u0645\u0633\u0627\u0639\u062f\u0629 \u0627\u0644\u0637\u0641\u0644 \u0639\u0644\u0649 \u0627\u0643\u062a\u0633\u0627\u0628 \u0627\u0644\u0643\u0641\u0627\u064a\u0629 \u0627\u0644\u0645\u0633\u062a\u0647\u062f\u0641\u0629'),
        ),
    ]
