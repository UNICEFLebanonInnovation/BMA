from django.contrib import admin

from import_export import resources, fields
from import_export import fields
from import_export.admin import ImportExportModelAdmin
# from import_export.widgets import *
from .models import Assessment


class AssessmentResource(resources.ModelResource):

    location_p_code = fields.Field()
    location_p_code_name = fields.Field()
    location_district = fields.Field()
    location_cadastral = fields.Field()
    locations_type = fields.Field()
    location_latitude = fields.Field()
    location_longitude = fields.Field()

    class Meta:
        model = Assessment
        fields = (
            '_id',
            'location_p_code',
            'location_p_code_name',
            'location_district',
            'location_cadastral',
            'locations_type',
            'assistance_type',
            'phone_number',
            'phone_owner',
            'location_latitude',
            'location_longitude',
            'first_name',
            'middle_name',
            'family_name',
            'mothers_name',
            'relationship_type',
            'family_count',
            'disabilities',
            'official_id',
            'gender',
            'dob',
            'marital_status',
            'creation_date',
            'completion_date',
            'partner_name',
            'moving_location',
            'new_district',
            'new_cadastral',
            '_0_to_3_months',
            '_3_to_12_months',
            '_1_year_old',
            '_2_years_old',
            '_3_years_old',
            '_4_years_old',
            '_5_years_old',
            '_6_years_old',
            '_7_years_old',
            '_8_years_old',
            '_9_years_old',
            '_10_years_old',
            '_11_years_old',
            '_12_years_old',
            '_13_years_old',
            '_14_years_old',
            'male',
            'female',
            '_3_months_kit',
            '_12_months_kit',
            '_2_years_kit',
            '_3_years_kit',
            '_5_years_kit',
            '_7_years_kit',
            '_9_years_kit',
            '_12_years_kit',
            '_14_years_kit',
            '_3_months_kit_completed',
            '_12_months_kit_completed',
            '_2_years_kit_completed',
            '_3_years_kit_completed',
            '_5_years_kit_completed',
            '_7_years_kit_completed',
            '_9_years_kit_completed',
            '_12_years_kit_completed',
            '_14_years_kit_completed',
        )
        export_order = fields

    def dehydrate_location_p_code(self, obj):
        return obj.location_p_code

    def dehydrate_location_p_code_name(self, obj):
        return obj.location_p_code_name

    def dehydrate_location_district(self, obj):
        return obj.location_district

    def dehydrate_location_cadastral(self, obj):
        return obj.location_cadastral

    def dehydrate_locations_type(self, obj):
        return obj.location_type

    def dehydrate_location_latitude(self, obj):
        return obj.location_latitude

    def dehydrate_location_longitude(self, obj):
        return obj.location_longitude


class AssessmentAdmin(ImportExportModelAdmin):
    resource_class = AssessmentResource
    list_display = (
        '_id',
        'p_code',
        'p_code_name',
        'location_p_code',
        'location_p_code_name',
        'location_district',
        'location_cadastral',
        'locations_type',
        'assistance_type',
        'phone_number',
        'phone_owner',
        'location_latitude',
        'location_longitude',
        'first_name',
        'middle_name',
        'family_name',
        'mothers_name',
        'relationship_type',
        'family_count',
        'disabilities',
        'official_id',
        'gender',
        'dob',
        'marital_status',
        'creation_date',
        'completion_date',
        'partner_name',
        'moving_location',
        'new_district',
        'new_cadastral',
        '_0_to_3_months',
        '_3_to_12_months',
        '_1_year_old',
        '_2_years_old',
        '_3_years_old',
        '_4_years_old',
        '_5_years_old',
        '_6_years_old',
        '_7_years_old',
        '_8_years_old',
        '_9_years_old',
        '_10_years_old',
        '_11_years_old',
        '_12_years_old',
        '_13_years_old',
        '_14_years_old',
        'male',
        'female',
        '_3_months_kit',
        '_12_months_kit',
        '_2_years_kit',
        '_3_years_kit',
        '_5_years_kit',
        '_7_years_kit',
        '_9_years_kit',
        '_12_years_kit',
        '_14_years_kit',
        '_3_months_kit_completed',
        '_12_months_kit_completed',
        '_2_years_kit_completed',
        '_3_years_kit_completed',
        '_5_years_kit_completed',
        '_7_years_kit_completed',
        '_9_years_kit_completed',
        '_12_years_kit_completed',
        '_14_years_kit_completed',
    )
    list_filter = (
        'assistance_type',
        'location_type',
        'partner_name',
        'gender',
        'family_count',
        'marital_status',
    )
    search_fields = (
        'id_type',
    )

    def get_export_formats(self):
        from student_registration.users.utils import get_default_export_formats
        return get_default_export_formats()

    def get_queryset(self, request):
        if request.user.id == 1 or request.user.id == 936:
            return super(AssessmentAdmin, self).get_queryset(request)
        return Assessment.objects.none()


# admin.site.register(Assessment, AssessmentAdmin)

