from __future__ import absolute_import, unicode_literals

from django.urls import re_path

from . import views, education_view, services_view, attendance_views

app_name = 'mscc'

urlpatterns = [

    re_path(
        r'^Child-Add/$',
        view=views.MainAddView.as_view(),
        name='child_add'
    ),
    re_path(
        r'^Child-Edit/(?P<pk>[\w.@+-]+)/$',
        view=views.MainEditView.as_view(),
        name='child_edit'
    ),
    re_path(
        r'^New-Round/(?P<pk>[\w.@+-]+)/$',
        view=views.NewRoundView.as_view(),
        name='new_round'
    ),
    re_path(
        r'^New-Round-Redirect/$',
        view=views.NewRoundRedirectView.as_view(),
        name='new_round_redirect'
    ),
    re_path(
        r'^Child-Mark-Delete/(?P<pk>[\w.@+-]+)/$',
        view=views.MainMarkDeleteView,
        name='child_mark_deleted'
    ),
    re_path(
        r'^List/$',
        view=views.MainListView.as_view(),
        name='list'
    ),
    re_path(
        r'^Dashboard/$',
        view=views.DashboardView.as_view(),
        name='dashboard'
    ),
    re_path(
        r'^Dashboard-Youth/$',
        view=views.DashboardYouthView.as_view(),
        name='dashboard_youth'
    ),
    re_path(
        r'^Services/Education-Assessment-Add/(?P<registry>[\w.@+-]+)/$',
        view=education_view.EducationAssessmentFormView.as_view(),
        name='service_education_assessment_add'
    ),
    re_path(
        r'^Services/Education-Assessment-Edit/(?P<registry>[\w.@+-]+)/(?P<pk>[\w.@+-]+)/$',
        view=education_view.EducationAssessmentFormView.as_view(),
        name='service_education_assessment_edit'
    ),
    re_path(
        r'^Services/Diagnostic-Assessment-Add/(?P<registry>[\w.@+-]+)/$',
        view=education_view.DiagnosticAssessmentFormView.as_view(),
        name='service_diagnostic_assessment_add'
    ),
    re_path(
        r'^Services/Diagnostic-Assessment-Edit/(?P<registry>[\w.@+-]+)/(?P<pk>[\w.@+-]+)/$',
        view=education_view.DiagnosticAssessmentFormView.as_view(),
        name='service_diagnostic_assessment_edit'
    ),
    re_path(
        r'^Services/Education-Add/(?P<registry>[\w.@+-]+)/(?P<package_type>[\w\s.@+-]+)/$',
        view=education_view.EducationServiceFormView.as_view(),
        name='service_education_add'
    ),
    re_path(
        r'^Services/Education-Edit/(?P<registry>[\w.@+-]+)/(?P<pk>[\w.@+-]+)/(?P<package_type>[\w\s.@+-]+)/$',
        view=education_view.EducationServiceFormView.as_view(),
        name='service_education_edit'
    ),
    re_path(
        r'^Services/RS-Add/(?P<registry>[\w.@+-]+)/$',
        view=education_view.EducationRSServiceFormView.as_view(),
        name='service_education_rs_add'
    ),
    re_path(
        r'^Services/RS-Edit/(?P<registry>[\w.@+-]+)/(?P<pk>[\w.@+-]+)/$',
        view=education_view.EducationRSServiceFormView.as_view(),
        name='service_education_rs_edit'
    ),
    re_path(
        r'^Child-Profile/(?P<pk>[\w.@+-]+)/$',
        view=views.ProfileView.as_view(),
        name='child_profile'
    ),
    re_path(
        r'^Services/Inclusion-Add/(?P<registry>[\w.@+-]+)/$',
        view=services_view.InclusionFormView.as_view(),
        name='service_inclusion_add'
    ),
    re_path(
        r'^Services/Inclusion-Edit/(?P<registry>[\w.@+-]+)/(?P<pk>[\w.@+-]+)/$',
        view=services_view.InclusionFormView.as_view(),
        name='service_inclusion_edit'
    ),
    re_path(
        r'^Services/Digital-Add/(?P<registry>[\w.@+-]+)/$',
        view=services_view.DigitalFormView.as_view(),
        name='service_digital_add'
    ),
    re_path(
        r'^Services/Digital-Edit/(?P<registry>[\w.@+-]+)/(?P<pk>[\w.@+-]+)/$',
        view=services_view.DigitalFormView.as_view(),
        name='service_digital_edit'
    ),
    re_path(
        r'^Services/Health-Nutrition-Add/(?P<registry>[\w.@+-]+)/(?P<age>[\w.@+-]+)/$',
        view=services_view.HealthNutritionFormView.as_view(),
        name='service_health_nutrition_add'
    ),
    re_path(
        r'^Services/Health-Nutrition-Edit/(?P<registry>[\w.@+-]+)/(?P<age>[\w.@+-]+)/(?P<pk>[\w.@+-]+)/$',
        view=services_view.HealthNutritionFormView.as_view(),
        name='service_health_nutrition_edit'
    ),
    re_path(
        r'^Services/Health-Nutrition-Referral-Add/(?P<registry>[\w.@+-]+)/$',
        view=services_view.HealthNutritionReferralFormView.as_view(),
        name='service_health_nutrition_referral_add'
    ),
    re_path(
        r'^Services/Health-Nutrition-Referral-Edit/(?P<registry>[\w.@+-]+)/(?P<pk>[\w.@+-]+)/$',
        view=services_view.HealthNutritionReferralFormView.as_view(),
        name='service_health_nutrition_referral_edit'
    ),
    re_path(
        r'^Services/PSS-Add/(?P<registry>[\w.@+-]+)/$',
        view=services_view.PSSFormView.as_view(),
        name='service_pss_add'
    ),
    re_path(
        r'^Services/PSS-Edit/(?P<registry>[\w.@+-]+)/(?P<pk>[\w.@+-]+)/$',
        view=services_view.PSSFormView.as_view(),
        name='service_pss_edit'
    ),
    re_path(
        r'^Services/Youth-Kit-Add/(?P<registry>[\w.@+-]+)/$',
        view=services_view.YouthKitServiceFormView.as_view(),
        name='service_youth_kit_add'
    ),
    re_path(
        r'^Services/Youth-Kit-Edit/(?P<registry>[\w.@+-]+)/(?P<pk>[\w.@+-]+)/$',
        view=services_view.YouthKitServiceFormView.as_view(),
        name='service_youth_kit_edit'
    ),
    re_path(
        r'^Services/Youth-Maharati-Add/(?P<registry>[\w.@+-]+)/$',
        view=services_view.YouthServiceMaharatiFormView.as_view(),
        name='service_youth_maharati_add'
    ),
    re_path(
        r'^Services/Youth-Maharati-Edit/(?P<registry>[\w.@+-]+)/(?P<pk>[\w.@+-]+)/$',
        view=services_view.YouthServiceMaharatiFormView.as_view(),
        name='service_youth_maharati_edit'
    ),
    re_path(
        r'^Services/Youth-Gil-Add/(?P<registry>[\w.@+-]+)/$',
        view=services_view.YouthServiceGilFormView.as_view(),
        name='service_youth_gil_add'
    ),
    re_path(
        r'^Services/Youth-Gil-Edit/(?P<registry>[\w.@+-]+)/(?P<pk>[\w.@+-]+)/$',
        view=services_view.YouthServiceGilFormView.as_view(),
        name='service_youth_gil_edit'
    ),
    re_path(
        r'^Services/Follow-Up-Add/(?P<registry>[\w.@+-]+)/$',
        view=services_view.FollowUpFormView.as_view(),
        name='service_follow_up_add'
    ),
    re_path(
        r'^Services/Follow-Up-Edit/(?P<registry>[\w.@+-]+)/(?P<pk>[\w.@+-]+)/$',
        view=services_view.FollowUpFormView.as_view(),
        name='service_follow_up_edit'
    ),
    re_path(
        r'^Services/Youth-Assessment-Add/(?P<registry>[\w.@+-]+)/$',
        view=services_view.YouthAssessmentFormView.as_view(),
        name='service_youth_assessment_add'
    ),
    re_path(
        r'^Services/Youth-Assessment-Edit/(?P<registry>[\w.@+-]+)/(?P<pk>[\w.@+-]+)/$',
        view=services_view.YouthAssessmentFormView.as_view(),
        name='service_youth_assessment_edit'
    ),
    re_path(
        r'^Services/Youth-Referral-Add/(?P<registry>[\w.@+-]+)/$',
        view=services_view.YouthReferralFormView.as_view(),
        name='service_youth_referral_add'
    ),
    re_path(
        r'^Services/Youth-Referral-Edit/(?P<registry>[\w.@+-]+)/(?P<pk>[\w.@+-]+)/$',
        view=services_view.YouthReferralFormView.as_view(),
        name='service_youth_referral_edit'
    ),
    re_path(
        'Outreach-Child-Search/$',
        views.outreach_child_search,
        name='outreach_child_search'
    ),
    re_path(
        'Outreach-Child/$',
        views.outreach_child,
        name='outreach_child'
    ),
    re_path(
        r'^Referral-Add/(?P<registry>[\w.@+-]+)/$',
        view=views.ReferralFormView.as_view(),
        name='referral_add'
    ),
    re_path(
        r'^Referral-Edit/(?P<registry>[\w.@+-]+)/(?P<pk>[\w.@+-]+)/$',
        view=views.ReferralFormView.as_view(),
        name='referral_edit'
    ),
    re_path(
        'Old-Child-Search/$',
        views.old_child_search,
        name='old_child_search'
    ),
    re_path(
        'Get-Old-Child-Data/$',
        views.old_child_data,
        name='old_child_data'
    ),
    re_path(
        'Child-Duplication-Check/$',
        views.child_duplication_check,
        name='child_duplication_check'
    ),
    re_path(
        'Quick-Search/$',
        views.quick_search,
        name='quick_search'
    ),
    re_path(
        'Find-Programme-Details/$',
        view=views.ProgrammeDetails.as_view(),
        name='find_programme_details'
    ),
    re_path(
        'Child-Profile-Preview/$',
        view=views.ChildProfilePreview.as_view(),
        name='child_profile_preview'
    ),
    re_path(
        r'^Attendance/$',
        view=attendance_views.AttendanceView.as_view(),
        name='attendance'
    ),
    re_path(
        'Load-Attendance-Children/$',
        view=attendance_views.LoadAttendanceChildren.as_view(),
        name='load_attendance_children'
    ),
    re_path(
        'Save-Attendance-Children/$',
        view=attendance_views.save_attendance_children,
        name='save_attendance_children'
    ),
    re_path(
        'Attendance-Child/(?P<child>[\w.@+-]+)/$',
        view=attendance_views.LoadAttendanceChild.as_view(),
        name='attendance_child'
    ),
    re_path(
        'attendance-report/$',
        attendance_views.AttendanceReport.as_view(),
        name='attendance_report'
    ),
    re_path(
        r'^Services/Follow-Up-View-ALl/(?P<registry>[\w.@+-]+)/$',
        view=services_view.FollowUpViewAll.as_view(),
        name='service_follow_up_view_all'
    ),
    re_path(
        r'^Services/Education-Grading-Add/(?P<registry>[\w.@+-]+)/(?P<programme_type>[\w\s.@+-]+)/$',
        view=education_view.EducationGradingFormView.as_view(),
        name='service_education_grading_add'
    ),
    re_path(
        r'^Services/Education-Grading-Edit/(?P<registry>[\w.@+-]+)/(?P<programme_type>[\w\s.@+-]+)/(?P<pre_post>[\w\s.@+-]+)/(?P<pk>[\w.@+-]+)/$',
        view=education_view.EducationGradingFormView.as_view(),
        name='service_education_grading_edit'
    ),
    re_path(
        r'^Services/Youth-Scoring-Add/(?P<registry>[\w.@+-]+)/(?P<programme_type>[\w\s.@+-]+)/$',
        view=education_view.YouthScoringFormView.as_view(),
        name='service_youth_scoring_add'
    ),
    re_path(
        r'^Services/Youth-Scoring-Edit/(?P<registry>[\w.@+-]+)/(?P<programme_type>[\w\s.@+-]+)/(?P<pre_post>[\w\s.@+-]+)/(?P<pk>[\w.@+-]+)/$',
        view=education_view.YouthScoringFormView.as_view(),
        name='service_youth_scoring_edit'
    ),
    re_path(
        r'^Services/Education-School-Grading/(?P<registry>[\w.@+-]+)/(?P<programme_type>[\w\s.@+-]+)/(?P<pk>[\w.@+-]+)/$',
        view=education_view.EducationSchoolGradingFormView.as_view(),
        name='service_school_grading'
    ),
    re_path(
        r'^Services/Recreational-Add/(?P<registry>[\w.@+-]+)/$',
        view=services_view.RecreationalFormView.as_view(),
        name='service_recreational_add'
    ),
    re_path(
        r'^Services/Recreational-Edit/(?P<registry>[\w.@+-]+)/(?P<pk>[\w.@+-]+)/$',
        view=services_view.RecreationalFormView.as_view(),
        name='service_recreational_edit'
    ),
    re_path(
        r'^Child-Registration-Cancel/(?P<pk>[\w.@+-]+)/$',
        view=views.MainRegistrationCancelView,
        name='child_registration_cancel'
    ),
    re_path(
        r'^export-list-background/$',
        view=views.export_list_background,
        name='export_list_background'
    ),
    re_path(
        r"^export-download/(?P<file_name>.+)/$",
        view=views.get_file,
        name='export_download'
    ),

    re_path(
        r"^export-download-csv/(?P<file_name>.+)/$",
        view=views.get_file_csv,
        name='export_download_csv'
    ),

    re_path(
        r'^Services/Lego-Add/(?P<registry>[\w.@+-]+)/(?P<age>[\w.@+-]+)/$',
        view=services_view.LegoServiceFormView.as_view(),
        name='service_lego_add'
    ),
    re_path(
        r'^Services/Lego-Edit/(?P<registry>[\w.@+-]+)/(?P<age>[\w.@+-]+)/(?P<pk>[\w.@+-]+)/$',
        view=services_view.LegoServiceFormView.as_view(),
        name='service_lego_edit'
    ),
]
