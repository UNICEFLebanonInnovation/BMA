# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

import datetime
from django.contrib.auth.decorators import login_required
import io
import csv
import logging
logging.basicConfig(level=logging.ERROR)
import os
import uuid
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.db import connection
import codecs
import logging
import traceback
from django.views.generic import ListView, FormView, TemplateView, UpdateView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, JsonResponse, HttpResponseBadRequest, HttpResponseForbidden, HttpResponseRedirect
from django.db.models import Q, Sum, Avg, F, Func, When
from rest_framework import status
from rest_framework import viewsets, mixins, permissions
from braces.views import GroupRequiredMixin, SuperuserRequiredMixin
from django_filters.views import FilterView
from django_tables2 import MultiTableMixin, RequestConfig, SingleTableView
from django_tables2.export.views import ExportMixin
from dal import autocomplete
from django.http import FileResponse
from storages.backends.azure_storage import AzureStorage

from student_registration.users.utils import force_default_language
from .utils import is_allowed_create, is_allowed_edit
from .models import (
    Student,
    Teacher
)
from student_registration.schools.models import (
    PartnerOrganization,
)
from .forms import (
    TeacherForm
)
from .serializers import (
    StudentSerializer,
    TeacherSerializer
)
from .tables import (
    BootstrapTable,
    TeacherTable
)
from .filters import (
    TeacherFilter
)
from student_registration.enrollments.models import (
    EducationYear
)
from student_registration.alp.models import ALPRound
from student_registration.backends.models import ExportHistory


class StudentViewSet(mixins.RetrieveModelMixin,
                     mixins.ListModelMixin,
                     viewsets.GenericViewSet):

    model = Student
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        alp_round = ALPRound.objects.get(current_round=True)
        education_year = EducationYear.objects.get(current_year=True)
        qs = self.queryset.filter(
            Q(alp_enrollment__isnull=False,
              alp_enrollment__deleted=False,
              alp_enrollment__alp_round=alp_round) |
            Q(student_enrollment__isnull=False,
              student_enrollment__deleted=False,
              student_enrollment__education_year=education_year)
        )
        if self.request.GET.get('barcode', None):
            qs = qs.filter(hh_barcode=self.request.GET.get('barcode', None))
        if self.request.GET.get('case_number', None):
            qs = qs.filter(id_number=self.request.GET.get('case_number', None))
        if self.request.GET.get('first_name', None):
            qs = qs.filter(first_name=self.request.GET.get('first_name', None))
        if self.request.GET.get('last_name', None):
            qs = qs.filter(last_name=self.request.GET.get('last_name', None))
        if self.request.GET.get('father_name', None):
            qs = qs.filter(father_name=self.request.GET.get('father_name', None))
        if self.request.GET.get('mother_fullname', None):
            qs = qs.filter(mother_fullname=self.request.GET.get('mother_fullname', None))
        if self.request.GET.get('birthday_day', None):
            qs = qs.filter(birthday_day=self.request.GET.get('birthday_day', None))
        if self.request.GET.get('birthday_month', None):
            qs = qs.filter(birthday_month=self.request.GET.get('birthday_month', None))
        if self.request.GET.get('birthday_year', None):
            qs = qs.filter(birthday_year=self.request.GET.get('birthday_year', None))
        if self.request.GET.get('gender', None):
            qs = qs.filter(sex=self.request.GET.get('gender', None))
        if self.request.GET.get('name', None):
            for term in self.request.GET.get('name', None).split():
                qs = qs.filter(
                    Q(first_name__contains=term) |
                    Q(father_name__contains=term) |
                    Q(last_name__contains=term) |
                    Q(id_number__contains=term)
                ).distinct()
        try:
            if self.request.GET.get('individual_number', None):
                qs = qs.filter(id_number=self.request.GET.get('individual_number', None))
        except Exception as ex:
            return []

        return qs


class StudentSearchViewSet(mixins.RetrieveModelMixin,
                           mixins.ListModelMixin,
                           mixins.CreateModelMixin,
                           mixins.UpdateModelMixin,
                           viewsets.GenericViewSet):

    model = Student
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        if self.request.method in ["PATCH", "POST", "PUT"]:
            return self.queryset
        terms = self.request.GET.get('term', 0)
        school_type = self.request.GET.get('school_type', '2ndshift')
        user_school = self.request.user.school_id
        school = int(self.request.GET.get('school', 0))
        if terms:
            if school_type == 'alp':
                alp_round = ALPRound.objects.get(current_round=True)
                qs = Student.alp.filter(
                    alp_enrollment__school_id__in=[school, user_school],
                    alp_enrollment__alp_round__lt=alp_round.id,
                    alp_enrollment__registered_in_level__isnull=False,
                )
            else:
                education_year = EducationYear.objects.get(current_year=True)
                qs = Student.second_shift.filter(
                    student_enrollment__school_id__in=[school, user_school],
                    student_enrollment__education_year__lt=education_year.id
                )
            for term in terms.split():
                qs = qs.filter(
                    Q(first_name__contains=term) |
                    Q(father_name__contains=term) |
                    Q(last_name__contains=term) |
                    Q(id_number__contains=term)
                ).distinct()
            return qs


class StudentAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if not self.request.user.is_authenticated:
            return Student.objects.none()

        qs = Student.objects.all()

        if self.q:
            qs = Student.objects.filter(
                Q(first_name__istartswith=self.q) | Q(father_name__istartswith=self.q) |
                Q(last_name__istartswith=self.q) | Q(id_number__istartswith=self.q)
            )

        return qs


class TeacherListView(LoginRequiredMixin,
                  GroupRequiredMixin,
                  FilterView,
                  ExportMixin,
                  SingleTableView,
                  RequestConfig):
    table_class = TeacherTable
    model = Teacher
    template_name = 'students/teacher_list.html'
    table = BootstrapTable(Teacher.objects.all(), order_by='id')
    group_required = [u"CLM_TEACHER"]
    filterset_class = TeacherFilter

    def get_queryset(self):
        force_default_language(self.request)
        clm_bridging_all = self.request.user.groups.filter(name='CLM_BRIDGING_ALL').exists()
        is_staff = self.request.user.is_staff

        queryset = Teacher.objects.all()

        if clm_bridging_all or is_staff:
            queryset = Teacher.objects.all()
            # queryset = Teacher.objects.filter(round__current_year=True)

        else:
            school_id = 0
            partner_id = 0

            if self.request.user.school:
                school_id = self.request.user.school.id
            if self.request.user.partner_id:
                partner_id = self.request.user.partner_id

            if school_id and school_id > 0:
                queryset = Teacher.objects.filter(school_id=school_id)

            elif partner_id > 0:
                queryset = Teacher.objects.filter(school_id__in=PartnerOrganization
                                                 .objects
                                                 .filter(id=partner_id)
                                                 .values_list('schools', flat=True))
            else:
                queryset = queryset.none()

        return queryset


class TeacherAddView(LoginRequiredMixin,
                 GroupRequiredMixin,
                 FormView):
    template_name = 'students/teacher_form.html'
    form_class = TeacherForm
    success_url = '/students/teacher-list/'
    group_required = [u"CLM_TEACHER"]

    def get_success_url(self):
        if self.request.POST.get('save_add_another', None):
            return '/students/teacher-add/'
        if self.request.POST.get('save_and_continue', None):
            return '/students/teacher-edit/' + str(self.request.session.get('instance_id')) + '/'
        return self.success_url

    def get_context_data(self, **kwargs):
        force_default_language(self.request)
        """Insert the form into the context dict."""
        if 'form' not in kwargs:
            kwargs['form'] = self.get_form()
        kwargs['is_allowed_create'] = is_allowed_create('Bridging')
        return super(TeacherAddView, self).get_context_data(**kwargs)

    def get_initial(self):
        initial = super(TeacherAddView, self).get_initial()
        data = {
            'new_teacher': self.request.GET.get('new_teacher', ''),
        }
        if self.request.GET.get('teacher_id'):
            instance = Teacher.objects.get(id=self.request.GET.get('teacher_id'))
            data = Teacher(instance).data

        if data:
            data['new_teacher'] = self.request.GET.get('new_teacher', 'yes')
        initial = data

        return initial

    def form_valid(self, form):
        form.save(self.request)
        return super(TeacherAddView, self).form_valid(form)

    def get_form(self, form_class=None):
        if self.request.method == "POST":
            return TeacherForm(self.request.POST, self.request.FILES, instance=None, request=self.request)
        else:
            return TeacherForm(None, instance=None, request=self.request, initial=self.get_initial())


class TeacherEditView(LoginRequiredMixin,
                  GroupRequiredMixin,
                  FormView):
    template_name = 'students/teacher_form.html'
    form_class = TeacherForm
    success_url = '/students/teacher-list/'
    group_required = [u"CLM_TEACHER"]

    def get_success_url(self):
        if self.request.POST.get('save_add_another', None):
            return '/students/teacher-add/'
        if self.request.POST.get('save_and_continue', None):
            return '/students/teacher-edit/' + str(self.request.session.get('instance_id')) + '/'
        return self.success_url

    def get_context_data(self, **kwargs):
        force_default_language(self.request)
        """Insert the form into the context dict."""
        if 'form' not in kwargs:
            kwargs['form'] = self.get_form()
        kwargs['is_allowed_edit'] = is_allowed_edit('Bridging')
        return super(TeacherEditView, self).get_context_data(**kwargs)

    def get_form(self, form_class=None):
        instance = Teacher.objects.get(id=self.kwargs['pk'])
        if self.request.method == "POST":
            return TeacherForm(self.request.POST, self.request.FILES, instance=instance, request=self.request)
        else:
            data = TeacherSerializer(instance).data
            return TeacherForm(data, instance=instance, request=self.request)

    def form_valid(self, form):
        instance = Teacher.objects.get(id=self.kwargs['pk'])
        form.save(request=self.request, instance=instance)
        return super(TeacherEditView, self).form_valid(form)


class TeacherViewSet(mixins.RetrieveModelMixin,
                 mixins.ListModelMixin,
                 mixins.CreateModelMixin,
                 mixins.UpdateModelMixin,
                 viewsets.GenericViewSet):
    model = Teacher
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    permission_classes = (permissions.IsAuthenticated,)


    def get_queryset(self):
        force_default_language(self.request)
        clm_bridging_all = self.request.user.groups.filter(name='CLM_BRIDGING_ALL').exists()
        is_staff = self.request.user.is_staff

        queryset = Teacher.objects.all()

        if clm_bridging_all or is_staff:
            queryset = Teacher.objects.all()
        else:
            school_id = 0
            partner_id = 0

            if self.request.user.school:
                school_id = self.request.user.school.id
            if self.request.user.partner_id:
                partner_id = self.request.user.partner_id

            if school_id and school_id > 0:
                queryset = Teacher.objects.filter(school_id=school_id)

            elif partner_id > 0:
                queryset = Teacher.objects.filter(school_id__in=PartnerOrganization
                                                 .objects
                                                 .filter(id=partner_id)
                                                 .values_list('schools', flat=True))
            else:
                queryset = queryset.none()

        return queryset

    def delete(self, request, *args, **kwargs):
        instance = self.model.objects.get(id=kwargs['pk'])
        instance.delete()
        return JsonResponse({'status': status.HTTP_200_OK})


@login_required(login_url='/users/login')
def teacher_export_data(request):
    try:
        cursor = connection.cursor()
        user = request.user
        is_staff = user.is_staff
        clm_bridging_all = user.groups.filter(name='CLM_BRIDGING_ALL').exists()
        partner_name = user.partner.name if user.partner else ''

        vw_teacher_data = 'SELECT * FROM vw_teacher_data WHERE id > 0'
        query_params = []

        if not clm_bridging_all and not is_staff and request.user.partner:
            school_id = 0
            partner_id = user.partner_id

            vw_teacher_data += " AND partner_id = %s"
            query_params.append(partner_id)

            if user.school:
                school_id = user.school.id
            if school_id > 0:
                vw_teacher_data += " AND school_id = %s"
                query_params.append(school_id)

        elif not clm_bridging_all and not is_staff and not request.user.partner:
            vw_teacher_data += " AND id = 0 "

        cursor.execute(vw_teacher_data, query_params)

        bridging_data = cursor.fetchall()

        logging.debug("Executing query: %s", vw_teacher_data)
        logging.debug("Query params: %s", str(query_params))

        headers = [col[0] for col in cursor.description]

        # Create CSV
        csv_output = io.StringIO()
        csv_writer = csv.writer(csv_output)

        # Add BOM for Arabic text
        csv_output.write(codecs.BOM_UTF8.decode('utf-8'))
        csv_writer.writerow(headers)  # Write headers

        for row in bridging_data:
            encoded_row = []
            for cell in row:
                if isinstance(cell, (str, bytes)):  # Handle string and bytes
                    encoded_row.append(cell.decode('utf-8') if isinstance(cell, bytes) else cell)
                elif isinstance(cell, (datetime.date, datetime.datetime)):  # Convert date/datetime objects to string
                    encoded_row.append(cell.strftime('%Y-%m-%d'))
                else:  # Convert other data types to string
                    encoded_row.append(str(cell))
            csv_writer.writerow(encoded_row)

        unique_id = str(uuid.uuid4())
        file_name = "teacher_{}.csv".format(unique_id)
        file_path = os.path.join('export', file_name)

        # Save file
        default_storage.save(file_path, ContentFile(csv_output.getvalue().encode('utf-8')))

        # Store export history
        ExportHistory.objects.create(
            export_type='Teacher List',
            created_by=user,
            partner_name=partner_name
        )

        return HttpResponse(file_name)

    except Exception as e:
        logging.error("An error occurred during the export process:")
        logging.error(traceback.format_exc())
        return HttpResponse("An error occurred: " + str(e), status=500)


class MyAzureStorage(AzureStorage):
    location = "export"


def serve_file(request, file_path):
    from pathlib import Path
    file_name = Path(file_path).name
    storage = MyAzureStorage()
    file = storage.open(file_path, "rb")
    response = FileResponse(file)
    response['Content-Disposition'] = 'attachment; filename="'+file_name+'"'
    return response
