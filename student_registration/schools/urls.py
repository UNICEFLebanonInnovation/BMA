from __future__ import absolute_import, unicode_literals

from django.urls import re_path

from . import views

app_name = 'schools'

urlpatterns = [

    re_path(
        r'^profile/$',
        view=views.ProfileView.as_view(),
        name='profile'
    ),
    re_path(
        r'^partner/$',
        view=views.PartnerView.as_view(),
        name='partner'
    ),
    re_path(
        r'^documents/$',
        view=views.PublicDocumentView.as_view(),
        name='documents'
    ),
    re_path(
        r'^autocomplete/$',
        view=views.AutocompleteView.as_view(),
        name='autocomplete'
    ),
    re_path(
        r'^evaluation/$',
        view=views.EvaluationView.as_view(),
        name='evaluation'
    ),
    re_path(
        r'^evaluation/update_classroom/(?P<pk>[\w.@+-]+)/$',
        view=views.Update_Class.as_view(),
        name='update_classroom'
    ),
    re_path(
        r'^evaluation/update_classroom_c1/(?P<pk>[\w.@+-]+)/$',
        view=views.Update_Class_c1.as_view(),
        name='update_classroom_c1'
    ),
    re_path(
        r'^evaluation/update_classroom_c3/(?P<pk>[\w.@+-]+)/$',
        view=views.Update_Class_C3.as_view(),
        name='update_classroom_c3'
    ),
    re_path(
        r'^evaluation/update_classroom_c4/(?P<pk>[\w.@+-]+)/$',
        view=views.Update_Class_c4.as_view(),
        name='update_classroom_c4'
    ),
    re_path(
        r'^evaluation/update_classroom_c5/(?P<pk>[\w.@+-]+)/$',
        view=views.Update_Class_c5.as_view(),
        name='update_classroom_c5'
    ),
    re_path(
        r'^evaluation/update_classroom_c6/(?P<pk>[\w.@+-]+)/$',
        view=views.Update_Class_c6.as_view(),
        name='update_classroom_c6'
    ),
    re_path(
        r'^evaluation/update_classroom_c7/(?P<pk>[\w.@+-]+)/$',
        view=views.Update_Class_c7.as_view(),
        name='update_classroom_c7'
    ),
    re_path(
        r'^evaluation/update_classroom_c8/(?P<pk>[\w.@+-]+)/$',
        view=views.Update_Class_c8.as_view(),
        name='update_classroom_c8'
    ),
    re_path(
        r'^evaluation/update_classroom_c9/(?P<pk>[\w.@+-]+)/$',
        view=views.Update_Class_c9.as_view(),
        name='update_classroom_c9'
    ),
    re_path(
        r'^evaluation/update_classroom_cprep/(?P<pk>[\w.@+-]+)/$',
        view=views.Update_Class_cprep.as_view(),
        name='update_classroom_cprep'
    ),
    re_path(
        r'^school-list/$',
        view=views.SchoolListView.as_view(),
        name='school_list'
    ),
    re_path(
        r'^school-add/$',
        view=views.SchoolAddView.as_view(),
        name='school_add'
    ),
    re_path(
        r'^school-edit/(?P<pk>[\w.@+-]+)/$',
        view=views.SchoolEditView.as_view(),
        name='school_edit'
    ),
    re_path(
        r'^club-list/(?P<school_id>[\w.@+-]+)/$',
        view=views.ClubListView.as_view(),
        name='club_list'
    ),
    re_path(
        r'^club-add/(?P<school_id>[\w.@+-]+)/$',
        view=views.ClubFormView.as_view(),
        name='club_add'
    ),
    re_path(
        r'^club-edit/(?P<school_id>[\w.@+-]+)/(?P<pk>[\w.@+-]+)/$',
        view=views.ClubFormView.as_view(),
        name='club_edit'
    ),
    re_path(
        r'^club-delete/(?P<pk>[\w.@+-]+)/$',
        view=views.club_delete,
        name='club_delete'
    ),
    re_path(
        r'^meeting-list/(?P<school_id>[\w.@+-]+)/$',
        view=views.MeetingListView.as_view(),
        name='meeting_list'
    ),
    re_path(
        r'^meeting-add/(?P<school_id>[\w.@+-]+)/$',
        view=views.MeetingFormView.as_view(),
        name='meeting_add'
    ),
    re_path(
        r'^meeting-edit/(?P<school_id>[\w.@+-]+)/(?P<pk>[\w.@+-]+)/$',
        view=views.MeetingFormView.as_view(),
        name='meeting_edit'
    ),
    re_path(
        r'^meeting-delete/(?P<pk>[\w.@+-]+)/$',
        view=views.meeting_delete,
        name='meeting_delete'
    ),
    re_path(
        r'^community-initiative-list/(?P<school_id>[\w.@+-]+)/$',
        view=views.CommunityInitiativeListView.as_view(),
        name='community_initiative_list'
    ),
    re_path(
        r'^community-initiative-add/(?P<school_id>[\w.@+-]+)/$',
        view=views.CommunityInitiativeFormView.as_view(),
        name='community_initiative_add'
    ),
    re_path(
        r'^community-initiative-edit/(?P<school_id>[\w.@+-]+)/(?P<pk>[\w.@+-]+)/$',
        view=views.CommunityInitiativeFormView.as_view(),
        name='community_initiative_edit'
    ),
    re_path(
        r'^community-initiative-delete/(?P<pk>[\w.@+-]+)/$',
        view=views.community_initiative_delete,
        name='community_initiative_delete'
    ),
    re_path(
        r'^health-visit-list/(?P<school_id>[\w.@+-]+)/$',
        view=views.HealthVisitListView.as_view(),
        name='health_visit_list'
    ),
    re_path(
        r'^health-visit-add/(?P<school_id>[\w.@+-]+)/$',
        view=views.HealthVisitFormView.as_view(),
        name='health_visit_add'
    ),
    re_path(
        r'^health-visit-edit/(?P<school_id>[\w.@+-]+)/(?P<pk>[\w.@+-]+)/$',
        view=views.HealthVisitFormView.as_view(),
        name='health_visit_edit'
    ),
    re_path(
        r'^health-visit-delete/(?P<pk>[\w.@+-]+)/$',
        view=views.health_visit_delete,
        name='health_visit_delete'
    ),
    re_path(
        'load-districts/$',
        views.load_districts,
        name='load_districts'
    ),
    re_path(
        'load-cadasters/$',
        views.load_cadasters,
        name='load_cadasters'
    ),
    re_path(
        'load-schools/$',
        views.load_schools,
        name='load_schools'
    ),
    re_path(
        r'^school-export-background/$',
        view=views.export_school_background,
        name='school_export_background'
    ),
]
