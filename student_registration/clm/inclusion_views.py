# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, FormView, TemplateView, UpdateView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, JsonResponse, HttpResponseBadRequest, HttpResponseForbidden


from braces.views import GroupRequiredMixin, SuperuserRequiredMixin
from rest_framework import viewsets, mixins, permissions
from rest_framework import status

from django.db.models import F, Q

from django_filters.views import FilterView
from django_tables2 import MultiTableMixin, RequestConfig, SingleTableView
from django_tables2.export.views import ExportMixin

from student_registration.backends.djqscsv import render_to_csv_response

from .inclusion_tables import InclusionTable
from .inclusion_filters import InclusionFilter
from .models import Inclusion
from .inclusion_forms import InclusionForm, InclusionAssessmentForm, InclusionFollowupForm
from .utils import is_allowed_create, is_allowed_edit
from .inclusion_serializers import InclusionSerializer


class InclusionAddView(LoginRequiredMixin,
                  GroupRequiredMixin,
                  FormView):

    template_name = 'clm/inclusion_form.html'
    form_class = InclusionForm
    success_url = '/clm/inclusion-list/'
    group_required = [u"CLM_Inclusion"]

    def get_success_url(self):
        if self.request.POST.get('save_add_another', None):
            return '/clm/inclusion-add/'
        if self.request.POST.get('save_and_continue', None):
            return '/clm/inclusion-edit/' + str(self.request.session.get('instance_id')) + '/'
        return self.success_url

    def get_context_data(self, **kwargs):
        """Insert the form into the context dict."""
        if 'form' not in kwargs:
            kwargs['form'] = self.get_form()
        kwargs['is_allowed_create'] = is_allowed_create('Inclusion')
        return super(InclusionAddView, self).get_context_data(**kwargs)

    def form_valid(self, form):
        form.save(self.request)
        return super(InclusionAddView, self).form_valid(form)

    def get_form(self, form_class=None):

        if self.request.method == "POST":
            return InclusionForm(self.request.POST, instance=None, request=self.request)
        else :
            return InclusionForm(None, instance=None, request=self.request, initial=self.get_initial())

    def get_initial(self):
            initial = super(InclusionAddView, self).get_initial()
            data = {
                'new_registry': self.request.GET.get('new_registry', ''),
                'student_outreached': self.request.GET.get('student_outreached', ''),
                'have_barcode': self.request.GET.get('have_barcode', '')
            }
            if self.request.GET.get('enrollment_id'):
                instance = Inclusion.objects.get(id=self.request.GET.get('enrollment_id'))
                data = InclusionSerializer(instance).data
                data['student_nationality'] = data['student_nationality_id']
                data['learning_result'] = ''

            if data:
                data['new_registry'] = self.request.GET.get('new_registry', 'yes')
                data['student_outreached'] = self.request.GET.get('student_outreached', '')
                data['have_barcode'] = self.request.GET.get('have_barcode', '')
            initial = data

            return initial


class InclusionEditView(LoginRequiredMixin,
                        GroupRequiredMixin,
                        FormView):

    template_name = 'clm/inclusion_form.html'
    form_class = InclusionForm
    success_url = '/clm/inclusion-list/'
    group_required = [u"CLM_Inclusion"]

    def get_success_url(self):
        if self.request.POST.get('save_add_another', None):
            return '/clm/inclusion-add/'
        if self.request.POST.get('save_and_continue', None):
            return '/clm/inclusion-edit/' + str(self.request.session.get('instance_id')) + '/'
        return self.success_url

    def get_context_data(self, **kwargs):
        """Insert the form into the context dict."""
        if 'form' not in kwargs:
            kwargs['form'] = self.get_form()
        kwargs['is_allowed_edit'] = is_allowed_edit('Inclusion')
        return super(InclusionEditView, self).get_context_data(**kwargs)

    def get_form(self, form_class=None):
        instance = Inclusion.objects.get(id=self.kwargs['pk'])
        if self.request.method == "POST":
            return InclusionForm(self.request.POST, instance=instance, request=self.request)
        else:
            data = InclusionSerializer(instance).data
            data['student_nationality'] = data['student_nationality_id']
            return InclusionForm(data, instance=instance, request=self.request)

    def form_valid(self, form):
        instance = Inclusion.objects.get(id=self.kwargs['pk'])
        form.save(request=self.request, instance=instance)
        return super(InclusionEditView, self).form_valid(form)


class InclusionListView(LoginRequiredMixin,
                        GroupRequiredMixin,
                        FilterView,
                        ExportMixin,
                        SingleTableView,
                        RequestConfig):

    table_class = InclusionTable
    model = Inclusion
    template_name = 'clm/inclusion_list.html'
    table = InclusionTable(Inclusion.objects.all(), order_by='id')
    group_required = [u"CLM_Inclusion"]
    filterset_class = InclusionFilter

    def get_queryset(self):
        partner_id = self.request.user.partner_id
        if not self.request.user.is_staff and partner_id:
            return Inclusion.objects.filter(round__current_year_inclusion=True,partner=partner_id).order_by('-id')
        elif self.request.user.is_staff:
            return Inclusion.objects.filter(round__current_year_inclusion=True).order_by('-id')
        return Inclusion.objects.none()


class InclusionAssessmentView(LoginRequiredMixin,
                              GroupRequiredMixin,
                              FormView):

    template_name = 'clm/inclusion_assessment.html'
    form_class = InclusionAssessmentForm
    success_url = '/clm/inclusion-list/'
    group_required = [u"CLM_Inclusion"]

    def get_context_data(self, **kwargs):
        """Insert the form into the context dict."""
        if 'form' not in kwargs:
            kwargs['form'] = self.get_form()
        return super(InclusionAssessmentView, self).get_context_data(**kwargs)

    def get_form(self, form_class=None):
        form_class = self.get_form_class()
        instance = Inclusion.objects.get(id=self.kwargs['pk'])
        if self.request.method == "POST":
            return form_class(self.request.POST, instance=instance, request=self.request)
        else:
            return form_class(instance=instance, request=self.request)

    def form_valid(self, form):
        instance = Inclusion.objects.get(id=self.kwargs['pk'])
        form.save(request=self.request, instance=instance)
        return super(InclusionAssessmentView, self).form_valid(form)


class InclusionFollowupView(LoginRequiredMixin,
                            GroupRequiredMixin,
                            FormView):

    template_name = 'clm/inclusion_followup.html'
    form_class = InclusionFollowupForm
    success_url = '/clm/inclusion-list/'
    group_required = [u"CLM_Inclusion"]

    def get_context_data(self, **kwargs):
        """Insert the form into the context dict."""
        if 'form' not in kwargs:
            kwargs['form'] = self.get_form()
        return super(InclusionFollowupView, self).get_context_data(**kwargs)

    def get_form(self, form_class=None):
        form_class = self.get_form_class()
        instance = Inclusion.objects.get(id=self.kwargs['pk'])
        if self.request.method == "POST":
            return form_class(self.request.POST, instance=instance)
        else:
            return form_class(instance=instance)

    def form_valid(self, form):
        instance = Inclusion.objects.get(id=self.kwargs['pk'])
        form.save(request=self.request, instance=instance)
        return super(InclusionFollowupView, self).form_valid(form)


def inclusion_delete_view(request, pk):
    if request.user.is_authenticated:
        try:
            registration =  Inclusion.objects.get(pk=pk)
            registration.delete()
            result = {"isSuccessful": True}
        except Inclusion.DoesNotExist:
            result = {"isSuccessful": False}
    else:
        result = {"isSuccessful": False}
    return JsonResponse(result)


@login_required(login_url='/users/login')
def inclusion_export(request):
    round_id = request.GET.get('round', None)
    partner_id = request.user.partner_id

    if not request.user.is_staff and partner_id and round_id:
        queryset = Inclusion.objects.filter(
            Q(round__isnull=True) | Q(round=round_id, partner=partner_id)
        ).order_by('-id')
    elif request.user.is_staff and round_id:
        queryset = Inclusion.objects.filter(
            Q(round=round_id)
        ).order_by('-id')
    else:
        queryset = Inclusion.objects.none()


    headers = {
        'id': 'enropllment_id',
        'partner__name': 'Partner',
        'source_of_identification': 'Source of Identification',
        'round__name': 'CLM Round',
        'first_attendance_date': 'first attendance date',
        'governorate__name_en': 'Governorate',
        'cadaster__name_en': 'Cadaster',
        'district__name_en': 'District',
        'location': 'Location',
        'student__first_name': 'First name',
        'student__father_name': 'Father name',
        'student__last_name': 'Last name',
        'student__sex': 'Sex',
        'student__birthday_day': 'Birthday - day',
        'student__birthday_month': 'Birthday - month',
        'student__birthday_year': 'Birthday - year',
        'student__nationality__name': 'Student Nationality',
        'other_nationality': 'Student Nationality Specify',
        'student__mother_fullname': 'Mother fullname',
        'student__p_code': 'P-Code If a child lives in a tent / Brax in a random camp',
        'student__id_number': 'ID number',
        'student__number': 'unique number',
        'disability__name_en': 'Does the child have any disability or special need?',
        'internal_number': 'Internal number',
        'comments': 'Comments',
        'phone_number': 'Phone number',
        'phone_number_confirm': 'Phone number confirm',
        'phone_owner': 'phone owner',
        'second_phone_number': 'Second Phone number',
        'second_phone_number_confirm': 'Second Phone number confirm',
        'second_phone_owner': 'Second phone owner',
        'id_type': 'ID Type',
        'case_number': 'UNHCR case number',
        'case_number_confirm': 'UNHCR case number confirm',
        'individual_case_number': 'Child individual ID',
        'individual_case_number_confirm': 'Child individual ID confirm',
        'parent_individual_case_number': 'Parent individual ID',
        'parent_individual_case_number_confirm': 'Parent individual ID confirm',
        'recorded_number': 'UNHCR recorded barcode',
        'recorded_number_confirm': 'UNHCR recorded barcode confirm',
        'national_number': 'Child Lebanese ID number',
        'national_number_confirm': 'Child Lebanese ID number confirm',
        'syrian_national_number': 'Child Syrian ID number',
        'syrian_national_number_confirm': 'Child Syrian ID number confirm',
        'sop_national_number': 'Child Palestinian ID number',
        'sop_national_number_confirm': 'Child Palestinian ID number confirm',
        'parent_national_number': 'Parent Lebanese ID number',
        'parent_national_number_confirm': 'Parent Lebanese ID number confirm',
        'parent_syrian_national_number': 'Parent Syrian ID number',
        'parent_syrian_national_number_confirm': 'Parent Syrian ID number confirm',
        'parent_sop_national_number': 'Parent Palestinian ID number',
        'parent_sop_national_number_confirm': 'Parent Palestinian ID number confirm',
        'parent_other_number': 'ID number of the Caretaker',
        'parent_other_number_confirm': 'ID number of the Caretaker confirm',
        'other_number': 'ID number of the child',
        'other_number_confirm': 'ID number of the child confirm',
        'main_caregiver': 'Main Caregiver',
        'main_caregiver_nationality__name': 'main caregiver nationality',
        'other_caregiver_relationship': 'other caregiver relationship',
        'caretaker_first_name': 'Caretaker first name',
        'caretaker_middle_name': 'Caretaker middle name',
        'caretaker_last_name': 'Caretaker last name',
        'caretaker_mother_name': 'Caretaker mother name',
        'caretaker_birthday_year': 'Caretaker birthday year',
        'caretaker_birthday_month': 'Caretaker birthday month',
        'caretaker_birthday_day': 'Caretaker birthday day',
        'have_labour': 'Does the child participate in work?',
        'labour_type': 'What is the type of work?',

        'participation': 'Level of participation / Absence',
        'barriers': 'The main barriers affecting the daily attendance and performance of the child or drop out of school?',
        'learning_result': 'Based on the overall score, what is the recommended learning path?',
        'owner__username': 'owner',
        'modified_by__username': 'modified_by',
        'created': 'created',
        'modified': 'modified',

        'referral_programme_type_1': 'Referral programme type 1',
        'referral_partner_1': 'Referral partner 1',
        'referral_date_1': 'Referral date 1',
        'confirmation_date_1': 'Referral confirmation date 1',

        'referral_programme_type_2': 'Referral programme type 2',
        'referral_partner_2': 'Referral partner 2',
        'referral_date_2': 'Referral date 2',
        'confirmation_date_2': 'Referral confirmation date 2',

        'referral_programme_type_3': 'Referral programme type 3',
        'referral_partner_3': 'Referral partner 3',
        'referral_date_3': 'Referral date 3',
        'confirmation_date_3': 'Referral confirmation date 3',
        'additional_comments': 'Comments',
        'child_dropout': 'Child dropout',
        'child_dropout_specify': 'Child dropout specify',
        'caregiver_trained_parental_engagement': 'Caregiver Trained Parental Engagement',
    }

    field_list = (
        'id',
        'partner__name',
        'source_of_identification',
        'round__name',
        'first_attendance_date',
        'governorate__name_en',
        'district__name_en',
        'cadaster__name_en',
        'location',
        'student__first_name',
        'student__father_name',
        'student__last_name',
        'student__sex',
        'student__birthday_day',
        'student__birthday_month',
        'student__birthday_year',
        'student__nationality__name',
        'other_nationality',
        'student__mother_fullname',
        'student__p_code',
        'student__id_number',
        'student__number',
        'disability__name_en',
        'internal_number',
        'comments',
        'phone_number',
        'phone_number_confirm',
        'phone_owner',
        'second_phone_number',
        'second_phone_number_confirm',
        'second_phone_owner',
        'id_type',
        'case_number',
        'case_number_confirm',
        'individual_case_number',
        'individual_case_number_confirm',
        'parent_individual_case_number',
        'parent_individual_case_number_confirm',
        'recorded_number',
        'recorded_number_confirm',
        'national_number',
        'national_number_confirm',
        'syrian_national_number',
        'syrian_national_number_confirm',
        'sop_national_number',
        'sop_national_number_confirm',
        'parent_national_number',
        'parent_national_number_confirm',
        'parent_syrian_national_number',
        'parent_syrian_national_number_confirm',
        'parent_sop_national_number',
        'parent_sop_national_number_confirm',
        'parent_other_number',
        'parent_other_number_confirm',
        'other_number',
        'other_number_confirm',
        'main_caregiver',
        'main_caregiver_nationality__name',
        'other_caregiver_relationship',
        'caretaker_first_name',
        'caretaker_middle_name',
        'caretaker_last_name',
        'caretaker_mother_name',
        'caretaker_birthday_year',
        'caretaker_birthday_month',
        'caretaker_birthday_day',
        'have_labour',
        'labour_type',

        'participation',
        'barriers',
        'learning_result',

        'referral_programme_type_1',
        'referral_partner_1',
        'referral_date_1',
        'confirmation_date_1',

        'referral_programme_type_2',
        'referral_partner_2',
        'referral_date_2',
        'confirmation_date_2',

        'referral_programme_type_3',
        'referral_partner_3',
        'referral_date_3',
        'confirmation_date_3',

        'owner__username',
        'modified_by__username',
        'created',
        'modified',
        'additional_comments',
        'child_dropout',
        'child_dropout_specify',
        'caregiver_trained_parental_engagement'
    )

    if queryset.exists():
        qs = queryset.values(*field_list)
        return render_to_csv_response(qs, field_header_map=headers, field_order=field_list)
    else:
        # Return an empty response or handle the empty case as needed
        return HttpResponse("No data available for export", content_type="text/plain")


####################### API VIEWS #############################


class InclusionViewSet(mixins.RetrieveModelMixin,
                 mixins.ListModelMixin,
                 mixins.CreateModelMixin,
                 mixins.UpdateModelMixin,
                 viewsets.GenericViewSet):

    model = Inclusion
    queryset = Inclusion.objects.all()
    serializer_class = InclusionSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        from datetime import datetime

        qs = self.queryset
        if self.request.GET.get('creation_date', None):
            return self.queryset.filter(created__gte=datetime.strptime(self.request.GET.get('creation_date', None), '%Y-%m-%d'))[:5000]
        if self.request.GET.get('school', None):
            return self.queryset.filter(school_id=self.request.GET.get('school', None))

        return qs

    def delete(self, request, *args, **kwargs):
        instance = self.model.objects.get(id=kwargs['pk'])
        instance.delete()
        return JsonResponse({'status': status.HTTP_200_OK})
