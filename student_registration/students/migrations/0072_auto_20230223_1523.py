# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2023-02-23 15:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0071_idtype_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='attach_type_1',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='attach_type_1', to='students.AttachmentType', verbose_name='Type'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='attach_type_2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='attach_type_2', to='students.AttachmentType', verbose_name='Type'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='attach_type_3',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='attach_type_3', to='students.AttachmentType', verbose_name='Type'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='attach_type_4',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='attach_type_4', to='students.AttachmentType', verbose_name='Type'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='attach_type_5',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='attach_type_5', to='students.AttachmentType', verbose_name='Type'),
        ),
    ]
