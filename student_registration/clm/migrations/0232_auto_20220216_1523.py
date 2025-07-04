# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2022-02-16 15:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clm', '0231_bridging'),
    ]

    operations = [
        migrations.AddField(
            model_name='abln_fc',
            name='child_performance_evaluation',
            field=models.CharField(blank=True, choices=[('', '----------'), ('excellent', '\u0645\u0645\u062a\u0627\u0632'), ('good', '\u062c\u064a\u0651\u062f'), ('need assistance', 'Needs assistance')], max_length=100, null=True, verbose_name='Child Lesson Evaluation'),
        ),
        migrations.AddField(
            model_name='abln_fc',
            name='lesson_modality',
            field=models.CharField(blank=True, choices=[('', '----------'), ('Online', 'Online'), ('Present', '\u062d\u0627\u0636\u0631'), ('Blended', 'Blended')], max_length=100, null=True, verbose_name='Lesson Modality'),
        ),
        migrations.AddField(
            model_name='abln_fc',
            name='steps_acquire_competency',
            field=models.CharField(blank=True, choices=[('', '----------'), ('Re-explain', 'Re-explain'), ('Extra Howmework', 'Extra Howmework'), ('other', '\u0622\u062e\u0631')], max_length=100, null=True, verbose_name='Steps to help the child acquire the targeted competency'),
        ),
        migrations.AddField(
            model_name='abln_fc',
            name='steps_acquire_competency_other',
            field=models.TextField(blank=True, null=True, verbose_name='\u064a\u0631\u062c\u0649 \u0627\u0644\u062a\u062d\u062f\u064a\u062f'),
        ),
        migrations.AddField(
            model_name='bln_fc',
            name='child_performance_evaluation',
            field=models.CharField(blank=True, choices=[('', '----------'), ('excellent', '\u0645\u0645\u062a\u0627\u0632'), ('good', '\u062c\u064a\u0651\u062f'), ('need assistance', 'Needs assistance')], max_length=100, null=True, verbose_name='Child Lesson Evaluation'),
        ),
        migrations.AddField(
            model_name='bln_fc',
            name='lesson_modality',
            field=models.CharField(blank=True, choices=[('', '----------'), ('Online', 'Online'), ('Present', '\u062d\u0627\u0636\u0631'), ('Blended', 'Blended')], max_length=100, null=True, verbose_name='Lesson Modality'),
        ),
        migrations.AddField(
            model_name='bln_fc',
            name='steps_acquire_competency',
            field=models.CharField(blank=True, choices=[('', '----------'), ('Re-explain', 'Re-explain'), ('Extra Howmework', 'Extra Howmework'), ('other', '\u0622\u062e\u0631')], max_length=100, null=True, verbose_name='Steps to help the child acquire the targeted competency'),
        ),
        migrations.AddField(
            model_name='bln_fc',
            name='steps_acquire_competency_other',
            field=models.TextField(blank=True, null=True, verbose_name='\u064a\u0631\u062c\u0649 \u0627\u0644\u062a\u062d\u062f\u064a\u062f'),
        ),
        migrations.AddField(
            model_name='cbece_fc',
            name='child_performance_evaluation',
            field=models.CharField(blank=True, choices=[('', '----------'), ('excellent', '\u0645\u0645\u062a\u0627\u0632'), ('good', '\u062c\u064a\u0651\u062f'), ('need assistance', 'Needs assistance')], max_length=100, null=True, verbose_name='Child Lesson Evaluation'),
        ),
        migrations.AddField(
            model_name='cbece_fc',
            name='lesson_modality',
            field=models.CharField(blank=True, choices=[('', '----------'), ('Online', 'Online'), ('Present', '\u062d\u0627\u0636\u0631'), ('Blended', 'Blended')], max_length=100, null=True, verbose_name='Lesson Modality'),
        ),
        migrations.AddField(
            model_name='cbece_fc',
            name='steps_acquire_competency',
            field=models.CharField(blank=True, choices=[('', '----------'), ('Re-explain', 'Re-explain'), ('Extra Howmework', 'Extra Howmework'), ('other', '\u0622\u062e\u0631')], max_length=100, null=True, verbose_name='Steps to help the child acquire the targeted competency'),
        ),
        migrations.AddField(
            model_name='cbece_fc',
            name='steps_acquire_competency_other',
            field=models.TextField(blank=True, null=True, verbose_name='\u064a\u0631\u062c\u0649 \u0627\u0644\u062a\u062d\u062f\u064a\u062f'),
        ),
        migrations.AddField(
            model_name='rs_fc',
            name='child_performance_evaluation',
            field=models.CharField(blank=True, choices=[('', '----------'), ('excellent', '\u0645\u0645\u062a\u0627\u0632'), ('good', '\u062c\u064a\u0651\u062f'), ('need assistance', 'Needs assistance')], max_length=100, null=True, verbose_name='Child Lesson Evaluation'),
        ),
        migrations.AddField(
            model_name='rs_fc',
            name='lesson_modality',
            field=models.CharField(blank=True, choices=[('', '----------'), ('Online', 'Online'), ('Present', '\u062d\u0627\u0636\u0631'), ('Blended', 'Blended')], max_length=100, null=True, verbose_name='Lesson Modality'),
        ),
        migrations.AddField(
            model_name='rs_fc',
            name='steps_acquire_competency',
            field=models.CharField(blank=True, choices=[('', '----------'), ('Re-explain', 'Re-explain'), ('Extra Howmework', 'Extra Howmework'), ('other', '\u0622\u062e\u0631')], max_length=100, null=True, verbose_name='Steps to help the child acquire the targeted competency'),
        ),
        migrations.AddField(
            model_name='rs_fc',
            name='steps_acquire_competency_other',
            field=models.TextField(blank=True, null=True, verbose_name='\u064a\u0631\u062c\u0649 \u0627\u0644\u062a\u062d\u062f\u064a\u062f'),
        ),
        migrations.AlterField(
            model_name='abln_fc',
            name='action_to_taken',
            field=models.CharField(blank=True, choices=[('', '----------'), ('yes', '\u0646\u0639\u0645'), ('no', '\u0643\u0644\u0627')], max_length=10, null=True, verbose_name='\u0647\u0644 \u0645\u0646 \u0625\u062c\u0631\u0627\u0621\u0627\u062a \u0645\u0639\u064a\u0646\u0629 \u064a\u062c\u0628 \u0627\u062a\u062e\u0627\u0630\u0647\u0627 \u0645\u0639 \u0647\u0630\u0627 \u0627\u0644\u0637\u0641\u0644 \u0642\u0628\u0644 \u0627\u0644\u0627\u0646\u062a\u0642\u0627\u0644 \u0627\u0644\u0649 \u0627\u0644\u062f\u0631\u0633 \u0627\u0644\u0642\u0627\u062f\u0645 \u0644\u0636\u0645\u0627\u0646 \u0645\u0634\u0627\u0631\u0643\u0629 \u0623\u0641\u0636\u0644\u061f'),
        ),
        migrations.AlterField(
            model_name='abln_fc',
            name='child_cant_access_resources',
            field=models.CharField(blank=True, choices=[('', '----------'), ('yes', '\u0646\u0639\u0645'), ('no', '\u0643\u0644\u0627')], max_length=10, null=True, verbose_name='\u0647\u0644 \u0644\u0627\u062d\u0638\u062a \u0623\u0646 \u0627\u0644\u0637\u0641\u0644 \u0644\u0627 \u064a\u0633\u062a\u0637\u064a\u0639 \u0627\u0644\u062d\u0635\u0648\u0644 \u0639\u0644\u0649 \u0627\u0644\u0647\u0627\u062a\u0641 \u0623\u0648 \u0627\u0644\u0648\u0633\u0627\u0626\u0644 \u0627\u0644\u0636\u0631\u0648\u0631\u064a\u0629 \u0644\u0625\u0643\u0645\u0627\u0644 \u0645\u062a\u0637\u0644\u0628\u0627\u062a \u0627\u0644\u062f\u0631\u0633 \u0627\u0646 \u0643\u0627\u0646 \u062d\u0636\u0648\u0631\u064a\u0627 \u0627\u0648 \u0639\u0646 \u0628\u0639\u062f\u061f'),
        ),
        migrations.AlterField(
            model_name='abln_fc',
            name='sessions_participated',
            field=models.CharField(blank=True, choices=[('', '----------'), ('participating_in_all_session', '\u0634\u0627\u0631\u0643 \u0641\u064a \u062c\u0645\u064a\u0639 \u0627\u0644\u062d\u0635\u0635'), ('participating_in_some_session', '\u0634\u0627\u0631\u0643 \u0641\u064a \u0628\u0639\u0636 \u0627\u0644\u062d\u0635\u0635'), ('not_participating_at_all', '\u0644\u0645 \u064a\u0634\u0627\u0631\u0643 \u0623\u0628\u062f\u064b\u0627')], max_length=100, null=True, verbose_name='How many session did this child participate in online classes this week?'),
        ),
        migrations.AlterField(
            model_name='abln_fc',
            name='share_expectations',
            field=models.CharField(blank=True, choices=[('', '----------'), ('yes', '\u0646\u0639\u0645'), ('no', '\u0643\u0644\u0627')], max_length=10, null=True, verbose_name='\u0647\u0644 \u062a\u0645 \u0627\u0639\u0644\u0627\u0645 \u0627\u0644\u0623\u0647\u0644 \u0645\u0627 \u0647\u0648 \u0645\u062a\u0648\u0642\u0639 \u0645\u0646 \u0645\u0634\u0627\u0631\u0643\u0629 \u0627\u0644\u0637\u0641\u0644 \u0641\u064a \u0627\u0644\u062a\u0639\u0644\u0645 \u0623\u0633\u0628\u0648\u0639\u064a\u064b\u0627 \u061f'),
        ),
        migrations.AlterField(
            model_name='abln_fc',
            name='targeted_competencies',
            field=models.TextField(blank=True, null=True, verbose_name='\u0627\u0644\u0643\u0641\u0627\u064a\u0627\u062a \u0627\u0644\u0645\u0633\u062a\u0647\u062f\u0641\u0629'),
        ),
        migrations.AlterField(
            model_name='bln_fc',
            name='action_to_taken',
            field=models.CharField(blank=True, choices=[('', '----------'), ('yes', '\u0646\u0639\u0645'), ('no', '\u0643\u0644\u0627')], max_length=10, null=True, verbose_name='\u0647\u0644 \u0645\u0646 \u0625\u062c\u0631\u0627\u0621\u0627\u062a \u0645\u0639\u064a\u0646\u0629 \u064a\u062c\u0628 \u0627\u062a\u062e\u0627\u0630\u0647\u0627 \u0645\u0639 \u0647\u0630\u0627 \u0627\u0644\u0637\u0641\u0644 \u0642\u0628\u0644 \u0627\u0644\u0627\u0646\u062a\u0642\u0627\u0644 \u0627\u0644\u0649 \u0627\u0644\u062f\u0631\u0633 \u0627\u0644\u0642\u0627\u062f\u0645 \u0644\u0636\u0645\u0627\u0646 \u0645\u0634\u0627\u0631\u0643\u0629 \u0623\u0641\u0636\u0644\u061f'),
        ),
        migrations.AlterField(
            model_name='bln_fc',
            name='child_cant_access_resources',
            field=models.CharField(blank=True, choices=[('', '----------'), ('yes', '\u0646\u0639\u0645'), ('no', '\u0643\u0644\u0627')], max_length=10, null=True, verbose_name='\u0647\u0644 \u0644\u0627\u062d\u0638\u062a \u0623\u0646 \u0627\u0644\u0637\u0641\u0644 \u0644\u0627 \u064a\u0633\u062a\u0637\u064a\u0639 \u0627\u0644\u062d\u0635\u0648\u0644 \u0639\u0644\u0649 \u0627\u0644\u0647\u0627\u062a\u0641 \u0623\u0648 \u0627\u0644\u0648\u0633\u0627\u0626\u0644 \u0627\u0644\u0636\u0631\u0648\u0631\u064a\u0629 \u0644\u0625\u0643\u0645\u0627\u0644 \u0645\u062a\u0637\u0644\u0628\u0627\u062a \u0627\u0644\u062f\u0631\u0633 \u0627\u0646 \u0643\u0627\u0646 \u062d\u0636\u0648\u0631\u064a\u0627 \u0627\u0648 \u0639\u0646 \u0628\u0639\u062f\u061f'),
        ),
        migrations.AlterField(
            model_name='bln_fc',
            name='sessions_participated',
            field=models.CharField(blank=True, choices=[('', '----------'), ('participating_in_all_session', '\u0634\u0627\u0631\u0643 \u0641\u064a \u062c\u0645\u064a\u0639 \u0627\u0644\u062d\u0635\u0635'), ('participating_in_some_session', '\u0634\u0627\u0631\u0643 \u0641\u064a \u0628\u0639\u0636 \u0627\u0644\u062d\u0635\u0635'), ('not_participating_at_all', '\u0644\u0645 \u064a\u0634\u0627\u0631\u0643 \u0623\u0628\u062f\u064b\u0627')], max_length=100, null=True, verbose_name='How many session did this child participate in online classes this week?'),
        ),
        migrations.AlterField(
            model_name='bln_fc',
            name='share_expectations',
            field=models.CharField(blank=True, choices=[('', '----------'), ('yes', '\u0646\u0639\u0645'), ('no', '\u0643\u0644\u0627')], max_length=10, null=True, verbose_name='\u0647\u0644 \u062a\u0645 \u0627\u0639\u0644\u0627\u0645 \u0627\u0644\u0623\u0647\u0644 \u0645\u0627 \u0647\u0648 \u0645\u062a\u0648\u0642\u0639 \u0645\u0646 \u0645\u0634\u0627\u0631\u0643\u0629 \u0627\u0644\u0637\u0641\u0644 \u0641\u064a \u0627\u0644\u062a\u0639\u0644\u0645 \u0623\u0633\u0628\u0648\u0639\u064a\u064b\u0627 \u061f'),
        ),
        migrations.AlterField(
            model_name='bln_fc',
            name='targeted_competencies',
            field=models.TextField(blank=True, null=True, verbose_name='\u0627\u0644\u0643\u0641\u0627\u064a\u0627\u062a \u0627\u0644\u0645\u0633\u062a\u0647\u062f\u0641\u0629'),
        ),
        migrations.AlterField(
            model_name='cbece_fc',
            name='action_to_taken',
            field=models.CharField(blank=True, choices=[('', '----------'), ('yes', '\u0646\u0639\u0645'), ('no', '\u0643\u0644\u0627')], max_length=10, null=True, verbose_name='\u0647\u0644 \u0645\u0646 \u0625\u062c\u0631\u0627\u0621\u0627\u062a \u0645\u0639\u064a\u0646\u0629 \u064a\u062c\u0628 \u0627\u062a\u062e\u0627\u0630\u0647\u0627 \u0645\u0639 \u0647\u0630\u0627 \u0627\u0644\u0637\u0641\u0644 \u0642\u0628\u0644 \u0627\u0644\u0627\u0646\u062a\u0642\u0627\u0644 \u0627\u0644\u0649 \u0627\u0644\u062f\u0631\u0633 \u0627\u0644\u0642\u0627\u062f\u0645 \u0644\u0636\u0645\u0627\u0646 \u0645\u0634\u0627\u0631\u0643\u0629 \u0623\u0641\u0636\u0644\u061f'),
        ),
        migrations.AlterField(
            model_name='cbece_fc',
            name='child_cant_access_resources',
            field=models.CharField(blank=True, choices=[('', '----------'), ('yes', '\u0646\u0639\u0645'), ('no', '\u0643\u0644\u0627')], max_length=10, null=True, verbose_name='\u0647\u0644 \u0644\u0627\u062d\u0638\u062a \u0623\u0646 \u0627\u0644\u0637\u0641\u0644 \u0644\u0627 \u064a\u0633\u062a\u0637\u064a\u0639 \u0627\u0644\u062d\u0635\u0648\u0644 \u0639\u0644\u0649 \u0627\u0644\u0647\u0627\u062a\u0641 \u0623\u0648 \u0627\u0644\u0648\u0633\u0627\u0626\u0644 \u0627\u0644\u0636\u0631\u0648\u0631\u064a\u0629 \u0644\u0625\u0643\u0645\u0627\u0644 \u0645\u062a\u0637\u0644\u0628\u0627\u062a \u0627\u0644\u062f\u0631\u0633 \u0627\u0646 \u0643\u0627\u0646 \u062d\u0636\u0648\u0631\u064a\u0627 \u0627\u0648 \u0639\u0646 \u0628\u0639\u062f\u061f'),
        ),
        migrations.AlterField(
            model_name='cbece_fc',
            name='sessions_participated',
            field=models.CharField(blank=True, choices=[('', '----------'), ('participating_in_all_session', '\u0634\u0627\u0631\u0643 \u0641\u064a \u062c\u0645\u064a\u0639 \u0627\u0644\u062d\u0635\u0635'), ('participating_in_some_session', '\u0634\u0627\u0631\u0643 \u0641\u064a \u0628\u0639\u0636 \u0627\u0644\u062d\u0635\u0635'), ('not_participating_at_all', '\u0644\u0645 \u064a\u0634\u0627\u0631\u0643 \u0623\u0628\u062f\u064b\u0627')], max_length=100, null=True, verbose_name='How many session did this child participate in online classes this week?'),
        ),
        migrations.AlterField(
            model_name='cbece_fc',
            name='share_expectations',
            field=models.CharField(blank=True, choices=[('', '----------'), ('yes', '\u0646\u0639\u0645'), ('no', '\u0643\u0644\u0627')], max_length=10, null=True, verbose_name='\u0647\u0644 \u062a\u0645 \u0627\u0639\u0644\u0627\u0645 \u0627\u0644\u0623\u0647\u0644 \u0645\u0627 \u0647\u0648 \u0645\u062a\u0648\u0642\u0639 \u0645\u0646 \u0645\u0634\u0627\u0631\u0643\u0629 \u0627\u0644\u0637\u0641\u0644 \u0641\u064a \u0627\u0644\u062a\u0639\u0644\u0645 \u0623\u0633\u0628\u0648\u0639\u064a\u064b\u0627 \u061f'),
        ),
        migrations.AlterField(
            model_name='cbece_fc',
            name='targeted_competencies',
            field=models.TextField(blank=True, null=True, verbose_name='\u0627\u0644\u0643\u0641\u0627\u064a\u0627\u062a \u0627\u0644\u0645\u0633\u062a\u0647\u062f\u0641\u0629'),
        ),
        migrations.AlterField(
            model_name='rs_fc',
            name='action_to_taken',
            field=models.CharField(blank=True, choices=[('', '----------'), ('yes', '\u0646\u0639\u0645'), ('no', '\u0643\u0644\u0627')], max_length=10, null=True, verbose_name='\u0647\u0644 \u0645\u0646 \u0625\u062c\u0631\u0627\u0621\u0627\u062a \u0645\u0639\u064a\u0646\u0629 \u064a\u062c\u0628 \u0627\u062a\u062e\u0627\u0630\u0647\u0627 \u0645\u0639 \u0647\u0630\u0627 \u0627\u0644\u0637\u0641\u0644 \u0642\u0628\u0644 \u0627\u0644\u0627\u0646\u062a\u0642\u0627\u0644 \u0627\u0644\u0649 \u0627\u0644\u062f\u0631\u0633 \u0627\u0644\u0642\u0627\u062f\u0645 \u0644\u0636\u0645\u0627\u0646 \u0645\u0634\u0627\u0631\u0643\u0629 \u0623\u0641\u0636\u0644\u061f'),
        ),
        migrations.AlterField(
            model_name='rs_fc',
            name='child_cant_access_resources',
            field=models.CharField(blank=True, choices=[('', '----------'), ('yes', '\u0646\u0639\u0645'), ('no', '\u0643\u0644\u0627')], max_length=10, null=True, verbose_name='\u0647\u0644 \u0644\u0627\u062d\u0638\u062a \u0623\u0646 \u0627\u0644\u0637\u0641\u0644 \u0644\u0627 \u064a\u0633\u062a\u0637\u064a\u0639 \u0627\u0644\u062d\u0635\u0648\u0644 \u0639\u0644\u0649 \u0627\u0644\u0647\u0627\u062a\u0641 \u0623\u0648 \u0627\u0644\u0648\u0633\u0627\u0626\u0644 \u0627\u0644\u0636\u0631\u0648\u0631\u064a\u0629 \u0644\u0625\u0643\u0645\u0627\u0644 \u0645\u062a\u0637\u0644\u0628\u0627\u062a \u0627\u0644\u062f\u0631\u0633 \u0627\u0646 \u0643\u0627\u0646 \u062d\u0636\u0648\u0631\u064a\u0627 \u0627\u0648 \u0639\u0646 \u0628\u0639\u062f\u061f'),
        ),
        migrations.AlterField(
            model_name='rs_fc',
            name='sessions_participated',
            field=models.CharField(blank=True, choices=[('', '----------'), ('participating_in_all_session', '\u0634\u0627\u0631\u0643 \u0641\u064a \u062c\u0645\u064a\u0639 \u0627\u0644\u062d\u0635\u0635'), ('participating_in_some_session', '\u0634\u0627\u0631\u0643 \u0641\u064a \u0628\u0639\u0636 \u0627\u0644\u062d\u0635\u0635'), ('not_participating_at_all', '\u0644\u0645 \u064a\u0634\u0627\u0631\u0643 \u0623\u0628\u062f\u064b\u0627')], max_length=100, null=True, verbose_name='How many session did this child participate in online classes this week?'),
        ),
        migrations.AlterField(
            model_name='rs_fc',
            name='share_expectations',
            field=models.CharField(blank=True, choices=[('', '----------'), ('yes', '\u0646\u0639\u0645'), ('no', '\u0643\u0644\u0627')], max_length=10, null=True, verbose_name='\u0647\u0644 \u062a\u0645 \u0627\u0639\u0644\u0627\u0645 \u0627\u0644\u0623\u0647\u0644 \u0645\u0627 \u0647\u0648 \u0645\u062a\u0648\u0642\u0639 \u0645\u0646 \u0645\u0634\u0627\u0631\u0643\u0629 \u0627\u0644\u0637\u0641\u0644 \u0641\u064a \u0627\u0644\u062a\u0639\u0644\u0645 \u0623\u0633\u0628\u0648\u0639\u064a\u064b\u0627 \u061f'),
        ),
        migrations.AlterField(
            model_name='rs_fc',
            name='targeted_competencies',
            field=models.TextField(blank=True, null=True, verbose_name='\u0627\u0644\u0643\u0641\u0627\u064a\u0627\u062a \u0627\u0644\u0645\u0633\u062a\u0647\u062f\u0641\u0629'),
        ),
    ]
