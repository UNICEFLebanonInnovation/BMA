# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2020-11-18 10:49
from __future__ import unicode_literals

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clm', '0172_cbece_mid_test'),
    ]

    operations = [
        migrations.AddField(
            model_name='cbece',
            name='mid_test_barriers_other',
            field=models.TextField(blank=True, null=True, verbose_name='\u0625\u0630\u0627 \u0643\u0627\u0646 \u0644\u0623\u0633\u0628\u0627\u0628 \u0623\u062e\u0631\u0649 \u064a\u0631\u062c\u0649 \u0627\u0644\u062a\u062d\u062f\u064a\u062f'),
        ),
        migrations.AddField(
            model_name='cbece',
            name='mid_test_barriers_single',
            field=models.CharField(blank=True, choices=[('Full time job to support family financially', '\u0627\u0644\u0639\u0645\u0644 \u0644\u0625\u0639\u0627\u0644\u0629 \u0627\u0644\u0639\u0627\u0626\u0644\u0629 \u0645\u0627\u062f\u064a\u0627\u064b'), ('seasonal_work', '\u0627\u0644\u0639\u0645\u0644 \u0627\u0644\u0645\u0648\u0633\u0645\u064a'), ('availablity_electronic_device', '\u0639\u062f\u0645  \u0648\u062c\u0648\u062f \u0627\u0644\u062c\u0647\u0627\u0632 \u0627\u0644\u0643\u062a\u0631\u0648\u0646\u064a'), ('internet_connectivity', '\u0627\u0644\u0627\u062a\u0635\u0627\u0644 \u0628\u0634\u0628\u0643\u0629 \u0627\u0644\u0625\u0646\u062a\u0631\u0646\u062a'), ('sickness', '\u0627\u0644\u0645\u0631\u0636'), ('security', '\u0627\u0644\u0648\u0636\u0639 \u0627\u0644\u0623\u0645\u0646\u064a'), ('family_moved', '\u062a\u0628\u062f\u064a\u0644 \u0645\u0643\u0627\u0646 \u0627\u0644\u0633\u0643\u0646'), ('Moved back to Syria', '\u0627\u0646\u062a\u0642\u0644 \u0627\u0644\u0649 \u0633\u0648\u0631\u064a\u0627'), ('Enrolled in formal education', '\u0645\u0633\u062c\u0644 \u0641\u064a \u0627\u0644\u062a\u0639\u0644\u064a\u0645 \u0627\u0644\u0631\u0633\u0645\u064a'), ('marriage engagement pregnancy', '\u0632\u0648\u0627\u062c/\u062e\u0637\u0648\u0628\u0629'), ('violence bullying', '  \u062a\u0646\u0645\u0631/\u0639\u0646\u0641 \u0636\u062f \u0627\u0644\u0637\u0641\u0644 \u0645\u0646 \u0642\u0628\u0644 \u0637\u0641\u0644 \u0623\u062e\u0631'), ('No interest in pursuing the programme/No value', '\u0639\u062f\u0645 \u0627\u0644\u0631\u063a\u0628\u0629 \u0641\u064a \u0627\u0644\u062a\u0639\u0644\u0645/ \u0644\u0627 \u0642\u064a\u0645\u0629'), ('no_barriers', '\u0644\u0627 \u064a\u0648\u062c\u062f'), ('other', '\u0622\u062e\u0631')], max_length=100, null=True, verbose_name='The main barriers affecting the daily attendance and performance'),
        ),
        migrations.AddField(
            model_name='cbece',
            name='mid_test_basic_stationery',
            field=models.CharField(blank=True, choices=[('yes', '\u0646\u0639\u0645'), ('no', '\u0643\u0644\u0627')], max_length=10, null=True, verbose_name=' \u0647\u0644 \u062d\u0635\u0644 \u0627\u0644\u0637\u0641\u0644 \u0639\u0644\u0649 \u0627\u0644\u0642\u0631\u0637\u0627\u0633\u064a\u0629 \u0627\u0644\u0623\u0633\u0627\u0633\u064a\u0629\u061f'),
        ),
        migrations.AddField(
            model_name='cbece',
            name='mid_test_child_health_concern',
            field=models.CharField(blank=True, choices=[('yes', '\u0646\u0639\u0645'), ('no', '\u0643\u0644\u0627')], max_length=100, null=True, verbose_name='\u0647\u0644 \u0647\u0646\u0627\u0643 \u0634\u064a\u0626 \u064a\u062f\u0639\u0648 \u0644\u0644\u0642\u0644\u0642'),
        ),
        migrations.AddField(
            model_name='cbece',
            name='mid_test_child_health_examed',
            field=models.CharField(blank=True, choices=[('yes', '\u0646\u0639\u0645'), ('no', '\u0643\u0644\u0627')], max_length=100, null=True, verbose_name='"Did the child receive health exam'),
        ),
        migrations.AddField(
            model_name='cbece',
            name='mid_test_covid_session_attended',
            field=models.CharField(blank=True, choices=[('yes', '\u0646\u0639\u0645'), ('no', '\u0643\u0644\u0627')], max_length=100, null=True, verbose_name='\u0647\u0644 \u062e\u0636\u0639 \u0627\u0644\u062a\u0644\u0645\u064a\u0630 \u0625\u0644\u0649 \u062c\u0644\u0633\u0627\u062a \u0627\u0644\u062f\u0639\u0645 \u0627\u0644\u0646\u0641\u0633\u064a \u0648\u0627\u0644\u0627\u062c\u062a\u0645\u0627\u0639\u064a\u0651'),
        ),
        migrations.AddField(
            model_name='cbece',
            name='mid_test_covid_session_modality',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, choices=[('online', '\u0639\u0646 \u0637\u0631\u064a\u0642 \u0627\u062a\u0635\u0627\u0644 Whatsapp'), ('phone', '\u0639\u0646 \u0637\u0631\u064a\u0642 \u0627\u0644\u0623\u062a\u0635\u0627\u0644 \u0627\u0644\u0647\u0627\u062a\u0641\u064a'), ('offline', ' \u0639\u0646 \u0637\u0631\u064a\u0642 \u0627\u0644\u0627\u062a\u0635\u0627\u0644 \u0627\u0644\u0645\u0628\u0627\u0634\u0631(\u0644\u064a\u0633 \u0639\u0628\u0631 \u0627\u0644\u0623\u0646\u062a\u0631\u0646\u062a)')], max_length=200, null=True), blank=True, null=True, size=None, verbose_name='Please the modality used per each session'),
        ),
        migrations.AddField(
            model_name='cbece',
            name='mid_test_covid_session_number',
            field=models.IntegerField(blank=True, null=True, verbose_name='PSS session number'),
        ),
        migrations.AddField(
            model_name='cbece',
            name='mid_test_done',
            field=models.CharField(blank=True, choices=[('yes', '\u0646\u0639\u0645'), ('no', '\u0643\u0644\u0627')], max_length=100, null=True, verbose_name='test_done'),
        ),
        migrations.AddField(
            model_name='cbece',
            name='mid_test_family_visit_number',
            field=models.IntegerField(blank=True, null=True, verbose_name='\u0627\u0644\u0631\u062c\u0627\u0621 \u0625\u062f\u062e\u0627\u0644 \u0639\u062f\u062f \u0632\u064a\u0627\u0631\u0629 \u0627\u0644\u0623\u0647\u0644 \u0644\u0644\u0645\u0631\u0643\u0632'),
        ),
        migrations.AddField(
            model_name='cbece',
            name='mid_test_follow_up_result',
            field=models.CharField(blank=True, choices=[('child back', '\u0625\u062a\u0635\u0627\u0644 \u0647\u0627\u062a\u0641\u064a'), ('child transfer to difficulty center', 'Child transfer to difficulty center'), ('child transfer to protection', 'Child transfer to protection'), ('child transfer to medical', 'Child transfer to medical'), ('Intensive followup', 'Intensive followup'), ('dropout', ' \u0645\u062a\u0633\u0631\u0628 \u0645\u0646 \u0627\u0644\u062a\u0639\u0644\u064a\u0645')], max_length=100, null=True, verbose_name='\u0646\u062a\u064a\u062c\u0629 \u0627\u0644\u0645\u062a\u0627\u0628\u0639\u0629'),
        ),
        migrations.AddField(
            model_name='cbece',
            name='mid_test_follow_up_type',
            field=models.CharField(blank=True, choices=[('none', '----------'), ('Phone', '\u0625\u062a\u0635\u0627\u0644 \u0647\u0627\u062a\u0641\u064a'), ('House visit', '\u0632\u064a\u0627\u0631\u0629 \u0645\u0646\u0632\u0644\u064a\u0629'), ('Family Visit', '\u0632\u064a\u0627\u0631\u0629 \u0627\u0644\u0623\u0647\u0644 \u0644\u0644\u0645\u0631\u0643\u0632')], max_length=100, null=True, verbose_name='\u0646\u0648\u0639 \u0627\u0644\u0645\u062a\u0627\u0628\u0639\u0629'),
        ),
        migrations.AddField(
            model_name='cbece',
            name='mid_test_followup_session_attended',
            field=models.CharField(blank=True, choices=[('yes', '\u0646\u0639\u0645'), ('no', '\u0643\u0644\u0627')], max_length=100, null=True, verbose_name='\u0647\u0644 \u062e\u0636\u0639 \u0627\u0644\u062a\u0644\u0645\u064a\u0630 \u0625\u0644\u0649 \u062c\u0644\u0633\u0627\u062a \u0627\u0644\u062f\u0639\u0645 \u0627\u0644\u0646\u0641\u0633\u064a \u0648\u0627\u0644\u0627\u062c\u062a\u0645\u0627\u0639\u064a\u0651'),
        ),
        migrations.AddField(
            model_name='cbece',
            name='mid_test_followup_session_modality',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, choices=[('online', '\u0639\u0646 \u0637\u0631\u064a\u0642 \u0627\u062a\u0635\u0627\u0644 Whatsapp'), ('phone', '\u0639\u0646 \u0637\u0631\u064a\u0642 \u0627\u0644\u0623\u062a\u0635\u0627\u0644 \u0627\u0644\u0647\u0627\u062a\u0641\u064a'), ('offline', ' \u0639\u0646 \u0637\u0631\u064a\u0642 \u0627\u0644\u0627\u062a\u0635\u0627\u0644 \u0627\u0644\u0645\u0628\u0627\u0634\u0631(\u0644\u064a\u0633 \u0639\u0628\u0631 \u0627\u0644\u0623\u0646\u062a\u0631\u0646\u062a)')], max_length=200, null=True), blank=True, null=True, size=None, verbose_name='Please the modality used per each session'),
        ),
        migrations.AddField(
            model_name='cbece',
            name='mid_test_followup_session_number',
            field=models.IntegerField(blank=True, null=True, verbose_name='PSS session number'),
        ),
        migrations.AddField(
            model_name='cbece',
            name='mid_test_house_visit_number',
            field=models.IntegerField(blank=True, null=True, verbose_name='\u0627\u0644\u0631\u062c\u0627\u0621 \u0625\u062f\u062e\u0627\u0644 \u0639\u062f\u062f \u0627\u0644\u0632\u064a\u0627\u0631\u0627\u062a \u0627\u0644\u0645\u0646\u0632\u0644\u064a\u0629'),
        ),
        migrations.AddField(
            model_name='cbece',
            name='mid_test_learning_result',
            field=models.CharField(blank=True, choices=[('', '----------'), ('graduated_to_cbece_next_level', '\u0631\u0641\u0639 \u0625\u0644\u0649 \u0627\u0644\u0645\u0633\u062a\u0648\u0649 \u0627\u0644\u062a\u0627\u0644\u064a'), ('graduated_to_cbece_next_round_same_level', '\u0625\u0643\u0645\u0627\u0644 \u0641\u064a \u0646\u0641\u0633 \u0627\u0644\u0645\u0633\u062a\u0648\u0649 \u0641\u064a \u0627\u0644\u062f\u0648\u0631\u0629 \u0627\u0644\u0642\u0627\u062f\u0645\u0629'), ('graduated_to_cbece_next_round_higher_level', '\u064a\u0631\u0641\u0639 \u0625\u0627\u0644\u0649 \u0627\u0644\u0645\u0633\u062a\u0648\u0649 \u0627\u0644\u0623\u0639\u0644\u0649 \u0641\u064a \u0627\u0644\u062f\u0648\u0631\u0629 \u0627\u0644\u0642\u0627\u062f\u0645\u0629'), ('referred_to_alp', '\u0623\u062d\u064a\u0644 \u0625\u0644\u0649 \u0628\u0631\u0646\u0627\u0645\u062c ALP'), ('referred_public_school', '\u0627\u0644\u0623\u062d\u0627\u0644\u0629 \u0625\u0644\u0649 \u0627\u0644\u062a\u0639\u0644\u064a\u0645 \u0627\u0644\u0631\u0633\u0645\u064a'), ('referred_to_tvet', '\u0627\u0644\u0623\u062d\u0627\u0644\u0629 \u0627\u0644\u0649 \u0627\u0644\u062a\u0639\u0644\u064a\u0645 \u0627\u0644\u0645\u0647\u0646\u064a \u0648 \u0627\u0644\u062a\u0642\u0646\u064a (TVET)'), ('referred_to_ycbece', 'Referred to YCBECE'), ('dropout', '\u0627\u0644\u062a\u0633\u0631\u0628 \u0645\u0646 \u0627\u0644\u062f\u0648\u0631\u0629')], max_length=100, null=True, verbose_name=' \u0646\u062a\u064a\u062c\u0629 \u0627\u0644\u062a\u0639\u0644\u0645'),
        ),
        migrations.AddField(
            model_name='cbece',
            name='mid_test_parent_attended',
            field=models.CharField(blank=True, choices=[('', '----------'), ('mother', '\u0627\u0644\u0623\u0645'), ('father', '\u0627\u0644\u0623\u0628'), ('other', '\u0622\u062e\u0631')], max_length=100, null=True, verbose_name='\u0647\u0644 \u062d\u0636\u0631 \u0648\u0644\u064a \u0623\u0645\u0631 \u0627\u0644\u0637\u0641\u0644 \u0623\u062c\u062a\u0645\u0627\u0639\u0627\u062a \u0627\u0644\u0623\u0647\u0644\u061f'),
        ),
        migrations.AddField(
            model_name='cbece',
            name='mid_test_parent_attended_other',
            field=models.TextField(blank=True, null=True, verbose_name='\u0625\u0630\u0627 \u0643\u0627\u0646 \u0644\u0623\u0633\u0628\u0627\u0628 \u0623\u062e\u0631\u0649 \u064a\u0631\u062c\u0649 \u0627\u0644\u062a\u062d\u062f\u064a\u062f'),
        ),
        migrations.AddField(
            model_name='cbece',
            name='mid_test_parent_attended_visits',
            field=models.CharField(blank=True, choices=[('yes', '\u0646\u0639\u0645'), ('no', '\u0643\u0644\u0627')], max_length=100, null=True, verbose_name='\u0647\u0644 \u062d\u0636\u0631 \u0648\u0644\u064a \u0623\u0645\u0631 \u0627\u0644\u0637\u0641\u0644 \u0623\u062c\u062a\u0645\u0627\u0639\u0627\u062a \u0627\u0644\u0623\u0647\u0644\u061f'),
        ),
        migrations.AddField(
            model_name='cbece',
            name='mid_test_participation',
            field=models.CharField(blank=True, choices=[('', '----------'), ('no_absence', '\u0644\u0627 \u063a\u064a\u0627\u0628'), ('less_than_5days', '\u063a\u064a\u0627\u0628 \u0627\u0642\u0644 \u0645\u0646 5 \u0627\u064a\u0627\u0645/\u0627\u0648 \u0645\u0627 \u064a\u0639\u0627\u062f\u0644\u0647\u0627 \u0628\u0627\u0644\u0646\u0633\u0628\u0629 \u0644\u0644\u062a\u0639\u0644\u064a\u0645 \u0639\u0646 \u0628\u0639\u062f'), ('5_10_days', '\u063a\u064a\u0627\u0628 \u0645\u0627 \u0628\u064a\u0646 10-5 \u0627\u064a\u0627\u0645/\u0627\u0648 \u0645\u0627 \u064a\u0639\u0627\u062f\u0644\u0647\u0627 \u0628\u0627\u0644\u0646\u0633\u0628\u0629 \u0644\u0644\u062a\u0639\u0644\u064a\u0645 \u0639\u0646 \u0628\u0639\u062f'), ('10_15_days', '\u063a\u064a\u0627\u0628 \u0645\u0627 \u0628\u064a\u0646 10-15 \u0627\u064a\u0627\u0645/\u0627\u0648 \u0645\u0627 \u064a\u0639\u0627\u062f\u0644\u0647\u0627 \u0628\u0627\u0644\u0646\u0633\u0628\u0629 \u0644\u0644\u062a\u0639\u0644\u064a\u0645 \u0639\u0646 \u0628\u0639\u062f'), ('15_25_days', '\u063a\u064a\u0627\u0628 \u0645\u0627 \u0628\u064a\u0646 25-15 \u0627\u064a\u0627\u0645/\u0627\u0648 \u0645\u0627 \u064a\u0639\u0627\u062f\u0644\u0647\u0627 \u0628\u0627\u0644\u0646\u0633\u0628\u0629 \u0644\u0644\u062a\u0639\u0644\u064a\u0645 \u0639\u0646 \u0628\u0639\u062f'), ('more_than_25days', '\u063a\u064a\u0627\u0628 \u0627\u0643\u062b\u0631 \u0645\u0646 25 \u0627\u064a\u0627\u0645/\u0627\u0648 \u0645\u0627 \u064a\u0639\u0627\u062f\u0644\u0647\u0627 \u0628\u0627\u0644\u0646\u0633\u0628\u0629 \u0644\u0644\u062a\u0639\u0644\u064a\u0645 \u0639\u0646 \u0628\u0639\u062f\u0628')], max_length=100, null=True, verbose_name='\u0627\u0644\u0645\u0634\u0627\u0631\u0643\u0629  '),
        ),
        migrations.AddField(
            model_name='cbece',
            name='mid_test_phone_call_number',
            field=models.IntegerField(blank=True, null=True, verbose_name='\u0627\u0644\u0631\u062c\u0627\u0621 \u0625\u062f\u062e\u0627\u0644 \u0639\u062f\u062f \u0627\u0644\u0627\u062a\u0635\u0627\u0644\u0627\u062a'),
        ),
        migrations.AddField(
            model_name='cbece',
            name='mid_test_pss_session_attended',
            field=models.CharField(blank=True, choices=[('yes', '\u0646\u0639\u0645'), ('no', '\u0643\u0644\u0627')], max_length=100, null=True, verbose_name='\u0647\u0644 \u062e\u0636\u0639 \u0627\u0644\u062a\u0644\u0645\u064a\u0630 \u0625\u0644\u0649 \u062c\u0644\u0633\u0627\u062a \u0627\u0644\u062f\u0639\u0645 \u0627\u0644\u0646\u0641\u0633\u064a \u0648\u0627\u0644\u0627\u062c\u062a\u0645\u0627\u0639\u064a\u0651'),
        ),
        migrations.AddField(
            model_name='cbece',
            name='mid_test_pss_session_modality',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, choices=[('online', '\u0639\u0646 \u0637\u0631\u064a\u0642 \u0627\u062a\u0635\u0627\u0644 Whatsapp'), ('phone', '\u0639\u0646 \u0637\u0631\u064a\u0642 \u0627\u0644\u0623\u062a\u0635\u0627\u0644 \u0627\u0644\u0647\u0627\u062a\u0641\u064a'), ('offline', ' \u0639\u0646 \u0637\u0631\u064a\u0642 \u0627\u0644\u0627\u062a\u0635\u0627\u0644 \u0627\u0644\u0645\u0628\u0627\u0634\u0631(\u0644\u064a\u0633 \u0639\u0628\u0631 \u0627\u0644\u0623\u0646\u062a\u0631\u0646\u062a)')], max_length=200, null=True), blank=True, null=True, size=None, verbose_name='Please the modality used per each session'),
        ),
        migrations.AddField(
            model_name='cbece',
            name='mid_test_pss_session_number',
            field=models.IntegerField(blank=True, null=True, verbose_name='PSS session number'),
        ),
        migrations.AddField(
            model_name='cbece',
            name='mid_test_round_complete',
            field=models.CharField(blank=True, choices=[('yes', '\u0646\u0639\u0645'), ('no', '\u0643\u0644\u0627')], max_length=100, null=True, verbose_name='\u0647\u0644 \u0627\u062a\u0645 \u0627\u0644\u0637\u0641\u0644 \u0627\u0644\u062f\u0648\u0631\u0629 \u0628\u0646\u062c\u0627\u062d\u061f'),
        ),
    ]
