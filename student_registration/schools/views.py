# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.db.models import Q
from django.views.generic import DetailView, ListView, RedirectView, CreateView, FormView, TemplateView, UpdateView
from django.http import HttpResponse, JsonResponse, HttpResponseBadRequest, HttpResponseForbidden
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from dal import autocomplete
from rest_framework import viewsets, mixins, permissions
from braces.views import GroupRequiredMixin
from django_filters.views import FilterView
from django_tables2 import MultiTableMixin, RequestConfig, SingleTableView
from django_tables2.export.views import ExportMixin
from django.contrib import admin
import zipfile
import csv
from django.utils.encoding import smart_str
import traceback

import os
import uuid
import codecs
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile

from django.shortcuts import render, redirect

from student_registration.users.templatetags.custom_tags import has_group
from django.contrib.auth.decorators import login_required

import logging
logging.basicConfig(level=logging.ERROR)
from student_registration.backends.models import Notification
from student_registration.users.utils import force_default_language
from .models import (
    EducationYear,
    School,
    ClassRoom,
    Section,
    PublicDocument,
    PartnerOrganization,
    Evaluation,
    Club,
    Meeting,
    CommunityInitiative,
    HealthVisit
)
from student_registration.locations.models import Location

from .serializers import (
    SchoolSerializer,
    ClassRoomSerializer,
    SectionSerializer
)
from .tables import (
    SchoolTable,
    SchoolExportTable,
    ClubTable,
    MeetingTable,
    CommunityInitiativeTable,
    HealthVisitTable

)
from student_registration.backends.models import ExportHistory

from .filters import (
    SchoolFilter
)
from .forms import ProfileForm,SchoolForm, ClubForm, MeetingForm, CommunityInitiativeForm , HealthVisitForm,  \
    PartnerForm, EvaluationForm,Classroom_Form, Classroom_Form_c1, Classroom_Form_c3,\
    Classroom_Form_c4, Classroom_Form_c5, Classroom_Form_c6, Classroom_Form_c7, Classroom_Form_c8, \
    Classroom_Form_c9, Classroom_Form_cprep
from .utils import *


class SchoolViewSet(mixins.ListModelMixin,
                    viewsets.GenericViewSet):

    model = School
    queryset = School.objects.all()
    serializer_class = SchoolSerializer
    permission_classes = (permissions.IsAuthenticated,)


class ClassRoomViewSet(mixins.ListModelMixin,
                       viewsets.GenericViewSet):

    model = ClassRoom
    queryset = ClassRoom.objects.all()
    serializer_class = ClassRoomSerializer
    permission_classes = (permissions.IsAuthenticated,)


class SectionViewSet(mixins.ListModelMixin,
                     viewsets.GenericViewSet):

    model = Section
    queryset = Section.objects.all()
    serializer_class = SectionSerializer
    permission_classes = (permissions.IsAuthenticated,)


class ProfileView(LoginRequiredMixin,
                  GroupRequiredMixin,
                  FormView):

    template_name = 'schools/profile.html'
    form_class = ProfileForm
    success_url = '/schools/profile/'
    group_required = [u"SCHOOL", u"ALP_SCHOOL"]

    def get_context_data(self, **kwargs):

        """Insert the form into the context dict."""
        if 'form' not in kwargs:
            kwargs['form'] = self.get_form()
            school = self.request.user.school

            notifications = Notification.objects.filter(type='general', schools=school)

            if school.is_2nd_shift and not school.is_alp:
                notifications = notifications.filter(school_type='2ndshift')
            if school.is_alp and not school.is_2nd_shift:
                notifications = notifications.filter(school_type='ALP')

            kwargs['notifications'] = notifications[:50]
            kwargs['unread_notifications'] = notifications.filter(status=False).count()
            tickets = Notification.objects.filter(
                type='helpdesk',
                school_id=school.id
            )
            kwargs['tickets'] = tickets[:50]
            kwargs['unread_tickets'] = tickets.filter(status=False).count()
        return super(ProfileView, self).get_context_data(**kwargs)

    def get_form(self, form_class=None):
        instance = School.objects.get(id=self.request.user.school_id)
        if self.request.method == "POST":
            return ProfileForm(self.request.POST, instance=instance)
        else:
            return ProfileForm(instance=instance)

    def form_valid(self, form):
        instance = School.objects.get(id=self.request.user.school_id)
        form.save(request=self.request, instance=instance)
        return super(ProfileView, self).form_valid(form)


class PartnerView(LoginRequiredMixin,
                  GroupRequiredMixin,
                  FormView):

    template_name = 'schools/partner.html'
    form_class = PartnerForm
    success_url = '/schools/partner/'
    group_required = [u"CLM"]

    def get_context_data(self, **kwargs):

        """Insert the form into the context dict."""
        if 'form' not in kwargs:
            kwargs['form'] = self.get_form()
        return super(PartnerView, self).get_context_data(**kwargs)

    def get_form(self, form_class=None):
        instance = PartnerOrganization.objects.get(id=self.request.user.partner_id)
        if self.request.method == "POST":
            return PartnerForm(self.request.POST, instance=instance)
        else:
            return PartnerForm(instance=instance)

    def form_valid(self, form):
        instance = PartnerOrganization.objects.get(id=self.request.user.partner_id)
        form.save(request=self.request, instance=instance)
        return super(PartnerView, self).form_valid(form)


class PublicDocumentView(LoginRequiredMixin,
                         GroupRequiredMixin,
                         TemplateView):

    model = PublicDocument
    queryset = PublicDocument.objects.all()
    template_name = 'schools/documents.html'
    group_required = [u"SCHOOL", u"ALP_SCHOOL"]

    def get_context_data(self, **kwargs):

        return {
            'documents': self.queryset
        }


class AutocompleteView(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if not self.request.user.is_authenticated:
            return School.objects.none()

        qs = School.objects.all()

        if self.q:
            qs = School.objects.filter(
                Q(name__istartswith=self.q) | Q(number__istartswith=self.q)
            )

        return qs


class EvaluationView(FormView):
    template_name = 'schools/evaluation.html'
    form_class = EvaluationForm
    success_url = '/schools/evaluation/'

    def get_form(self, form_class=None):
        education_year = EducationYear.objects.get(current_year=True)
        if self.request:
            if self.request.user:
                if self.request.user.school_id:
                    evaluation = Evaluation.objects.filter(school_id=self.request.user.school_id, education_year=education_year)
                    instance = Evaluation.objects.get(id=evaluation)

        if self.request.method == "POST":
            return EvaluationForm(self.request.POST, instance=instance)
        else:
            return EvaluationForm(instance=instance)

    def form_valid(self, form):
        education_year = EducationYear.objects.get(current_year=True)
        instance = Evaluation.objects.get(school_id=self.request.user.school_id, education_year=education_year)
        form.save(request=self.request, instance=instance)
        return super(EvaluationView, self).form_valid(form)


class Update_Class(UpdateView):
    model = Evaluation
    form_class = Classroom_Form

    template_name = 'schools/classform.html'
    success_url = '/schools/evaluation/'
    context_object_name = 'school_class'

    def get_success_url(self):
        return self.success_url

    def get_context_data(self, **kwargs):

        """Insert the form into the context dict."""
        if 'form' not in kwargs:
            kwargs['form'] = self.get_form()
        return super(Update_Class, self).get_context_data(**kwargs)

    def get_form(self, form_class=None):
        instance = Evaluation.objects.get(id=self.kwargs['pk'])
        if self.request.method == "POST":
            instance.save()
            return Classroom_Form(self.request.POST, instance=instance)
        else:
            return Classroom_Form(instance=instance)


class Update_Class_c1(UpdateView):
    model = Evaluation
    form_class = Classroom_Form_c1

    template_name = 'schools/classform.html'
    success_url = '/schools/evaluation/'
    context_object_name = 'school_class'

    def get_success_url(self):
        return self.success_url

    def get_context_data(self, **kwargs):

        """Insert the form into the context dict."""
        if 'form' not in kwargs:
            kwargs['form'] = self.get_form()
        return super(Update_Class_c1, self).get_context_data(**kwargs)

    def get_form(self, form_class=None):
        instance = Evaluation.objects.get(id=self.kwargs['pk'])
        if self.request.method == "POST":
            instance.save()
            return Classroom_Form_c1(self.request.POST, instance=instance)
        else:
            return Classroom_Form_c1(instance=instance)


class Update_Class_C3(UpdateView):
    model = Evaluation
    form_class = Classroom_Form_c3

    template_name = 'schools/classform.html'
    success_url = '/schools/evaluation/'
    context_object_name = 'school_class'

    def get_success_url(self):
        return self.success_url

    def get_context_data(self, **kwargs):

        """Insert the form into the context dict."""
        if 'form' not in kwargs:
            kwargs['form'] = self.get_form()
        return super(Update_Class_C3, self).get_context_data(**kwargs)

    def get_form(self, form_class=None):
        instance = Evaluation.objects.get(id=self.kwargs['pk'])
        if self.request.method == "POST":
            instance.save()
            return Classroom_Form_c3(self.request.POST, instance=instance)
        else:
            return Classroom_Form_c3(instance=instance)


class Update_Class_c4(UpdateView):
    model = Evaluation
    form_class = Classroom_Form_c4

    template_name = 'schools/classform.html'
    success_url = '/schools/evaluation/'
    context_object_name = 'school_class'

    def get_success_url(self):
        return self.success_url

    def get_context_data(self, **kwargs):

        """Insert the form into the context dict."""
        if 'form' not in kwargs:
            kwargs['form'] = self.get_form()
        return super(Update_Class_c4, self).get_context_data(**kwargs)

    def get_form(self, form_class=None):
        instance = Evaluation.objects.get(id=self.kwargs['pk'])
        if self.request.method == "POST":
            instance.save()
            return Classroom_Form_c4(self.request.POST, instance=instance)
        else:
            return Classroom_Form_c4(instance=instance)


class Update_Class_c5(UpdateView):
    model = Evaluation
    form_class = Classroom_Form_c5

    template_name = 'schools/classform.html'
    success_url = '/schools/evaluation/'
    context_object_name = 'school_class'

    def get_success_url(self):
        return self.success_url

    def get_context_data(self, **kwargs):

        """Insert the form into the context dict."""
        if 'form' not in kwargs:
            kwargs['form'] = self.get_form()
        return super(Update_Class_c5, self).get_context_data(**kwargs)

    def get_form(self, form_class=None):
        instance = Evaluation.objects.get(id=self.kwargs['pk'])
        if self.request.method == "POST":
            instance.save()
            return Classroom_Form_c5(self.request.POST, instance=instance)
        else:
            return Classroom_Form_c5(instance=instance)


class Update_Class_c6(UpdateView):
    model = Evaluation
    form_class = Classroom_Form_c6

    template_name = 'schools/classform.html'
    success_url = '/schools/evaluation/'
    context_object_name = 'school_class'

    def get_success_url(self):
        return self.success_url

    def get_context_data(self, **kwargs):

        """Insert the form into the context dict."""
        if 'form' not in kwargs:
            kwargs['form'] = self.get_form()
        return super(Update_Class_c6, self).get_context_data(**kwargs)

    def get_form(self, form_class=None):
        instance = Evaluation.objects.get(id=self.kwargs['pk'])
        if self.request.method == "POST":
            instance.save()
            return Classroom_Form_c6(self.request.POST, instance=instance)
        else:
            return Classroom_Form_c6(instance=instance)


class Update_Class_c7(UpdateView):
    model = Evaluation
    form_class = Classroom_Form_c7

    template_name = 'schools/classform.html'
    success_url = '/schools/evaluation/'
    context_object_name = 'school_class'

    def get_success_url(self):
        return self.success_url

    def get_context_data(self, **kwargs):

        """Insert the form into the context dict."""
        if 'form' not in kwargs:
            kwargs['form'] = self.get_form()
        return super(Update_Class_c7, self).get_context_data(**kwargs)

    def get_form(self, form_class=None):
        instance = Evaluation.objects.get(id=self.kwargs['pk'])
        if self.request.method == "POST":
            instance.save()
            return Classroom_Form_c7(self.request.POST, instance=instance)
        else:
            return Classroom_Form_c7(instance=instance)


class Update_Class_c8(UpdateView):
    model = Evaluation
    form_class = Classroom_Form_c8

    template_name = 'schools/classform.html'
    success_url = '/schools/evaluation/'
    context_object_name = 'school_class'

    def get_success_url(self):
        return self.success_url

    def get_context_data(self, **kwargs):

        """Insert the form into the context dict."""
        if 'form' not in kwargs:
            kwargs['form'] = self.get_form()
        return super(Update_Class_c8, self).get_context_data(**kwargs)

    def get_form(self, form_class=None):
        instance = Evaluation.objects.get(id=self.kwargs['pk'])
        if self.request.method == "POST":
            instance.save()
            return Classroom_Form_c8(self.request.POST, instance=instance)
        else:
            return Classroom_Form_c8(instance=instance)


class Update_Class_c9(UpdateView):
    model = Evaluation
    form_class = Classroom_Form_c9

    template_name = 'schools/classform.html'
    success_url = '/schools/evaluation/'
    context_object_name = 'school_class'

    def get_success_url(self):
        return self.success_url

    def get_context_data(self, **kwargs):

        """Insert the form into the context dict."""
        if 'form' not in kwargs:
            kwargs['form'] = self.get_form()
        return super(Update_Class_c9, self).get_context_data(**kwargs)

    def get_form(self, form_class=None):
        instance = Evaluation.objects.get(id=self.kwargs['pk'])
        if self.request.method == "POST":
            instance.save()
            return Classroom_Form_c9(self.request.POST, instance=instance)
        else:
            return Classroom_Form_c9(instance=instance)


class Update_Class_cprep(UpdateView):
    model = Evaluation
    form_class = Classroom_Form_cprep

    template_name = 'schools/classform.html'
    success_url = '/schools/evaluation/'
    context_object_name = 'school_class'

    def get_success_url(self):
        return self.success_url

    def get_context_data(self, **kwargs):

        """Insert the form into the context dict."""
        if 'form' not in kwargs:
            kwargs['form'] = self.get_form()
        return super(Update_Class_cprep, self).get_context_data(**kwargs)

    def get_form(self, form_class=None):
        instance = Evaluation.objects.get(id=self.kwargs['pk'])
        if self.request.method == "POST":
            instance.save()
            return Classroom_Form_cprep(self.request.POST, instance=instance)
        else:
            return Classroom_Form_cprep(instance=instance)


def load_districts(request):
    cities = []
    if request.GET.get('id_governorate'):
        id_governorate = request.GET.get('id_governorate')
        cities = Location.objects.filter(parent_id=id_governorate).order_by('name')
    return render(request, 'clm/city_dropdown_list_options.html', {'cities': cities})


def load_cadasters(request):
    cities = []
    if request.GET.get('id_district'):
        id_district = request.GET.get('id_district')
        cities = Location.objects.filter(parent_id=id_district).order_by('name')
    return render(request, 'clm/cadaster_dropdown_list_options.html', {'cities': cities})


def load_schools(request):
    schools = []
    if request.GET.get('id_governorate'):
        id_governorate = request.GET.get('id_governorate')
        schools = School.objects.filter(location_id=id_governorate).order_by('name')
    return render(request, 'clm/school_dropdown_list_options.html', {'schools': schools})


class SchoolListView(LoginRequiredMixin,
                  GroupRequiredMixin,
                  FilterView,
                  ExportMixin,
                  SingleTableView,
                  RequestConfig):
    table_class = SchoolTable
    model = School
    template_name = 'schools/school_list.html'
    table = SchoolTable(School.objects.all(), order_by='id')
    group_required = [u"CLM_Bridging"]
    filterset_class = SchoolFilter

    def get_queryset(self):

        clm_bridging_all = self.request.user.groups.filter(name='CLM_BRIDGING_ALL').exists()
        is_staff = self.request.user.is_staff

        queryset = School.objects.filter(is_bma=True).all()

        if clm_bridging_all or is_staff:
            queryset = School.objects.filter(is_bma=True).all()
        else:
            school_id = 0
            partner_id = 0

            if self.request.user.school:
                school_id = self.request.user.school.id
            if self.request.user.partner_id:
                partner_id = self.request.user.partner_id

            if school_id and school_id > 0:
                queryset = School.objects.filter(id=school_id)

            elif partner_id > 0:
                queryset = School.objects.filter(is_bma=True,
                                                 id__in=PartnerOrganization
                                                 .objects
                                                 .filter(id=partner_id)
                                                 .values_list('schools', flat=True))
            else:
                queryset = queryset.none()


        return queryset

    def get_table_class(self):

        """
        Return the class to use for the table.
        """
        if self.request.user.groups.filter(name='EXPORT').exists():
            return SchoolExportTable
        else:
            return SchoolTable

        return self.table_class


class SchoolAddView(LoginRequiredMixin,
                 GroupRequiredMixin,
                 FormView):
    template_name = 'schools/school_create_form.html'
    form_class = SchoolForm
    success_url = '/schools/school-list/'
    group_required = [u"CLM_Bridging"]

    def get_success_url(self):
        if self.request.POST.get('save_add_another', None):
            return '/clm/school-add/'
        if self.request.POST.get('save_and_continue', None):
            return '/clm/school-edit/' + str(self.request.session.get('instance_id')) + '/'
        return self.success_url

    def get_context_data(self, **kwargs):

        """Insert the form into the context dict."""
        if 'form' not in kwargs:
            kwargs['form'] = self.get_form()
        kwargs['is_allowed_create'] = is_allowed_create('Bridging')
        return super(SchoolAddView, self).get_context_data(**kwargs)

    def get_initial(self):
        initial = super(SchoolAddView, self).get_initial()
        data = {
            'new_school': self.request.GET.get('new_school', ''),
        }
        if self.request.GET.get('school_id'):
            instance = School.objects.get(id=self.request.GET.get('school_id'))
            data = SchoolSerializer(instance).data

        if data:
            data['new_school'] = self.request.GET.get('new_school', 'yes')
        initial = data

        return initial

    def form_valid(self, form):
        form.save(self.request)
        return super(SchoolAddView, self).form_valid(form)

    def get_form(self, form_class=None):
        if self.request.method == "POST":
            return SchoolForm(self.request.POST, instance=None, request=self.request)
        else:
            return SchoolForm(None, instance=None, request=self.request, initial=self.get_initial())


class SchoolEditView(LoginRequiredMixin,
                  GroupRequiredMixin,
                  FormView):
    template_name = 'schools/school_edit_form.html'
    form_class = SchoolForm
    success_url = '/schools/school-list/'
    group_required = [u"CLM_Bridging"]

    def get_success_url(self):
        if self.request.POST.get('save_add_another', None):
            return '/clm/school-add/'
        if self.request.POST.get('save_and_continue', None):
            return '/clm/school-edit/' + str(self.request.session.get('instance_id')) + '/'
        return self.success_url

    def get_context_data(self, **kwargs):

        """Insert the form into the context dict."""
        if 'form' not in kwargs:
            kwargs['form'] = self.get_form()
        kwargs['is_allowed_edit'] = is_allowed_edit('Bridging')
        return super(SchoolEditView, self).get_context_data(**kwargs)

    def get_form(self, form_class=None):
        instance = School.objects.get(id=self.kwargs['pk'])
        if self.request.method == "POST":
            return SchoolForm(self.request.POST, instance=instance, request=self.request)
        else:
            data = SchoolSerializer(instance).data
            return SchoolForm(data, instance=instance, request=self.request)

    def form_valid(self, form):
        instance = School.objects.get(id=self.kwargs['pk'])
        form.save(request=self.request, instance=instance)
        return super(SchoolEditView, self).form_valid(form)


class ClubListView(LoginRequiredMixin,
                  GroupRequiredMixin,
                  FilterView,
                  ExportMixin,
                  SingleTableView,
                  RequestConfig):

    table_class = ClubTable
    model = Club
    template_name = 'schools/club_list.html'
    table = ClubTable(Club.objects.all(), order_by='id')
    group_required = [u"CLM_Bridging"]

    def get_queryset(self):

        school_id = int(self.kwargs['school_id'])
        return Club.objects.filter(school_id=school_id).order_by('-id')

    def get_context_data(self, **kwargs):
        """Insert the form into the context dict."""
        kwargs['school_id'] = self.kwargs['school_id'] if 'school_id' in self.kwargs else None
        return super(ClubListView, self).get_context_data(**kwargs)


class ClubFormView(LoginRequiredMixin,
                       GroupRequiredMixin,
                       FormView):
    template_name = 'schools/club_form.html'
    form_class = ClubForm
    group_required = [u"CLM_Bridging"]

    def get_success_url(self):
        school_id = self.kwargs['school_id'] if 'school_id' in self.kwargs else None
        return '/schools/club-list/' + school_id

    def get_context_data(self, **kwargs):
        """Insert the form into the context dict."""
        if 'form' not in kwargs:
            kwargs['form'] = self.get_form()
            kwargs['school_id']  = self.kwargs['school_id'] if 'school_id' in self.kwargs else None
        return super(ClubFormView, self).get_context_data(**kwargs)

    def get_form(self, form_class=None):
        school_id = self.kwargs['school_id'] if 'school_id' in self.kwargs else None
        pk = self.kwargs['pk'] if 'pk' in self.kwargs else None

        if self.request.method == "POST":
            return ClubForm(self.request.POST, pk=pk, school_id=school_id, request=self.request)
        else:
            if pk:
                instance = Club.objects.get(id=pk)

                return ClubForm(instance=instance, school_id=school_id, pk=pk, request=self.request)
            return ClubForm(school_id=school_id, pk=pk, request=self.request)

    def form_valid(self, form):
        school_id = self.kwargs['school_id'] if 'school_id' in self.kwargs else None
        instance = self.kwargs['pk'] if 'pk' in self.kwargs else None
        form.save(request=self.request, school_id=school_id, instance=instance)
        return super(ClubFormView, self).form_valid(form)


def club_delete(request, pk):
    if request.user.is_authenticated:
        try:
            club = Club.objects.get(pk=pk)
            club.delete()
            result = {"isSuccessful": True}
        except Club.DoesNotExist:
            result = {"isSuccessful": False}
    else:
        result = {"isSuccessful": False}
    return JsonResponse(result)


class MeetingListView(LoginRequiredMixin,
                  GroupRequiredMixin,
                  FilterView,
                  ExportMixin,
                  SingleTableView,
                  RequestConfig):

    table_class = MeetingTable
    model = Meeting
    template_name = 'schools/meeting_list.html'
    table = MeetingTable(Meeting.objects.all(), order_by='id')
    group_required = [u"CLM_Bridging"]

    def get_queryset(self):

        school_id = int(self.kwargs['school_id'])
        return Meeting.objects.filter(school_id=school_id).order_by('-id')

    def get_context_data(self, **kwargs):
        """Insert the form into the context dict."""
        kwargs['school_id'] = self.kwargs['school_id'] if 'school_id' in self.kwargs else None
        return super(MeetingListView, self).get_context_data(**kwargs)


class MeetingFormView(LoginRequiredMixin,
                       GroupRequiredMixin,
                       FormView):
    template_name = 'schools/meeting_form.html'
    form_class = MeetingForm
    group_required = [u"CLM_Bridging"]

    def get_success_url(self):
        school_id = self.kwargs['school_id'] if 'school_id' in self.kwargs else None
        return '/schools/meeting-list/' + school_id

    def get_context_data(self, **kwargs):
        """Insert the form into the context dict."""
        if 'form' not in kwargs:
            kwargs['form'] = self.get_form()
            kwargs['school_id']  = self.kwargs['school_id'] if 'school_id' in self.kwargs else None
        return super(MeetingFormView, self).get_context_data(**kwargs)

    def get_form(self, form_class=None):
        school_id = self.kwargs['school_id'] if 'school_id' in self.kwargs else None
        pk = self.kwargs['pk'] if 'pk' in self.kwargs else None

        if self.request.method == "POST":
            return MeetingForm(self.request.POST, pk=pk, school_id=school_id, request=self.request)
        else:
            if pk:
                instance = Meeting.objects.get(id=pk)

                return MeetingForm(instance=instance, school_id=school_id, pk=pk, request=self.request)
            return MeetingForm(school_id=school_id, pk=pk, request=self.request)

    def form_valid(self, form):
        school_id = self.kwargs['school_id'] if 'school_id' in self.kwargs else None
        instance = self.kwargs['pk'] if 'pk' in self.kwargs else None
        form.save(request=self.request, school_id=school_id, instance=instance)
        return super(MeetingFormView, self).form_valid(form)


def meeting_delete(request, pk):
    if request.user.is_authenticated:
        try:
            meeting = Meeting.objects.get(pk=pk)
            meeting.delete()
            result = {"isSuccessful": True}
        except Meeting.DoesNotExist:
            result = {"isSuccessful": False}
    else:
        result = {"isSuccessful": False}
    return JsonResponse(result)


class CommunityInitiativeListView(LoginRequiredMixin,
                  GroupRequiredMixin,
                  FilterView,
                  ExportMixin,
                  SingleTableView,
                  RequestConfig):

    table_class = CommunityInitiativeTable
    model = CommunityInitiative
    template_name = 'schools/community_initiative_list.html'
    table = CommunityInitiativeTable(CommunityInitiative.objects.all(), order_by='id')
    group_required = [u"CLM_Bridging"]

    def get_queryset(self):

        school_id = int(self.kwargs['school_id'])
        return CommunityInitiative.objects.filter(school_id=school_id).order_by('-id')

    def get_context_data(self, **kwargs):
        """Insert the form into the context dict."""
        kwargs['school_id'] = self.kwargs['school_id'] if 'school_id' in self.kwargs else None
        return super(CommunityInitiativeListView, self).get_context_data(**kwargs)


class CommunityInitiativeFormView(LoginRequiredMixin,
                       GroupRequiredMixin,
                       FormView):
    template_name = 'schools/community_initiative_form.html'
    form_class = CommunityInitiativeForm
    group_required = [u"CLM_Bridging"]

    def get_success_url(self):
        school_id = self.kwargs['school_id'] if 'school_id' in self.kwargs else None
        return '/schools/community-initiative-list/' + school_id

    def get_context_data(self, **kwargs):
        """Insert the form into the context dict."""
        if 'form' not in kwargs:
            kwargs['form'] = self.get_form()
            kwargs['school_id']  = self.kwargs['school_id'] if 'school_id' in self.kwargs else None
        return super(CommunityInitiativeFormView, self).get_context_data(**kwargs)

    def get_form(self, form_class=None):
        school_id = self.kwargs['school_id'] if 'school_id' in self.kwargs else None
        pk = self.kwargs['pk'] if 'pk' in self.kwargs else None

        if self.request.method == "POST":
            return CommunityInitiativeForm(self.request.POST, pk=pk, school_id=school_id, request=self.request)
        else:
            if pk:
                instance = CommunityInitiative.objects.get(id=pk)

                return CommunityInitiativeForm(instance=instance, school_id=school_id, pk=pk, request=self.request)
            return CommunityInitiativeForm(school_id=school_id, pk=pk, request=self.request)

    def form_valid(self, form):
        school_id = self.kwargs['school_id'] if 'school_id' in self.kwargs else None
        instance = self.kwargs['pk'] if 'pk' in self.kwargs else None
        form.save(request=self.request, school_id=school_id, instance=instance)
        return super(CommunityInitiativeFormView, self).form_valid(form)


def community_initiative_delete(request, pk):
    if request.user.is_authenticated:
        try:
            initiative = CommunityInitiative.objects.get(pk=pk)
            initiative.delete()
            result = {"isSuccessful": True}
        except CommunityInitiative.DoesNotExist:
            result = {"isSuccessful": False}
    else:
        result = {"isSuccessful": False}
    return JsonResponse(result)


class HealthVisitListView(LoginRequiredMixin,
                  GroupRequiredMixin,
                  FilterView,
                  ExportMixin,
                  SingleTableView,
                  RequestConfig):

    table_class = HealthVisitTable
    model = HealthVisit
    template_name = 'schools/health_visit_list.html'
    table = HealthVisitTable(HealthVisit.objects.all(), order_by='id')
    group_required = [u"CLM_Bridging"]

    def get_queryset(self):

        school_id = int(self.kwargs['school_id'])
        return HealthVisit.objects.filter(school_id=school_id).order_by('-id')

    def get_context_data(self, **kwargs):
        """Insert the form into the context dict."""
        kwargs['school_id'] = self.kwargs['school_id'] if 'school_id' in self.kwargs else None
        return super(HealthVisitListView, self).get_context_data(**kwargs)


class HealthVisitFormView(LoginRequiredMixin,
                       GroupRequiredMixin,
                       FormView):
    template_name = 'schools/health_visit_form.html'
    form_class = HealthVisitForm
    group_required = [u"CLM_Bridging"]

    def get_success_url(self):
        school_id = self.kwargs['school_id'] if 'school_id' in self.kwargs else None
        return '/schools/health-visit-list/' + school_id

    def get_context_data(self, **kwargs):
        """Insert the form into the context dict."""
        if 'form' not in kwargs:
            kwargs['form'] = self.get_form()
            kwargs['school_id']  = self.kwargs['school_id'] if 'school_id' in self.kwargs else None
        return super(HealthVisitFormView, self).get_context_data(**kwargs)

    def get_form(self, form_class=None):
        school_id = self.kwargs['school_id'] if 'school_id' in self.kwargs else None
        pk = self.kwargs['pk'] if 'pk' in self.kwargs else None

        if self.request.method == "POST":
            return HealthVisitForm(self.request.POST, pk=pk, school_id=school_id, request=self.request)
        else:
            if pk:
                instance = HealthVisit.objects.get(id=pk)

                return HealthVisitForm(instance=instance, school_id=school_id, pk=pk, request=self.request)
            return HealthVisitForm(school_id=school_id, pk=pk, request=self.request)

    def form_valid(self, form):
        school_id = self.kwargs['school_id'] if 'school_id' in self.kwargs else None
        instance = self.kwargs['pk'] if 'pk' in self.kwargs else None
        form.save(request=self.request, school_id=school_id, instance=instance)
        return super(HealthVisitFormView, self).form_valid(form)


def health_visit_delete(request, pk):
    if request.user.is_authenticated:
        try:
            visit = HealthVisit.objects.get(pk=pk)
            visit.delete()
            result = {"isSuccessful": True}
        except HealthVisit.DoesNotExist:
            result = {"isSuccessful": False}
    else:
        result = {"isSuccessful": False}
    return JsonResponse(result)


def add_csv_to_zip(zipfile_obj, filename, queryset):
    csv_output = io.StringIO()
    csv_writer = csv.writer(csv_output)

    csv_output.write(codecs.BOM_UTF8.decode('utf-8'))

    headers = [field.name for field in queryset.model._meta.fields]
    csv_writer.writerow(headers)

    for obj in queryset:
        csv_writer.writerow([getattr(obj, field) for field in headers])

    zipfile_obj.writestr(filename, csv_output.getvalue())


@login_required(login_url='/users/login')
def export_school_background(request):
    try:
        user = request.user
        school_id = user.school.id if hasattr(user, 'school') and user.school else 0
        partner_id = user.partner_id if hasattr(user, 'partner_id') else 0
        partner_name = user.partner.name if hasattr(user, 'partner') and user.partner else ''

        qs_school = School.objects.filter(is_bma=True).order_by('-id')
        if not (user.is_staff or has_group(user, 'CLM_BRIDGING_ALL')):
            if school_id > 0:
                qs_school = School.objects.filter(id=school_id)
            elif partner_id > 0:
                qs_school = School.objects.filter(
                    is_bma=True,
                    id__in=PartnerOrganization.objects.filter(id=partner_id).values_list('schools', flat=True)
                )
            else:
                qs_school = qs_school.none()

        school_ids = qs_school.values_list('id', flat=True)
        qs_club = Club.objects.filter(school_id__in=school_ids).order_by('-id')
        qs_meeting = Meeting.objects.filter(school_id__in=school_ids).order_by('-id')
        qs_community_initiative = CommunityInitiative.objects.filter(school_id__in=school_ids).order_by('-id')
        qs_health_visit = HealthVisit.objects.filter(school_id__in=school_ids).order_by('-id')

        zip_output = io.BytesIO()
        with zipfile.ZipFile(zip_output, 'w') as zf:
            add_csv_to_zip(zf, 'qs_school_data.csv', qs_school)
            add_csv_to_zip(zf, 'qs_club_data.csv', qs_club)
            add_csv_to_zip(zf, 'qs_meeting_data.csv', qs_meeting)
            add_csv_to_zip(zf, 'qs_community_initiative_data.csv', qs_community_initiative)
            add_csv_to_zip(zf, 'qs_health_visit_data.csv', qs_health_visit)

        unique_id = str(uuid.uuid4())
        file_name = "out_file_{}.zip".format(unique_id)

        file_path = os.path.join('export', file_name)

        try:
            default_storage.save(file_path, ContentFile(zip_output.getvalue()))
        except Exception as e:
            logging.error("Error saving file: %s", str(e))
            return HttpResponse("An error occurred while saving the file.", status=500)

        ExportHistory.objects.create(
            export_type='School List',
            created_by=request.user,
            partner_name=partner_name
        )

        return HttpResponse(file_name)
    except Exception as e:
        logging.error("An error occurred during the export process:")
        logging.error(traceback.format_exc())
        return HttpResponse("An error occurred: " + str(e), status=500)


class SchoolAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if not self.request.user.is_authenticated:
            return School.objects.none()

        qs = School.objects.all()

        if self.q:
            qs = School.objects.filter(
                Q(number__istartswith=self.q) | Q(name__istartswith=self.q)
            )

        return qs
