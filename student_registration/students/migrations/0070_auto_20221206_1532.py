# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2022-12-06 15:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import student_registration.students.models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0069_auto_20220819_1703'),
    ]

    operations = [
        migrations.AlterField(
            model_name='specialneedsdt',
            name='specialneeds',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='students.SpecialNeeds', verbose_name='Detail Special Needs'),
        ),
        migrations.AlterField(
            model_name='student',
            name='Financialsupport_number',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='Financial Support Number'),
        ),
        migrations.AlterField(
            model_name='student',
            name='address',
            field=models.TextField(blank=True, null=True, verbose_name='Address'),
        ),
        migrations.AlterField(
            model_name='student',
            name='birth_documenttype',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='documenttype', to='students.Birth_DocumentType', verbose_name='Document Type'),
        ),
        migrations.AlterField(
            model_name='student',
            name='birthday_day',
            field=models.CharField(blank=True, choices=[(b'1', 1), (b'2', 2), (b'3', 3), (b'4', 4), (b'5', 5), (b'6', 6), (b'7', 7), (b'8', 8), (b'9', 9), (b'10', 10), (b'11', 11), (b'12', 12), (b'13', 13), (b'14', 14), (b'15', 15), (b'16', 16), (b'17', 17), (b'18', 18), (b'19', 19), (b'20', 20), (b'21', 21), (b'22', 22), (b'23', 23), (b'24', 24), (b'25', 25), (b'26', 26), (b'27', 27), (b'28', 28), (b'29', 29), (b'30', 30), (b'31', 31)], default=0, max_length=2, null=True, verbose_name='Birthday day'),
        ),
        migrations.AlterField(
            model_name='student',
            name='birthday_month',
            field=models.CharField(blank=True, choices=[('1', 'January'), ('2', 'February'), ('3', 'March'), ('4', 'April'), ('5', 'May'), ('6', 'June'), ('7', 'July'), ('8', 'August'), ('9', 'September'), ('10', 'October'), ('11', 'November'), ('12', 'December')], default=0, max_length=2, null=True, verbose_name='Birthday month'),
        ),
        migrations.AlterField(
            model_name='student',
            name='birthday_year',
            field=models.CharField(blank=True, choices=[(b'1990', 1990), (b'1991', 1991), (b'1992', 1992), (b'1993', 1993), (b'1994', 1994), (b'1995', 1995), (b'1996', 1996), (b'1997', 1997), (b'1998', 1998), (b'1999', 1999), (b'2000', 2000), (b'2001', 2001), (b'2002', 2002), (b'2003', 2003), (b'2004', 2004), (b'2005', 2005), (b'2006', 2006), (b'2007', 2007), (b'2008', 2008), (b'2009', 2009), (b'2010', 2010), (b'2011', 2011), (b'2012', 2012), (b'2013', 2013), (b'2014', 2014), (b'2015', 2015), (b'2016', 2016), (b'2017', 2017), (b'2018', 2018), (b'2019', 2019), (b'2020', 2020), (b'2021', 2021), (b'2022', 2022), (b'2023', 2023), (b'2024', 2024), (b'2025', 2025), (b'2026', 2026), (b'2027', 2027), (b'2028', 2028), (b'2029', 2029), (b'2030', 2030), (b'2031', 2031), (b'2032', 2032), (b'2033', 2033), (b'2034', 2034), (b'2035', 2035), (b'2036', 2036), (b'2037', 2037), (b'2038', 2038), (b'2039', 2039), (b'2040', 2040), (b'2041', 2041), (b'2042', 2042), (b'2043', 2043), (b'2044', 2044), (b'2045', 2045), (b'2046', 2046), (b'2047', 2047), (b'2048', 2048), (b'2049', 2049)], default=0, max_length=4, null=True, verbose_name='Birthday year'),
        ),
        migrations.AlterField(
            model_name='student',
            name='birthdoc_image',
            field=models.ImageField(blank=True, help_text='Birth Document', null=True, upload_to='profiles/birthdoc', validators=[student_registration.students.models.validate_file_size]),
        ),
        migrations.AlterField(
            model_name='student',
            name='family_status',
            field=models.CharField(blank=True, choices=[('married', 'Married'), ('engaged', 'Engaged'), ('divorced', 'Divorced'), ('widower', 'Widower'), ('single', 'Single')], max_length=50, null=True, verbose_name='Family status'),
        ),
        migrations.AlterField(
            model_name='student',
            name='father_name',
            field=models.CharField(blank=True, db_index=True, max_length=64, null=True, verbose_name='Father name'),
        ),
        migrations.AlterField(
            model_name='student',
            name='financialsupport',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='financialsupport', to='students.FinancialSupport', verbose_name='Financial Support Program'),
        ),
        migrations.AlterField(
            model_name='student',
            name='first_name',
            field=models.CharField(blank=True, db_index=True, max_length=64, null=True, verbose_name='First name'),
        ),
        migrations.AlterField(
            model_name='student',
            name='have_children',
            field=models.CharField(blank=True, choices=[(1, 'Yes'), (0, 'No')], max_length=50, null=True, verbose_name='Have children'),
        ),
        migrations.AlterField(
            model_name='student',
            name='id_image',
            field=models.ImageField(blank=True, help_text='Identification picture', null=True, upload_to='profiles/ids', validators=[student_registration.students.models.validate_file_size]),
        ),
        migrations.AlterField(
            model_name='student',
            name='id_number',
            field=models.CharField(blank=True, db_index=True, max_length=45, null=True, verbose_name='ID number'),
        ),
        migrations.AlterField(
            model_name='student',
            name='id_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='students.IDType', verbose_name='ID type'),
        ),
        migrations.AlterField(
            model_name='student',
            name='last_name',
            field=models.CharField(blank=True, db_index=True, max_length=64, null=True, verbose_name='Last name'),
        ),
        migrations.AlterField(
            model_name='student',
            name='mother_fullname',
            field=models.CharField(blank=True, db_index=True, max_length=64, null=True, verbose_name='Mother fullname'),
        ),
        migrations.AlterField(
            model_name='student',
            name='mother_nationality',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='students.Nationality', verbose_name='Mother nationality'),
        ),
        migrations.AlterField(
            model_name='student',
            name='nationality',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='students.Nationality', verbose_name='Nationality'),
        ),
        migrations.AlterField(
            model_name='student',
            name='phone',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='Phone number'),
        ),
        migrations.AlterField(
            model_name='student',
            name='phone_prefix',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='Phone prefix'),
        ),
        migrations.AlterField(
            model_name='student',
            name='place_of_birth',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Place of birth'),
        ),
        migrations.AlterField(
            model_name='student',
            name='recordnumber',
            field=models.CharField(blank=True, max_length=45, null=True, verbose_name='Identity record number'),
        ),
        migrations.AlterField(
            model_name='student',
            name='registered_in_unhcr',
            field=models.CharField(blank=True, choices=[(1, 'Yes'), (0, 'No')], max_length=50, null=True, verbose_name='Registered in UNHCR'),
        ),
        migrations.AlterField(
            model_name='student',
            name='sex',
            field=models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female')], max_length=50, null=True, verbose_name='Sex'),
        ),
        migrations.AlterField(
            model_name='student',
            name='specialneeds',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='specialneeds', to='students.SpecialNeeds', verbose_name='Types Special Needs'),
        ),
        migrations.AlterField(
            model_name='student',
            name='specialneedsdt',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='students.SpecialNeedsDt', verbose_name='Details Special Needs'),
        ),
        migrations.AlterField(
            model_name='student',
            name='std_image',
            field=models.ImageField(blank=True, help_text='Profile Picture', null=True, upload_to='profiles', validators=[student_registration.students.models.validate_file_size], verbose_name='Profile Picture'),
        ),
        migrations.AlterField(
            model_name='student',
            name='unhcr_family',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='UNHCR Family Number'),
        ),
        migrations.AlterField(
            model_name='student',
            name='unhcr_image',
            field=models.ImageField(blank=True, help_text='UNHCR picture', null=True, upload_to='profiles/unhcr', validators=[student_registration.students.models.validate_file_size]),
        ),
        migrations.AlterField(
            model_name='student',
            name='unhcr_personal',
            field=models.CharField(blank=True, db_index=True, max_length=150, null=True, verbose_name='UNHCR Personal Number'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='address',
            field=models.TextField(blank=True, null=True, verbose_name='Address'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='birthday_day',
            field=models.CharField(blank=True, choices=[(b'1', 1), (b'2', 2), (b'3', 3), (b'4', 4), (b'5', 5), (b'6', 6), (b'7', 7), (b'8', 8), (b'9', 9), (b'10', 10), (b'11', 11), (b'12', 12), (b'13', 13), (b'14', 14), (b'15', 15), (b'16', 16), (b'17', 17), (b'18', 18), (b'19', 19), (b'20', 20), (b'21', 21), (b'22', 22), (b'23', 23), (b'24', 24), (b'25', 25), (b'26', 26), (b'27', 27), (b'28', 28), (b'29', 29), (b'30', 30), (b'31', 31)], default=0, max_length=2, null=True, verbose_name='Birthday day'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='birthday_month',
            field=models.CharField(blank=True, choices=[('1', 'January'), ('2', 'February'), ('3', 'March'), ('4', 'April'), ('5', 'May'), ('6', 'June'), ('7', 'July'), ('8', 'August'), ('9', 'September'), ('10', 'October'), ('11', 'November'), ('12', 'December')], default=0, max_length=2, null=True, verbose_name='Birthday month'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='birthday_year',
            field=models.CharField(blank=True, choices=[(b'1990', 1990), (b'1991', 1991), (b'1992', 1992), (b'1993', 1993), (b'1994', 1994), (b'1995', 1995), (b'1996', 1996), (b'1997', 1997), (b'1998', 1998), (b'1999', 1999), (b'2000', 2000), (b'2001', 2001), (b'2002', 2002), (b'2003', 2003), (b'2004', 2004), (b'2005', 2005), (b'2006', 2006), (b'2007', 2007), (b'2008', 2008), (b'2009', 2009), (b'2010', 2010), (b'2011', 2011), (b'2012', 2012), (b'2013', 2013), (b'2014', 2014), (b'2015', 2015), (b'2016', 2016), (b'2017', 2017), (b'2018', 2018), (b'2019', 2019), (b'2020', 2020), (b'2021', 2021), (b'2022', 2022), (b'2023', 2023), (b'2024', 2024), (b'2025', 2025), (b'2026', 2026), (b'2027', 2027), (b'2028', 2028), (b'2029', 2029), (b'2030', 2030), (b'2031', 2031), (b'2032', 2032), (b'2033', 2033), (b'2034', 2034), (b'2035', 2035), (b'2036', 2036), (b'2037', 2037), (b'2038', 2038), (b'2039', 2039), (b'2040', 2040), (b'2041', 2041), (b'2042', 2042), (b'2043', 2043), (b'2044', 2044), (b'2045', 2045), (b'2046', 2046), (b'2047', 2047), (b'2048', 2048), (b'2049', 2049)], default=0, max_length=4, null=True, verbose_name='Birthday year'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='email',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='extra_coaching',
            field=models.CharField(blank=True, choices=[('', '----------'), ('yes', 'Yes'), ('no', 'No')], max_length=10, null=True, verbose_name='Extra coaching'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='family_status',
            field=models.CharField(blank=True, choices=[('married', 'Married'), ('engaged', 'Engaged'), ('divorced', 'Divorced'), ('widower', 'Widower'), ('single', 'Single')], max_length=50, null=True, verbose_name='Family status'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='father_name',
            field=models.CharField(blank=True, db_index=True, max_length=64, null=True, verbose_name='Father name'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='first_name',
            field=models.CharField(blank=True, db_index=True, max_length=64, null=True, verbose_name='First name'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='have_children',
            field=models.CharField(blank=True, choices=[(1, 'Yes'), (0, 'No')], max_length=50, null=True, verbose_name='Have children'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='id_number',
            field=models.CharField(blank=True, db_index=True, max_length=45, null=True, verbose_name='ID number'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='id_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='students.IDType', verbose_name='ID type'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='last_name',
            field=models.CharField(blank=True, db_index=True, max_length=64, null=True, verbose_name='Last name'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='mother_fullname',
            field=models.CharField(blank=True, db_index=True, max_length=64, null=True, verbose_name='Mother fullname'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='mother_nationality',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='students.Nationality', verbose_name='Mother nationality'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='nationality',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='students.Nationality', verbose_name='Nationality'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='phone',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='Phone number'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='phone_prefix',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='Phone prefix'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='place_of_birth',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Place of birth'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='primary_phone_number',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Phone number'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='recordnumber',
            field=models.CharField(blank=True, max_length=45, null=True, verbose_name='Identity record number'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='registered_in_unhcr',
            field=models.CharField(blank=True, choices=[(1, 'Yes'), (0, 'No')], max_length=50, null=True, verbose_name='Registered in UNHCR'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='school',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='schools.School', verbose_name='School'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='sex',
            field=models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female')], max_length=50, null=True, verbose_name='Sex'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='subject_provided',
            field=models.CharField(blank=True, choices=[('arabic', 'Arabic'), ('math', 'Math'), ('english', 'English'), ('french', 'French')], max_length=100, null=True, verbose_name='Subject provided'),
        ),
    ]
