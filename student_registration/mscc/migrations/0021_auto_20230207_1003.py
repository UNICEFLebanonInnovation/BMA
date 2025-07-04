# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2023-02-07 10:03
from __future__ import unicode_literals

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mscc', '0020_auto_20230120_1501'),
    ]

    operations = [
        migrations.AlterField(
            model_name='digitalservice',
            name='using_akelius',
            field=models.CharField(blank=True, choices=[('', '----------'), ('Yes', 'Yes'), ('No', 'No')], max_length=100, null=True, verbose_name='Is the child using Akelius?'),
        ),
        migrations.AlterField(
            model_name='digitalservice',
            name='using_lp',
            field=models.CharField(blank=True, choices=[('', '----------'), ('Yes', 'Yes'), ('No', 'No')], max_length=100, null=True, verbose_name='Is the child using Learning Passport?'),
        ),
        migrations.AlterField(
            model_name='educationassessment',
            name='post_attended_arabic',
            field=models.CharField(blank=True, choices=[('', '----------'), ('Yes', 'Yes'), ('No', 'No')], max_length=100, null=True, verbose_name='Did the Child Undertake Arabic Language Development Assessment'),
        ),
        migrations.AlterField(
            model_name='educationassessment',
            name='post_attended_language',
            field=models.CharField(blank=True, choices=[('', '----------'), ('Yes', 'Yes'), ('No', 'No')], max_length=100, null=True, verbose_name='Did the Child Undertake Foreign Language Development Assessment'),
        ),
        migrations.AlterField(
            model_name='educationassessment',
            name='post_attended_math',
            field=models.CharField(blank=True, choices=[('', '----------'), ('Yes', 'Yes'), ('No', 'No')], max_length=100, null=True, verbose_name='Did the Child Undertake Cognitive Development - Mathematics test'),
        ),
        migrations.AlterField(
            model_name='educationassessment',
            name='post_test_done',
            field=models.CharField(blank=True, choices=[('', '----------'), ('Yes', 'Yes'), ('No', 'No')], max_length=100, null=True, verbose_name='Did the child undertake the Post tests?'),
        ),
        migrations.AlterField(
            model_name='educationassessment',
            name='pre_attended_arabic',
            field=models.CharField(blank=True, choices=[('', '----------'), ('Yes', 'Yes'), ('No', 'No')], max_length=100, null=True, verbose_name='Did the Child Undertake Arabic Language Development Assessment'),
        ),
        migrations.AlterField(
            model_name='educationassessment',
            name='pre_attended_language',
            field=models.CharField(blank=True, choices=[('', '----------'), ('Yes', 'Yes'), ('No', 'No')], max_length=100, null=True, verbose_name='Did the Child Undertake Foreign Language Development Assessment'),
        ),
        migrations.AlterField(
            model_name='educationassessment',
            name='pre_attended_math',
            field=models.CharField(blank=True, choices=[('', '----------'), ('Yes', 'Yes'), ('No', 'No')], max_length=100, null=True, verbose_name='Did the Child Undertake Cognitive Development - Mathematics test'),
        ),
        migrations.AlterField(
            model_name='educationassessment',
            name='school_year_completed',
            field=models.CharField(blank=True, choices=[('', '----------'), ('Yes', 'Yes'), ('No', 'No')], max_length=100, null=True, verbose_name='Did the child fully complete the school year?'),
        ),
        migrations.AlterField(
            model_name='educationprogrammeassessment',
            name='programme_type',
            field=models.CharField(blank=True, choices=[('', '----------'), ('BLN Level 1', 'BLN Level 1'), ('BLN Level 2', 'BLN Level 2'), ('YBLN', 'YBLN'), ('YFNL', 'YFNL'), ('CBECE Level 3', 'CBECE Level 3'), ('Retention Support', 'Retention Support')], max_length=100, null=True, verbose_name='Education Programme Type'),
        ),
        migrations.AlterField(
            model_name='educationrsservice',
            name='support_needed',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, choices=[('', '----------'), ('Foreign Languages', 'Foreign Languages'), ('Arabic', 'Arabic'), ('Math', 'Math'), ('Sciences', 'Sciences')], max_length=100, null=True), blank=True, null=True, size=None, verbose_name='Needed support'),
        ),
        migrations.AlterField(
            model_name='followupservice',
            name='parent_attended_meeting',
            field=models.CharField(blank=True, choices=[('', '----------'), ('Yes', 'Yes'), ('No', 'No')], max_length=10, null=True, verbose_name="Did the child's caregiver attend parent meeting/engagment sessions"),
        ),
        migrations.AlterField(
            model_name='healthnutritionservice',
            name='baby_breastfed',
            field=models.CharField(blank=True, choices=[('', '----------'), ('Yes', 'Yes'), ('No', 'No')], max_length=10, null=True, verbose_name='Is the baby being Breastfed?'),
        ),
        migrations.AlterField(
            model_name='healthnutritionservice',
            name='child_vaccinated',
            field=models.CharField(blank=True, choices=[('', '----------'), ('Yes', 'Yes'), ('No', 'No')], max_length=10, null=True, verbose_name='Is the child being vaccinated as per the National vaccination calendar?'),
        ),
        migrations.AlterField(
            model_name='healthnutritionservice',
            name='development_delays_identified',
            field=models.CharField(blank=True, choices=[('', '----------'), ('Mental', 'Mental'), ('Cognitive', 'Cognitive'), ('Neurological', 'Neurological'), ('No', 'No')], max_length=50, null=True, verbose_name='Any mental , cognitive or neurological development delays is being identified?'),
        ),
        migrations.AlterField(
            model_name='healthnutritionservice',
            name='eat_solid_food',
            field=models.CharField(blank=True, choices=[('', '----------'), ('Yes', 'Yes'), ('No', 'No')], max_length=10, null=True, verbose_name='Did the child start to eat solid food?'),
        ),
        migrations.AlterField(
            model_name='healthnutritionservice',
            name='eating_minimum_meals',
            field=models.CharField(blank=True, choices=[('', '----------'), ('Yes', 'Yes'), ('No', 'No')], max_length=10, null=True, verbose_name='Is the child eating 3 minimum meals per day?'),
        ),
        migrations.AlterField(
            model_name='healthnutritionservice',
            name='infant_exclusively_breastfed',
            field=models.CharField(blank=True, choices=[('', '----------'), ('Yes', 'Yes'), ('No', 'No')], max_length=10, null=True, verbose_name='if yes, is it exclusively breastfeeding for infants between 0-6 months?'),
        ),
        migrations.AlterField(
            model_name='healthnutritionservice',
            name='positive_parenting',
            field=models.CharField(blank=True, choices=[('', '----------'), ('Yes', 'Yes'), ('No', 'No')], max_length=10, null=True, verbose_name='positive parenting and dealing with difficult children without the use of harsh punishment?'),
        ),
        migrations.AlterField(
            model_name='inclusionservice',
            name='dropout',
            field=models.CharField(blank=True, choices=[('', '----------'), ('Yes', 'Yes'), ('No', 'No')], max_length=100, null=True, verbose_name='Dropout'),
        ),
        migrations.AlterField(
            model_name='inclusionservice',
            name='parental_engagement',
            field=models.CharField(blank=True, choices=[('', '----------'), ('Mother Only', 'Mother Only'), ('Father Only', 'Father Only'), ('Both', 'Both'), ('No one', 'No one'), ("Haven't started yet", "Haven't started yet")], max_length=100, null=True, verbose_name='Parental Engagement Curriculum'),
        ),
        migrations.AlterField(
            model_name='pssservice',
            name='caregivers_additional_parenting',
            field=models.CharField(blank=True, choices=[('', '----------'), ('Yes', 'Yes'), ('No', 'No')], max_length=100, null=True, verbose_name='If yes, would you like any additional parenting or psychosocial support?'),
        ),
        migrations.AlterField(
            model_name='pssservice',
            name='caregivers_distress',
            field=models.CharField(blank=True, choices=[('', '----------'), ('Yes', 'Yes'), ('No', 'No')], max_length=100, null=True, verbose_name='Do you feel distressed and anxious?'),
        ),
        migrations.AlterField(
            model_name='pssservice',
            name='child_additional_parenting',
            field=models.CharField(blank=True, choices=[('', '----------'), ('Yes', 'Yes'), ('No', 'No')], max_length=100, null=True, verbose_name='If yes, do you need additional support for taking care or better dealing with your children?'),
        ),
        migrations.AlterField(
            model_name='pssservice',
            name='child_distress',
            field=models.CharField(blank=True, choices=[('', '----------'), ('Yes', 'Yes'), ('No', 'No')], max_length=100, null=True, verbose_name='Are any of the children in your HH experiencing any signs of distress or negative mental health symptoms ?'),
        ),
        migrations.AlterField(
            model_name='pssservice',
            name='child_living_arrangement',
            field=models.CharField(blank=True, choices=[('', '----------'), ('Unaccompanied or Separated Child', 'Unaccompanied or Separated Child'), ('Living with single parent/caregiver', 'Living with single parent/caregiver'), ('Living with Mother/women-headed Household ', 'Living with Mother/women-headed Household'), ('Child-headed Household', 'Child-headed Household'), ('Main caregiver is ill/disabled', 'Main caregiver is ill/disabled')], max_length=250, null=True, verbose_name="What is the child's living arrangement?"),
        ),
        migrations.AlterField(
            model_name='pssservice',
            name='child_out_school_reasons',
            field=models.CharField(blank=True, choices=[('', '----------'), ('Fear of bullying, discrimination or violence at school or on the way to school', 'Fear of bullying, discrimination or violence at school or on the way to school'), ('The child needs to work', 'The child needs to work'), ('The child needs to stay at home to support the family with chores', 'The child needs to stay at home to support the family with chores'), ('Disability', 'Disability')], max_length=250, null=True, verbose_name='Reasons for a child being out of school'),
        ),
        migrations.AlterField(
            model_name='pssservice',
            name='child_registered',
            field=models.CharField(blank=True, choices=[('', '----------'), ('Yes', 'Yes'), ('No', 'No')], max_length=100, null=True, verbose_name='Is the child registered/ have birth registration?'),
        ),
        migrations.AlterField(
            model_name='pssservice',
            name='child_vulnerability',
            field=models.CharField(blank=True, choices=[('', '----------'), ('Clear signs of neglect', 'Clear signs of neglect'), ('Clear signs of distress', 'Clear signs of distress'), ('Clear signs of physical maltreatment/damage and/or injuries', 'Clear signs of physical maltreatment/damage and/or injuries')], max_length=250, null=True, verbose_name="What is the child's living arrangement?"),
        ),
        migrations.AlterField(
            model_name='referral',
            name='receive_needed_material',
            field=models.CharField(blank=True, choices=[('', '----------'), ('Yes', 'Yes'), ('No', 'No')], max_length=50, null=True, verbose_name='Did the child receive all needed materials and resources (Stationery, Books, Learning bundle)?'),
        ),
        migrations.AlterField(
            model_name='referral',
            name='referred_formal_education',
            field=models.CharField(blank=True, choices=[('', '----------'), ('Yes', 'Yes'), ('No', 'No')], max_length=10, null=True, verbose_name='Was the child referred to formal education (Grade 1)?'),
        ),
        migrations.AlterField(
            model_name='registration',
            name='cash_support_programmes',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, choices=[('', '----------'), ('Haddi', 'Haddi'), ('Education Cash assistance', 'Education Cash assistance'), ('UNHCR cash assistance', 'UNHCR cash assistance'), ('WFP cash assistance', 'WFP cash assistance')], max_length=100, null=True), blank=True, null=True, size=None, verbose_name='Cash support programmes that child is already benefitting from'),
        ),
        migrations.AlterField(
            model_name='registration',
            name='have_labour',
            field=models.CharField(blank=True, choices=[('', '----------'), ('No', 'No'), ('Yes - Morning', 'Yes - Morning'), ('Yes - Afternoon', 'Yes - Afternoon'), ('Yes - All day', 'Yes - All day')], max_length=100, null=True, verbose_name='Does the child participate in work?'),
        ),
        migrations.AlterField(
            model_name='youthassessment',
            name='benefit_innovation_course',
            field=models.CharField(blank=True, choices=[('', '----------'), ('Yes', 'Yes'), ('No', 'No')], max_length=100, null=True, verbose_name='Did the adolescent benefit from any social innovation/entrepreneurship course?'),
        ),
        migrations.AlterField(
            model_name='youthassessment',
            name='compelete_yfs_course',
            field=models.CharField(blank=True, choices=[('', '----------'), ('Yes', 'Yes'), ('No', 'No')], max_length=100, null=True, verbose_name='Did the adolescent compelete the YFS course?'),
        ),
        migrations.AlterField(
            model_name='youthassessment',
            name='complete_life_skills',
            field=models.CharField(blank=True, choices=[('', '----------'), ('Yes', 'Yes'), ('No', 'No')], max_length=100, null=True, verbose_name='Did the adolescent complete the life skills package?'),
        ),
        migrations.AlterField(
            model_name='youthassessment',
            name='participate_community_initiatives',
            field=models.CharField(blank=True, choices=[('', '----------'), ('Yes', 'Yes'), ('No', 'No')], max_length=100, null=True, verbose_name='Did the adolescent participate/come up in community based initiatives?'),
        ),
        migrations.AlterField(
            model_name='youthassessment',
            name='participate_volunteering',
            field=models.CharField(blank=True, choices=[('', '----------'), ('Yes', 'Yes'), ('No', 'No')], max_length=100, null=True, verbose_name='Did the adolescent participate in any volunteering opportunity during the course of the program?'),
        ),
        migrations.AlterField(
            model_name='youthassessment',
            name='receive_passing_grade',
            field=models.CharField(blank=True, choices=[('', '----------'), ('Yes', 'Yes'), ('No', 'No')], max_length=100, null=True, verbose_name='Did the adolescent receive a passing grade for the tests?'),
        ),
        migrations.AlterField(
            model_name='youthassessment',
            name='undertake_post_diagnostic',
            field=models.CharField(blank=True, choices=[('', '----------'), ('Yes', 'Yes'), ('No', 'No')], max_length=100, null=True, verbose_name='Did the adolescent undertake any Post Diagnotic tests?'),
        ),
        migrations.AlterField(
            model_name='youthkitservice',
            name='life_skills_completed',
            field=models.CharField(blank=True, choices=[('', '----------'), ('Yes', 'Yes'), ('No', 'No')], max_length=10, null=True, verbose_name='Did the adolescent complete the life skills package?'),
        ),
        migrations.AlterField(
            model_name='youthkitservice',
            name='participate_community_initiatives',
            field=models.CharField(blank=True, choices=[('', '----------'), ('Yes', 'Yes'), ('No', 'No')], max_length=10, null=True, verbose_name='Did the adolescent participate/come up in community based initiatives?'),
        ),
        migrations.AlterField(
            model_name='youthkitservice',
            name='participate_volunteering',
            field=models.CharField(blank=True, choices=[('', '----------'), ('Yes', 'Yes'), ('No', 'No')], max_length=10, null=True, verbose_name='Did the adolescent participate in any volunteering opportunity during the course of the program?'),
        ),
        migrations.AlterField(
            model_name='youthkitservice',
            name='pre_tests_administered',
            field=models.CharField(blank=True, choices=[('', '----------'), ('Yes', 'Yes'), ('No', 'No')], max_length=10, null=True, verbose_name='Were pre-tests administered to assess adolescents level?'),
        ),
        migrations.AlterField(
            model_name='youthkitservice',
            name='previous_community_initiative',
            field=models.CharField(blank=True, choices=[('', '----------'), ('Yes', 'Yes'), ('No', 'No')], max_length=10, null=True, verbose_name='Was the adolescent part of any previous community based initiative?'),
        ),
        migrations.AlterField(
            model_name='youthkitservice',
            name='receive_passing_grade',
            field=models.CharField(blank=True, choices=[('', '----------'), ('Yes', 'Yes'), ('No', 'No')], max_length=10, null=True, verbose_name='Did the adolescent receive a passing grade for the tests?'),
        ),
        migrations.AlterField(
            model_name='youthkitservice',
            name='social_course',
            field=models.CharField(blank=True, choices=[('', '----------'), ('Yes', 'Yes'), ('No', 'No')], max_length=10, null=True, verbose_name='Did the adolescent benefit from any social innovation/entrepreneurship course?'),
        ),
        migrations.AlterField(
            model_name='youthkitservice',
            name='test_diagnostic_done',
            field=models.CharField(blank=True, choices=[('', '----------'), ('Yes', 'Yes'), ('No', 'No')], max_length=10, null=True, verbose_name='Did the adolescent undertake any Post Diagnostic tests?'),
        ),
        migrations.AlterField(
            model_name='youthkitservice',
            name='volunteering_experience',
            field=models.CharField(blank=True, choices=[('', '----------'), ('Yes', 'Yes'), ('No', 'No')], max_length=10, null=True, verbose_name='Does the adolescent have any volunteering experience?'),
        ),
        migrations.AlterField(
            model_name='youthkitservice',
            name='yfs_course_completed',
            field=models.CharField(blank=True, choices=[('', '----------'), ('Yes', 'Yes'), ('No', 'No')], max_length=10, null=True, verbose_name='Did the adolescent complete the YFS course?'),
        ),
    ]
