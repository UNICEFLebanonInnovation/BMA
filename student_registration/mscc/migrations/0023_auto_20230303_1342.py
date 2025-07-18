# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2023-03-03 13:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mscc', '0022_auto_20230220_1400'),
    ]

    operations = [
        migrations.AddField(
            model_name='healthnutritionservice',
            name='accessing_reproductive_health',
            field=models.CharField(blank=True, choices=[('', '----------'), ('Yes', 'Yes'), ('No', 'No')], max_length=10, null=True, verbose_name='In case of a child marriage to ask if the child is accessing in reproductive health services'),
        ),
        migrations.AddField(
            model_name='healthnutritionservice',
            name='immunization_record_screened',
            field=models.CharField(blank=True, choices=[('', '----------'), ('Yes', 'Yes'), ('No', 'No')], max_length=10, null=True, verbose_name='Child immunization record screened (to check the integrated ECD milestones Cards based on the age of the child- or the national immunization Calendar)'),
        ),
        migrations.AddField(
            model_name='healthnutritionservice',
            name='muac_malnutrition_screening',
            field=models.CharField(blank=True, choices=[('', '----------'), ('MAM (MUAC >11.5 and <12.5 cm)', 'MAM (MUAC >11.5 and <12.5 cm)'), ('SAM (MUAC <11.5 cm)', 'SAM (MUAC <11.5 cm)'), ('SAM with Bilateral pitting oedema  (both feet puffy)', 'SAM with Bilateral pitting oedema  (both feet puffy)'), ('At risk of malnutrition (MUAC 12.5-13.5 cm)', 'At risk of malnutrition (MUAC 12.5-13.5 cm)')], max_length=10, null=True, verbose_name='MUAC malnutrition screening '),
        ),
        migrations.AddField(
            model_name='healthnutritionservice',
            name='physical_activity',
            field=models.CharField(blank=True, choices=[('', '----------'), ('Yes', 'Yes'), ('No', 'No')], max_length=10, null=True, verbose_name='Is the child practicing physical activity at least twice a week'),
        ),
        migrations.AddField(
            model_name='healthnutritionservice',
            name='vaccine_missing',
            field=models.TextField(blank=True, null=True, verbose_name='write the name of vaccine missing'),
        ),
        migrations.AlterField(
            model_name='healthnutritionservice',
            name='age_eat_solid_food',
            field=models.CharField(blank=True, choices=[('', '----------'), ('0 month', '1 months'), ('1 month', '1 months'), ('2 months', '2 months'), ('3 months', '3 months'), ('4 months', '4 months'), ('5 months', '5 months'), ('6 months', '6 months'), ('7 months', '7 months'), ('8 months', '8 months'), ('9 months', '9 months'), ('10 months', '10 months'), ('11 months', '11 months'), ('12 months', '12 months'), ('13 months', '13 months'), ('14 months', '14 months'), ('15 months', '15 months'), ('16 months', '16 months'), ('17 months', '17 months'), ('18 months', '18 months'), ('19 months', '19 months'), ('20 months', '20 months'), ('21 months', '21 months'), ('22 months', '22 months'), ('23 months', '23 months'), ('24 months', '24 months')], max_length=50, null=True, verbose_name='If yes, at which age ?'),
        ),
        migrations.AlterField(
            model_name='healthnutritionservice',
            name='development_delays_identified',
            field=models.CharField(blank=True, choices=[('', '----------'), ('social/emotional', 'social/emotional'), ('Language/communication', 'language/communication'), ('Cognitive (learning thinking, problem solving)', 'Cognitive (learning thinking, problem solving)'), ('Movement/Physical development', 'Movement/Physical development')], max_length=50, null=True, verbose_name='Any delays in the development milestones  is being identified? (please to check the Integrated ECD milestones Cards based on the age of the child)'),
        ),
        migrations.AlterField(
            model_name='healthnutritionservice',
            name='infant_exclusively_breastfed',
            field=models.CharField(blank=True, choices=[('', '----------'), ('Yes', 'Yes'), ('No', 'No')], max_length=10, null=True, verbose_name='if yes, is it exclusively breastfeeding for infants between 0-6 months?(only brest milk no other liquids even water)'),
        ),
    ]
