# coding: utf-8
import django_tables2 as tables
from django.utils.translation import gettext as _

from .models import Teacher


class BootstrapTable(tables.Table):

    class Meta:
        model = Teacher
        template = 'django_tables2/bootstrap.html'
        attrs = {'class': 'table table-bordered table-striped table-hover'}


class CommonTable(tables.Table):

    edit_column = tables.TemplateColumn(verbose_name=_('Edit'),
                                        template_name='django_tables2/edit_column.html',
                                        attrs={'url': ''})
    # delete_column = tables.TemplateColumn(verbose_name=_('Delete school'),
    #                                       template_name='django_tables2/delete_column.html',
    #                                       attrs={'url': ''})

    class Meta:
        model = Teacher
        template = 'django_tables2/bootstrap.html'
        fields = (
            'edit_column',
            # 'delete_column',
        )


class TeacherTable(CommonTable):

    action_column = tables.TemplateColumn(verbose_name=_('Actions'), orderable=False,
                                        template_name='django_tables2/students/teacher_action_column.html',
                                        attrs={'url_edit': '/students/teacher-edit/',
                                               'url_delete': '/students/teacher-delete/',
                                               'programme': 'Bridging'})

    class Meta:
        model = Teacher
        template = 'django_tables2/bootstrap.html'
        fields = (
            'action_column',
            'first_name',
            'father_name',
            'last_name',
            'sex',
            'unicef_id',
            'primary_phone_number',
            'school',
            'round',
            'email',
            'owner',
            'modified_by',
            'created',
            'modified',
        )
