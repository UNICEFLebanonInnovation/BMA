# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.contrib import admin
from import_export import resources, fields
from import_export import fields
from import_export.admin import ImportExportModelAdmin
from django.utils.translation import gettext, gettext_lazy as _
from django.contrib.auth.admin import UserAdmin as AuthUserAdmin
from django.contrib.auth.models import Group
from .models import User
from .forms import UserAdminForm
from student_registration.alp.templatetags.util_tags import has_group
from django.contrib.admin import SimpleListFilter


class UserCategoryFilter(SimpleListFilter):
    title = 'User Category'
    parameter_name = 'user_category'

    def lookups(self, request, model_admin):
        return (
            ('MSCC', 'MSCC'),
            ('YOUTH', 'YOUTH'),
            ('Dirasa', 'Dirasa'),
        )

    def queryset(self, request, queryset):
        if self.value() == 'MSCC':
            return queryset.filter(groups__name='MSCC')
        if self.value() == 'YOUTH':
            return queryset.filter(groups__name='YOUTH')
        if self.value() == 'Dirasa':
            return queryset.exclude(groups__name__in=['MSCC', 'YOUTH'])
        return queryset


class UserResource(resources.ModelResource):
    is_active = fields.Field(column_name='is_active', attribute='is_active')
    user_category = fields.Field(column_name='user_category')

    class Meta:
        model = User
        fields = (
            'id',
            'first_name',
            'last_name',
            'username',
            'email',
            'partner__name',
            'school__name',
            'center__name',
            'partner__name',
            'is_active',
            'user_category',
        )
        export_order = fields

    def dehydrate_user_category(self, user):
        if has_group(user, 'MSCC'):
            return 'MSCC'
        if has_group(user, 'YOUTH'):
            return 'YOUTH'
        return 'Dirasa'


class UserAdmin(AuthUserAdmin, ImportExportModelAdmin):
    resource_class = UserResource
    form = UserAdminForm
    filter_horizontal = ('groups', 'user_permissions')
    list_display = (
        'username',
        'first_name',
        'last_name',
        'is_active',
        'email',
        'school',
        'center',
        'partner',
        'phone_number',
        'is_active',
        'user_category_display'
    )
    search_fields = (
        u'username',
        u'school__name',
        u'first_name',
        u'last_name',
    )
    list_filter = (
        'groups',
        'school',
        'center',
        'partner',
        'is_active',
        UserCategoryFilter
    )
    actions = (
        'activate',
        'disable',
        'allow_enroll_create',
        'allow_enroll_edit',
        'allow_enroll_delete',
        'allow_enroll_edit_old',
        'allow_enroll_grading',
        'allow_attendance',
        'deny_enroll_create',
        'deny_enroll_edit',
        'deny_enroll_delete',
        'deny_enroll_edit_old',
        'deny_enroll_grading',
        'deny_attendance',
        'allow_helpdesk',
        'deny_helpdesk',
        'allow_utilities',
        'deny_utilities',
        'allow_showpic',
        'deny_showpic',
        'allow_clearpic',
        'deny_clearpic',
        'allow_evalcovid19',
        'deny_evalcovid19',
        'allow_staff_attendance',
        'deny_staff_attendance',
        'allow_survey_ps',
        'deny_survey_ps',
    )

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
        (None, {'fields': ('partner',
                           'center',
                           'school',
                           # 'location', 'locations', 'schools', 'regions'
                           )})
    )

    add_fieldsets = (
        (None, {'fields': ('username', 'password1', 'password2')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
        (None, {'fields': ('partner', 'center',
                           'school',
                           # 'location', 'locations', 'schools', 'regions'
                           )})
    )

    def user_category_display(self, obj):
        if has_group(obj, 'MSCC'):
            return 'MSCC'
        if has_group(obj, 'YOUTH'):
            return 'YOUTH'
        return 'Dirasa'
    user_category_display.short_description = 'User Category'

    def activate(self, request, queryset):
        queryset.update(is_active=True)

    def disable(self, request, queryset):
        queryset.update(is_active=False)
        return False

    def allow_enroll_create(self, request, queryset):
        group = Group.objects.get(name='ENROL_CREATE')
        for user in queryset:
            user.groups.add(group)

    def allow_enroll_edit(self, request, queryset):
        group = Group.objects.get(name='ENROL_EDIT')
        for user in queryset:
            user.groups.add(group)

    def allow_enroll_delete(self, request, queryset):
        group = Group.objects.get(name='ENROL_DELETE')
        for user in queryset:
            user.groups.add(group)

    def allow_enroll_edit_old(self, request, queryset):
        group = Group.objects.get(name='ENROL_EDIT_OLD')
        for user in queryset:
            user.groups.add(group)

    def allow_enroll_grading(self, request, queryset):
        group = Group.objects.get(name='ENROL_GRADING')
        for user in queryset:
            user.groups.add(group)

    def allow_utilities(self, request, queryset):
        group = Group.objects.get(name='UTILITIES')
        for user in queryset:
            user.groups.add(group)

    def allow_showpic(self, request, queryset):
        group = Group.objects.get(name='ENROL_SHOWPIC')
        for user in queryset:
            user.groups.add(group)

    def allow_staff_evalcovid19(self, request, queryset):
        group = Group.objects.get(name='EVAL_COVID19')
        for user in queryset:
            user.groups.add(group)

    def allow_staff_attendance(self, request, queryset):
        group = Group.objects.get(name='ALLOW_STAFF_ATTENDANCE')
        for user in queryset:
            user.groups.add(group)

    def allow_survey_ps(self, request, queryset):
        group = Group.objects.get(name='SURVEY_PS')
        for user in queryset:
            user.groups.add(group)

    def allow_clearpic(self, request, queryset):
        group = Group.objects.get(name='ENROL_CLEARPIC')
        for user in queryset:
            user.groups.add(group)

    def allow_attendance(self, request, queryset):
        group = Group.objects.get(name='ATTENDANCE')
        for user in queryset:
            user.groups.add(group)

    def deny_enroll_create(self, request, queryset):
        group = Group.objects.get(name='ENROL_CREATE')
        for user in queryset:
            user.groups.remove(group)

    def deny_enroll_edit(self, request, queryset):
        group = Group.objects.get(name='ENROL_EDIT')
        for user in queryset:
            user.groups.remove(group)

    def deny_enroll_delete(self, request, queryset):
        group = Group.objects.get(name='ENROL_DELETE')
        for user in queryset:
            user.groups.remove(group)

    def deny_enroll_edit_old(self, request, queryset):
        group = Group.objects.get(name='ENROL_EDIT_OLD')
        for user in queryset:
            user.groups.remove(group)

    def deny_enroll_grading(self, request, queryset):
        group = Group.objects.get(name='ENROL_GRADING')
        for user in queryset:
            user.groups.remove(group)

    def deny_clearpic(self, request, queryset):
        group = Group.objects.get(name='ENROL_CLEARPIC')
        for user in queryset:
            user.groups.remove(group)

    def deny_utilities(self, request, queryset):
        group = Group.objects.get(name='UTILITIES')
        for user in queryset:
            user.groups.remove(group)

    def deny_showpic(self, request, queryset):
        group = Group.objects.get(name='ENROL_SHOWPIC')
        for user in queryset:
            user.groups.remove(group)

    def deny_evalcovid19(self, request, queryset):
        group = Group.objects.get(name='EVAL_COVID19')
        for user in queryset:
            user.groups.remove(group)

    def deny_attendance(self, request, queryset):
        group = Group.objects.get(name='ATTENDANCE')
        for user in queryset:
            user.groups.remove(group)

    def deny_staff_attendance(self, request, queryset):
        group = Group.objects.get(name='ALLOW_STAFF_ATTENDANCE')
        for user in queryset:
            user.groups.remove(group)

    def deny_survey_ps(self, request, queryset):
        group = Group.objects.get(name='SURVEY_PS')
        for user in queryset:
            user.groups.remove(group)

    def allow_helpdesk(self, request, queryset):
        group = Group.objects.get(name='HELPDESK')
        for user in queryset:
            user.groups.add(group)
        queryset.update(is_staff=True)

    def deny_helpdesk(self, request, queryset):
        group = Group.objects.get(name='HELPDESK')
        for user in queryset:
            user.groups.remove(group)
        queryset.update(is_staff=False)

    def allow_staffenroll_create(self, request, queryset):
        group = Group.objects.get(name='STAFFENROL_CREATE')
        for user in queryset:
            user.groups.add(group)

    def allow_staffenroll_edit(self, request, queryset):
        group = Group.objects.get(name='STAFFENROL_EDIT')
        for user in queryset:
            user.groups.add(group)

    def allow_staffenroll_delete(self, request, queryset):
        group = Group.objects.get(name='STAFFENROL_DELETE')
        for user in queryset:
            user.groups.add(group)


admin.site.register(User, UserAdmin)


