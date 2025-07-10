from __future__ import unicode_literals, absolute_import, division

from django.utils.translation import gettext as _
from django import forms
from django.urls import reverse
from django.contrib import messages

from crispy_forms.helper import FormHelper

from crispy_forms.bootstrap import (
    FormActions,
    InlineCheckboxes
)
from crispy_forms.layout import Layout, Fieldset, Button, Submit, Div, Field, HTML, Reset
from dal import autocomplete

from student_registration.students.models import (
    Nationality,
    IDType,
)

from student_registration.locations.models import Center
from student_registration.clm.models import Disability, EducationalLevel
from student_registration.child.models import Child
from .models import (
    Registration,
    Referral,
    YES_NO
)
from student_registration.schools.models import (
    School
)
from .utils import generate_services, generate_education_history, regenerate_services
from .serializers import MainSerializer
from student_registration.mscc.templatetags.simple_tags import get_service, get_education_service
import datetime

DAYS = list(((str(x), x) for x in range(1, 32)))
DAYS.insert(0, ('', '---------'))


class MainForm(forms.ModelForm):
    # YEARS = list(((str(x), x) for x in range(Child.CURRENT_YEAR - 20, Child.CURRENT_YEAR + 1)))
    YEARS = list(((str(x), x) for x in range(1990, Child.CURRENT_YEAR + 1)))
    YEARS.insert(0, ('', '---------'))

    # center = forms.ModelChoiceField(
    #     queryset=Center.objects.all(), widget=forms.Select,
    #     label=_('Center'),
    #     empty_label='-------',
    #     required=True, to_field_name='id',
    # )
    child_first_name = forms.CharField(
        label=_("Child\'s First Name"),
        widget=forms.TextInput, required=True
    )
    child_father_name = forms.CharField(
        label=_("Child\'s Father Name"),
        widget=forms.TextInput, required=True
    )
    child_last_name = forms.CharField(
        label=_("Child\'s Family Name"),
        widget=forms.TextInput, required=True
    )
    child_mother_fullname = forms.CharField(
        label=_("Mother Full Name"),
        widget=forms.TextInput, required=True
    )
    child_gender = forms.ChoiceField(
        label=_("Child\'s Gender"),
        widget=forms.Select, required=True,
        choices=Child.GENDER
    )
    child_nationality = forms.ModelChoiceField(
        label=_("Child\'s Nationality"),
        queryset=Nationality.objects.all(), widget=forms.Select,
        required=True, to_field_name='id',
    )
    child_nationality_other = forms.CharField(
        label=_('If Other, Please specify'),
        widget=forms.TextInput, required=False
    )
    child_birthday_year = forms.ChoiceField(
        label=_("Birthday year"),
        widget=forms.Select, required=True,
        choices=YEARS
    )
    child_birthday_month = forms.ChoiceField(
        label=_("Birthday month"),
        widget=forms.Select, required=True,
        choices=Child.MONTHS
    )
    child_birthday_day = forms.ChoiceField(
        label=_("Birthday day"),
        widget=forms.Select, required=True,
        choices=DAYS
    )
    main_caregiver_nationality = forms.ModelChoiceField(
        queryset=Nationality.objects.all(), widget=forms.Select,
        label=_('Caregiver Nationality'),
        required=False, to_field_name='id',
    )
    main_caregiver_nationality_other = forms.CharField(
        label=_('If Other, Please specify'),
        widget=forms.TextInput, required=False
    )
    child_p_code = forms.CharField(
        label=_('Insert Pcode if the child lives in Internal Settlement/Camp'),
        widget=forms.TextInput, required=False,
        max_length=50
    )
    child_address = forms.CharField(
        label=_("Registered child Home Address (Village, Street, Building/Camp, Cadaster)"),
        widget=forms.TextInput, required=False
    )
    child_living_arrangement = forms.ChoiceField(
        label=_("Living Arrangement"),
        widget=forms.Select, required=False,
        choices=Child.LIVING_ARRANGEMENT
    )
    child_disability = forms.ModelChoiceField(
        label=_("Does the child have any disability or special need?"),
        queryset=Disability.objects.all(), widget=forms.Select,
        required=True, to_field_name='id',
    )
    child_marital_status = forms.ChoiceField(
        label=_('Child\'s Marital Status '),
        widget=forms.Select, required=True,
        choices=Child.MARITAL_STATUS,
    )
    child_have_children = forms.ChoiceField(
        label=_("Does the child have children"),
        widget=forms.Select, required=True,
        choices=Child.HAVE_CHILDREN,
    )
    child_children_number = forms.IntegerField(
        label=_('If yes, How many?'),
        widget=forms.NumberInput(attrs=({'maxlength': 4})),
        required=False,
        initial=0,
        min_value=0
    )
    child_have_sibling = forms.ChoiceField(
        label=_("Does the child have siblings?"),
        widget=forms.Select, required=True,
        choices=Child.YES_NO,
    )
    child_siblings_have_disability = forms.ChoiceField(
        label=_("Does any of the siblings have a disability?"),
        widget=forms.Select, required=False,
        choices=Child.YES_NO,
    )
    child_mother_pregnant_expecting = forms.ChoiceField(
        label=_("Is the mother pregnant or expecting?"),
        widget=forms.Select, required=True,
        choices=Child.YES_NO,
    )
    child_fe_unique_id = forms.ChoiceField(
        label=_('Formal Education unique student ID'),
        widget=forms.TextInput, required=False,
    )
    partner_unique_number = forms.CharField(
        label=_('Partner unique child number'),
        widget=forms.TextInput, required=False
    )
    source_of_identification = forms.ChoiceField(
        label=_("Source of referral of the child to Makani"),
        widget=forms.Select,
        required=True,
        choices=Registration.IDENTIFICATION_SOURCE,
        initial=''
    )
    source_of_identification_specify = forms.CharField(
        label=_('If Other, Please specify'),
        widget=forms.TextInput, required=False
    )
    cash_support_programmes = forms.MultipleChoiceField(
        label=_('Cash support programmes that the child is already benefiting from'),
        choices=Registration.CASH_SUPPORT_PROGRAMMES,
        widget=forms.CheckboxSelectMultiple,
        required=False
    )
    # mscc_packages = forms.MultipleChoiceField(
    #     label=_('Packages received/to be provided to child under Makani'),
    #     choices=Registration.MSCC_PACKAGES,
    #     widget=forms.CheckboxSelectMultiple,
    #     required=False
    # )
    father_educational_level = forms.ModelChoiceField(
        queryset=EducationalLevel.objects.all(), widget=forms.Select,
        label=_('What is the father\'s educational level?'),
        required=False, to_field_name='id',
    )
    mother_educational_level = forms.ModelChoiceField(
        queryset=EducationalLevel.objects.all(), widget=forms.Select,
        label=_('What is the mother\'s educational level?'),
        required=False, to_field_name='id',
    )
    first_phone_owner = forms.ChoiceField(
        label=_("Who will be answering the phone?"),
        widget=forms.Select,
        required=False,
        choices=Child.PHONE_OWNER,
        initial=''
    )
    first_phone_number = forms.RegexField(
        regex=r'^(((03|70|71|76|78|79|81|86)-\d{6})|(963 \d{2} \d{3} \d{4}))$',
        widget=forms.TextInput(attrs={'placeholder': 'Format: XX-XXXXXX or 963 XX XXX XXXX'}),
        required=False,
        label=_('Primary phone number')
    )
    first_phone_number_confirm = forms.RegexField(
        regex=r'^(((03|70|71|76|78|79|81|86)-\d{6})|(963 \d{2} \d{3} \d{4}))$',
        widget=forms.TextInput(attrs={'placeholder': 'Format: XX-XXXXXX or 963 XX XXX XXXX'}),
        required=False,
        label=_('Confirm primary phone number')
    )
    second_phone_owner = forms.ChoiceField(
        label=_("Who will be answering the phone?"),
        widget=forms.Select,
        required=False,
        choices=Child.PHONE_OWNER,
        initial=''
    )
    second_phone_number = forms.RegexField(
        regex=r'^(((03|70|71|76|78|79|81|86)-\d{6})|(963 \d{2} \d{3} \d{4}))$',
        widget=forms.TextInput(attrs={'placeholder': 'Format: XX-XXXXXX or 963 XX XXX XXXX'}),
        required=False,
        label=_('Secondary phone number')
    )
    second_phone_number_confirm = forms.RegexField(
        regex=r'^(((03|70|71|76|78|79|81|86)-\d{6})|(963 \d{2} \d{3} \d{4}))$',
        widget=forms.TextInput(attrs={'placeholder': 'Format: XX-XXXXXX or 963 XX XXX XXXX'}),
        required=False,
        label=_('Confirm secondary phone number')
    )
    main_caregiver = forms.ChoiceField(
        label=_("Who is the Child\'s primary caregiver?"),
        widget=forms.Select, required=False,
        choices=Child.MAIN_CAREGIVER
    )
    main_caregiver_other = forms.CharField(
        label=_('If Other, Please specify'),
        widget=forms.TextInput, required=False
    )
    children_number_under18 = forms.IntegerField(
        label=_('Number of children under 18'),
        widget=forms.NumberInput(attrs=({'maxlength': 4})),
        required=False,
        initial=0,
        min_value=0
    )
    caregiver_first_name = forms.CharField(
        label=_("Caregiver First Name"),
        widget=forms.TextInput, required=False
    )
    caregiver_middle_name = forms.CharField(
        label=_("Caregiver Middle Name"),
        widget=forms.TextInput, required=False
    )
    caregiver_last_name = forms.CharField(
        label=_("Caregiver Last Name"),
        widget=forms.TextInput, required=False
    )
    caregiver_mother_name = forms.CharField(
        label=_("Caregiver Mother Full Name"),
        widget=forms.TextInput, required=False
    )
    have_labour = forms.ChoiceField(
        label=_('Does the child participate in work?'),
        widget=forms.Select, required=False,
        choices=Registration.HAVE_LABOUR,
    )
    labour_type = forms.ChoiceField(
        label=_('What is the type of work?'),
        widget=forms.Select, required=False,
        choices=Registration.LABOURS
    )
    labour_type_specify = forms.CharField(
        label=_('Please specify (hotel, restaurant, transport, '
                'personal services such as cleaning, hair care, cooking and childcare)'),
        widget=forms.TextInput, required=False
    )
    labour_hours = forms.IntegerField(
        label=_('How many hours does this child work in a week?'),
        widget=forms.NumberInput(attrs=({'maxlength': 4})),
        required=False,
        initial=0,
        min_value=0
    )
    labour_weekly_income = forms.ChoiceField(
        label=_('How much does the child get paid per week?'),
        widget=forms.Select,
        choices=Registration.LABOUR_INCOME,
        initial='',
        required=False
    )
    labour_condition=forms.MultipleChoiceField(
        label=_('What is the work condition that the child is exposed to?'),
        choices=Registration.LABOUR_CONDITION,
        widget=forms.CheckboxSelectMultiple,
        required=False
    )
    id_type = forms.ModelChoiceField(
        queryset=IDType.objects.filter(active =True),
        widget=forms.Select,
        label=_('ID type of the caregiver'),
        required=False, to_field_name='id'
    )
    case_number = forms.RegexField(
        regex=r'^((245)|(380)|(568)|(705)|(781)|(909)|(947)|(954)|(781)|(LEB)|(leb)|(LB1)|(LB2)|(lb2)|(LBE)|(lbe)|(b6a)|(B6A))-[0-9]{2}[C-](?:\d{5}|\d{6})$',
        widget=forms.TextInput(attrs={'placeholder': 'Format: XXX-XXCXXXXX or XXX-XX-XXXXXX'}),
        required=False,
        label=_('UNHCR Case Number')
    )
    case_number_confirm = forms.RegexField(
        regex=r'^((245)|(380)|(568)|(705)|(781)|(909)|(947)|(954)|(781)|(LEB)|(leb)|(LB1)|(LB2)|(lb2)|(LBE)|(lbe)|(b6a)|(B6A))-[0-9]{2}[C-](?:\d{5}|\d{6})$',
        widget=forms.TextInput(attrs={'placeholder': 'Format: XXX-XXCXXXXX or XXX-XX-XXXXXX'}),
        required=False,
        label=_('Confirm UNHCR Case Number')
    )
    parent_individual_case_number = forms.RegexField(
        regex=r'^((245)|(380)|(568)|(705)|(781)|(909)|(947)|(954)|(781)|(LEB)|(leb)|(LB1)|(LB2)|(lb2)|(LBE)|(lbe)|(b6a)|(B6A))-[0-9]{8}$',
        widget=forms.TextInput(attrs={'placeholder': 'Format: XXX-XXXXXXXX'}),
        required=False,
        label=_(
            'Cargiver Individual ID from the certificate (Optional, in case not listed in the certificate)')
    )
    parent_individual_case_number_confirm = forms.RegexField(
        regex=r'^((245)|(380)|(568)|(705)|(781)|(909)|(947)|(954)|(781)|(LEB)|(leb)|(LB1)|(LB2)|(lb2)|(LBE)|(lbe)|(b6a)|(B6A))-[0-9]{8}$',
        widget=forms.TextInput(attrs={'placeholder': 'Format: XXX-XXXXXXXX'}),
        required=False,
        label=_(
            'Confirm Cargiver Individual ID from the certificate (Optional, in case not listed in the certificate)')
    )
    individual_case_number = forms.RegexField(
        regex=r'^((245)|(380)|(568)|(705)|(781)|(909)|(947)|(954)|(781)|(LEB)|(leb)|(LB1)|(LB2)|(lb2)|(LBE)|(lbe)|(b6a)|(B6A))-[0-9]{8}$',
        widget=forms.TextInput(attrs={'placeholder': 'Format: XXX-XXXXXXXX'}),
        required=False,
        label=_(
            'Individual ID of the Child from the certificate (Optional, in case not listed in the certificate)')
    )
    individual_case_number_confirm = forms.RegexField(
        regex=r'^((245)|(380)|(568)|(705)|(781)|(909)|(947)|(954)|(781)|(LEB)|(leb)|(LB1)|(LB2)|(lb2)|(LBE)|(lbe)|(b6a)|(B6A))-[0-9]{8}$',
        widget=forms.TextInput(attrs={'placeholder': 'Format: XXX-XXXXXXXX'}),
        required=False,
        label=_(
            'Confirm Individual ID of the Child from the certificate (Optional, in case not listed in the certificate)')
    )
    recorded_number = forms.RegexField(
        regex=r'^((245)|(380)|(568)|(705)|(781)|(909)|(947)|(954)|(781)|(LEB)|(leb)|(LB1)|(LB2)|(lb2)|(LBE)|(lbe)|(b6a)|(B6A))-[0-9]{2}[C-](?:\d{5}|\d{6})$|^LB-\d{3}-\d{6}|\d{7}$|^86A-\d{2}-\d{5}$',
        widget=forms.TextInput(attrs={'placeholder': 'Format: LEB-XXCXXXXX or LB-XXX-XXXXXX'}),
        required=False,
        label=_('UNHCR Barcode number (Shifra number)')
    )
    recorded_number_confirm = forms.RegexField(
        regex=r'^((245)|(380)|(568)|(705)|(781)|(909)|(947)|(954)|(781)|(LEB)|(leb)|(LB1)|(LB2)|(lb2)|(LBE)|(lbe)|(b6a)|(B6A))-[0-9]{2}[C-](?:\d{5}|\d{6})$|^LB-\d{3}-\d{6}|\d{7}$|^86A-\d{2}-\d{5}$',
        widget=forms.TextInput(attrs={'placeholder': 'Format: LEB-XXCXXXXX or LB-XXX-XXXXXX'}),
        required=False,
        label=_('Confirm UNHCR Barcode number (Shifra number)')
    )
    national_number = forms.RegexField(
        regex=r'^\d{12}$',
        widget=forms.TextInput(attrs={'placeholder': 'Format: XXXXXXXXXXXX'}),
        required=False,
        label=_('Lebanese ID number of the child (Optional)')
    )
    national_number_confirm = forms.RegexField(
        regex=r'^\d{12}$',
        widget=forms.TextInput(attrs={'placeholder': 'Format: XXXXXXXXXXXX'}),
        required=False,
        label=_('Confirm Lebanese ID number of the child (optional)')
    )
    parent_extract_record = forms.CharField(
        label=_('Lebanese Extract of Record'),
        widget=forms.TextInput, required=False
    )

    parent_extract_record_confirm = forms.CharField(
        label=_('Confirm Lebanese Extract of Record'),
        widget=forms.TextInput, required=False
    )
    syrian_national_number = forms.RegexField(
        regex=r'^\d{11}$',
        required=False,
        label=_('National ID number of the child (Optional)')
    )
    syrian_national_number_confirm = forms.RegexField(
        regex=r'^\d{11}$',
        required=False,
        label=_('Confirm National ID number of the child (Optional)')
    )
    sop_national_number = forms.CharField(
        required=False,
        label=_('Palestinian ID number of the child (Optional)')
    )
    sop_national_number_confirm = forms.CharField(
        required=False,
        label=_('Confirm Palestinian ID number of the child (optional)')
    )
    parent_national_number = forms.RegexField(
        regex=r'^\d{12}$',
        widget=forms.TextInput(attrs={'placeholder': 'Format: XXXXXXXXXXXX'}),
        required=False,
        label=_('Lebanese ID number of the Cargiver')
    )
    parent_national_number_confirm = forms.RegexField(
        regex=r'^\d{12}$',
        widget=forms.TextInput(attrs={'placeholder': 'Format: XXXXXXXXXXXX'}),
        required=False,
        label=_('Confirm Lebanese ID number of the Cargiver')
    )
    parent_syrian_national_number = forms.RegexField(
        regex=r'^\d{11}$',
        required=False,
        label=_('National ID number of the Cargiver (Mandatory)')
    )
    parent_syrian_national_number_confirm = forms.RegexField(
        regex=r'^\d{11}$',
        required=False,
        label=_('Confirm National ID number of the Cargiver (Mandatory)')
    )
    parent_sop_national_number = forms.CharField(
        # regex=r'^\d{11}$',
        required=False,
        label=_('Palestinian ID number of the Cargiver (Mandatory)')
    )
    parent_sop_national_number_confirm = forms.CharField(
        # regex=r'^\d{11}$',
        required=False,
        label=_('Confirm Palestinian ID number of the Cargiver (Mandatory)')
    )

    parent_other_number = forms.CharField(
        required=False,
        label=_('ID number of the Cargiver (Mandatory)')
    )
    parent_other_number_confirm = forms.CharField(
        required=False,
        label=_('Confirm ID number of the Cargiver (Mandatory)')
    )
    other_number = forms.CharField(
        required=False,
        label=_(' ID number of the child (Optional)')
    )
    other_number_confirm = forms.CharField(
        required=False,
        label=_('Confirm ID number of the child (optional)')
    )
    child_id = forms.CharField(widget=forms.HiddenInput, required=False)
    registration_id = forms.CharField(widget=forms.HiddenInput, required=False)
    child_outreach = forms.IntegerField(widget=forms.HiddenInput, required=False)
    student_old = forms.IntegerField(widget=forms.HiddenInput, required=False)
    partner_name = forms.CharField(widget=forms.HiddenInput, required=False)
    type = forms.CharField(widget=forms.HiddenInput, required=False)

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(MainForm, self).__init__(*args, **kwargs)

        display_registry = ''
        instance = kwargs['instance'] if 'instance' in kwargs else ''
        form_action = reverse('mscc:child_add')
        if instance:
            display_registry = ' d-none'
            form_action = reverse('mscc:child_edit', kwargs={'pk': instance.id})

        self.helper = FormHelper()
        self.helper.form_show_labels = True
        self.helper.form_action = form_action

    def clean(self):
        cleaned_data = super(MainForm, self).clean()

        child_p_code = cleaned_data.get("child_p_code")
        if child_p_code and len(child_p_code) > 50:
            self.add_error('child_p_code', _('P-Code must not exceed 50 characters.'))

        # check if date is valid
        year = 0
        month = 0
        day = 0
        if cleaned_data.get("child_birthday_year"):
            year = int(cleaned_data.get("child_birthday_year"))
        if cleaned_data.get("child_birthday_month"):
            month = int(cleaned_data.get("child_birthday_month"))
        if cleaned_data.get("child_birthday_day"):
            day = int(cleaned_data.get("child_birthday_day"))

        try:
            datetime.datetime(year, month, day)
        except ValueError:
            self.add_error('child_birthday_year', 'The date is not valid.')

        child_nationality = cleaned_data.get("child_nationality")
        child_nationality_other = cleaned_data.get("child_nationality_other")
        if child_nationality and child_nationality.id == 6 and not child_nationality_other:
            self.add_error('child_nationality_other', 'This field is required')

        child_have_children = cleaned_data.get("child_have_children")
        child_children_number = cleaned_data.get("child_children_number")
        if child_have_children == "Yes" and not child_children_number:
            self.add_error('child_children_number', 'This field is required')

        child_have_sibling = cleaned_data.get("child_have_sibling")
        child_siblings_have_disability = cleaned_data.get("child_siblings_have_disability")
        if child_have_sibling == "Yes" and not child_siblings_have_disability:
            self.add_error('child_siblings_have_disability', 'This field is required')

        source_of_identification = cleaned_data.get("source_of_identification")
        source_of_identification_specify = cleaned_data.get("source_of_identification_specify")
        if source_of_identification == 'Other Sources' and not source_of_identification_specify:
            self.add_error('source_of_identification_specify', 'This field is required')

        package_type = cleaned_data.get("type")
        if package_type == 'Core-Package':

            father_educational_level = cleaned_data.get("father_educational_level")
            mother_educational_level = cleaned_data.get("mother_educational_level")
            if not father_educational_level:
                self.add_error('father_educational_level', 'This field is required')
            if not mother_educational_level:
                self.add_error('mother_educational_level', 'This field is required')

            first_phone_owner = cleaned_data.get("first_phone_owner")
            first_phone_number = cleaned_data.get("first_phone_number")
            first_phone_number_confirm = cleaned_data.get("first_phone_number_confirm")
            second_phone_number = cleaned_data.get("second_phone_number")
            second_phone_number_confirm = cleaned_data.get("second_phone_number_confirm")
            if not first_phone_owner:
                self.add_error('first_phone_owner', 'This field is required')
            if first_phone_number != first_phone_number_confirm:
                msg = "The phone numbers are not matched"
                self.add_error('first_phone_number_confirm', msg)
            if second_phone_number != second_phone_number_confirm:
                msg = "The phone numbers are not matched"
                self.add_error('second_phone_number_confirm', msg)

            main_caregiver = cleaned_data.get("main_caregiver")
            main_caregiver_other = cleaned_data.get("main_caregiver_other")

            if not main_caregiver:
                self.add_error('main_caregiver', 'This field is required')
            if main_caregiver == 'Other' and not main_caregiver_other:
                self.add_error('main_caregiver_other', 'This field is required')


            children_number_under18 = cleaned_data.get("children_number_under18")
            if not children_number_under18:
                self.add_error('children_number_under18', 'This field is required')



            have_labour = cleaned_data.get("have_labour")
            labour_type = cleaned_data.get("labour_type")
            labour_type_specify = cleaned_data.get("labour_type_specify")
            labour_hours = cleaned_data.get("labour_hours")
            labour_weekly_income = cleaned_data.get("labour_weekly_income")
            labour_condition = cleaned_data.get("labour_condition")
            if not have_labour:
                self.add_error('have_labour', 'This field is required')
            if have_labour != 'No':
                if not labour_type:
                    self.add_error('labour_type', 'This field is required')
                elif labour_type == 'Other services' and not labour_type_specify:
                    self.add_error('labour_type_specify', 'This field is required')
                if not labour_hours:
                    self.add_error('labour_hours', 'This field is required')
                if not labour_weekly_income:
                    self.add_error('labour_weekly_income', 'This field is required')
                if not labour_condition:
                    self.add_error('labour_condition', 'This field is required')

            id_type = cleaned_data.get("id_type")
            case_number = cleaned_data.get("case_number")
            case_number_confirm = cleaned_data.get("case_number_confirm")
            parent_individual_case_number = cleaned_data.get("parent_individual_case_number")
            parent_individual_case_number_confirm = cleaned_data.get("parent_individual_case_number_confirm")
            individual_case_number = cleaned_data.get("individual_case_number")
            individual_case_number_confirm = cleaned_data.get("individual_case_number_confirm")

            # UNHCR Registered

            if id_type and id_type.id == 1:
                if not case_number:
                    self.add_error('case_number', 'This field is required')
                elif case_number != case_number_confirm:
                    msg = "The case numbers are not matched"
                    self.add_error('case_number_confirm', msg)

                if parent_individual_case_number != parent_individual_case_number_confirm:
                    msg = "The individual case numbers are not matched"
                    self.add_error('parent_individual_case_number_confirm', msg)

                if individual_case_number != individual_case_number_confirm:
                    msg = "The individual case numbers are not matched"
                    self.add_error('individual_case_number_confirm', msg)

            recorded_number = cleaned_data.get("recorded_number")
            recorded_number_confirm = cleaned_data.get("recorded_number_confirm")

            # UNHCR Recorded
            if id_type and id_type.id == 2:
                if not recorded_number:
                    self.add_error('recorded_number', 'This field is required')
                elif recorded_number != recorded_number_confirm:
                    msg = "The recorded numbers are not matched"
                    self.add_error('recorded_number_confirm', msg)

            parent_syrian_national_number = cleaned_data.get("parent_syrian_national_number")
            parent_syrian_national_number_confirm = cleaned_data.get("parent_syrian_national_number_confirm")
            syrian_national_number = cleaned_data.get("syrian_national_number")
            syrian_national_number_confirm = cleaned_data.get("syrian_national_number_confirm")

            # Syrian national ID
            if id_type and id_type.id == 3:
                if not parent_syrian_national_number:
                    self.add_error('parent_syrian_national_number', 'This field is required')
                elif parent_syrian_national_number and not len(parent_syrian_national_number) == 11:
                    msg = "Please enter a valid number (11 digits)"
                    self.add_error('parent_syrian_national_number', msg)

                if not parent_syrian_national_number_confirm:
                    self.add_error('parent_syrian_national_number_confirm', 'This field is required')
                elif parent_syrian_national_number_confirm and not len(parent_syrian_national_number_confirm) == 11:
                    msg = "Please enter a valid number (11 digits)"
                    self.add_error('parent_syrian_national_number_confirm', msg)

                if parent_syrian_national_number != parent_syrian_national_number_confirm:
                    msg = "The national numbers are not matched"
                    self.add_error('parent_syrian_national_number_confirm', msg)

                if syrian_national_number != syrian_national_number_confirm:
                    msg = "The national numbers are not matched"
                    self.add_error('syrian_national_number_confirm', msg)

            parent_sop_national_number = cleaned_data.get("parent_sop_national_number")
            parent_sop_national_number_confirm = cleaned_data.get("parent_sop_national_number_confirm")
            sop_national_number = cleaned_data.get("sop_national_number")
            sop_national_number_confirm = cleaned_data.get("sop_national_number_confirm")

            # Palestinian national ID
            if id_type and id_type.id == 4:
                if not parent_sop_national_number:
                    self.add_error('parent_sop_national_number', 'This field is required')

                if not parent_sop_national_number_confirm:
                    self.add_error('parent_sop_national_number_confirm', 'This field is required')

                if parent_sop_national_number != parent_sop_national_number_confirm:
                    msg = "The national numbers are not matched"
                    self.add_error('parent_sop_national_number_confirm', msg)

                if sop_national_number != sop_national_number_confirm:
                    msg = "The national numbers are not matched"
                    self.add_error('sop_national_number_confirm', msg)

            parent_national_number = cleaned_data.get("parent_national_number")
            parent_national_number_confirm = cleaned_data.get("parent_national_number_confirm")
            national_number = cleaned_data.get("national_number")
            national_number_confirm = cleaned_data.get("national_number_confirm")

            # Lebanese national ID
            if id_type and id_type.id == 5:
                if parent_national_number and not len(parent_national_number) == 12:
                    msg = "Please enter a valid number (12 digits)"
                    self.add_error('parent_national_number', msg)

                if parent_national_number_confirm and not len(parent_national_number_confirm) == 12:
                    msg = "Please enter a valid number (12 digits)"
                    self.add_error('parent_national_number_confirm', msg)

                if parent_national_number != parent_national_number_confirm:
                    msg = "The national numbers are not matched"
                    self.add_error('parent_national_number_confirm', msg)

                if national_number != national_number_confirm:
                    msg = "The national numbers are not matched"
                    self.add_error('national_number_confirm', msg)

            parent_other_number = cleaned_data.get("parent_other_number")
            parent_other_number_confirm = cleaned_data.get("parent_other_number_confirm")
            other_number = cleaned_data.get("other_number")
            other_number_confirm = cleaned_data.get("other_number_confirm")

            parent_extract_record = cleaned_data.get("parent_extract_record")
            parent_extract_record_confirm = cleaned_data.get("parent_extract_record_confirm")

            # Other nationality
            if id_type and id_type.id == 6:
                if not parent_other_number:
                    self.add_error('parent_other_number', 'This field is required')

                if not parent_other_number_confirm:
                    self.add_error('parent_other_number_confirm', 'This field is required')

                if parent_other_number != parent_other_number_confirm:
                    msg = "The ID numbers are not matched"
                    self.add_error('parent_other_number_confirm', msg)

                if other_number != other_number_confirm:
                    msg = "The ID numbers are not matched"
                    self.add_error('other_number_confirm', msg)

            if id_type and id_type == 9:
                if parent_extract_record != parent_extract_record_confirm:
                    msg = "The Parent Extract Record are not matched"
                    self.add_error('parent_extract_record_confirm', msg)

            child_living_arrangement = cleaned_data.get("child_living_arrangement")
            if not child_living_arrangement:
                self.add_error('child_living_arrangement', 'This field is required')

            cash_support_programmes = cleaned_data.get("cash_support_programmes")
            if not cash_support_programmes:
                self.add_error('cash_support_programmes', 'This field is required')


    def save(self, request=None, instance=None):

        from student_registration.students.utils import generate_one_unique_id

        if instance:
            serializer = MainSerializer(instance, data=request.POST)
            if serializer.is_valid():
                old_dob_year = instance.child.birthday_year
                old_dob_month = instance.child.birthday_month
                old_dob_age = instance.child_age

                instance = serializer.update(validated_data=serializer.validated_data, instance=instance)

                instance.modified_by = request.user
                instance.save()

                if (old_dob_year != instance.child.birthday_year or
                    old_dob_month != instance.child.birthday_month) and old_dob_age != instance.child_age:
                    regenerate_services(instance.child.age, instance, request.user)

                request.session['instance_id'] = instance.id
                messages.success(request, _('Your data has been sent successfully to the server'))
            else:
                messages.warning(request, serializer.errors)

        else:
            serializer = MainSerializer(data=request.POST)
            if serializer.is_valid():
                instance = serializer.create(validated_data=serializer.validated_data)

                instance.owner = request.user
                instance.modified_by = request.user
                instance.partner = request.user.partner
                instance.center = request.user.center
                if request.POST.get("child_outreach"):
                    instance.child_outreach = request.POST.get("child_outreach")
                if request.POST.get("student_old"):
                    instance.student_old = request.POST.get("student_old")
                instance.save()
                request.session['instance_id'] = instance.id
                generate_services(instance.child.age, instance, request.user)
                generate_education_history(instance.id, instance.child_id, instance.student_old)

                messages.success(request, _('Your data has been sent successfully to the server'))

            else:
                messages.warning(request, serializer.errors)

        if instance:
            instance.child.unicef_id = generate_one_unique_id(
                str(instance.child.pk),
                instance.child.first_name,
                instance.child.father_name,
                instance.child.last_name,
                instance.child.mother_fullname,
                instance.child.birthdate,
                instance.child.nationality_name_en,
                instance.child.gender
            )
            instance.child.save()

        return instance

    class Meta:
        model = Registration
        fields = (
            # 'center',
            'child_outreach',
            'student_old',
            'child_first_name',
            'child_father_name',
            'child_last_name',
            'child_mother_fullname',
            'child_gender',
            'child_nationality',
            'child_nationality_other',
            'child_birthday_year',
            'child_birthday_month',
            'child_birthday_day',
            'main_caregiver_nationality',
            'main_caregiver_nationality_other',
            'child_p_code',
            'child_address',
            'child_living_arrangement',
            'child_disability',
            'child_marital_status',
            'child_have_children',
            'child_children_number',
            'child_have_sibling',
            'child_siblings_have_disability',
            'child_mother_pregnant_expecting',
            'partner_unique_number',
            'source_of_identification',
            'source_of_identification_specify',
            'child_fe_unique_id',
            'cash_support_programmes',
            # 'mscc_packages',
            'father_educational_level',
            'mother_educational_level',
            'first_phone_owner',
            'first_phone_number',
            'first_phone_number_confirm',
            'second_phone_owner',
            'second_phone_number',
            'second_phone_number_confirm',
            'main_caregiver',
            'main_caregiver_other',
            'children_number_under18',
            'caregiver_first_name',
            'caregiver_middle_name',
            'caregiver_last_name',
            'caregiver_mother_name',
            'have_labour',
            'labour_type',
            'labour_type_specify',
            'labour_hours',
            'labour_weekly_income',
            'labour_condition',
            'id_type',
            'case_number',
            'case_number_confirm',
            'parent_individual_case_number',
            'parent_individual_case_number_confirm',
            'individual_case_number',
            'individual_case_number_confirm',
            'parent_extract_record',
            'parent_extract_record_confirm',
            'recorded_number',
            'recorded_number_confirm',
            'parent_national_number',
            'parent_national_number_confirm',
            'national_number',
            'national_number_confirm',
            'parent_syrian_national_number',
            'parent_syrian_national_number_confirm',
            'syrian_national_number',
            'syrian_national_number_confirm',
            'parent_sop_national_number',
            'parent_sop_national_number_confirm',
            'sop_national_number',
            'sop_national_number_confirm',
            'parent_other_number',
            'parent_other_number_confirm',
            'other_number',
            'other_number_confirm',
            'type'
        )


class ReferralForm(forms.ModelForm):

    referred_formal_education = forms.ChoiceField(
        label=_("Was the child referred to formal education (Grade 1)?"),
        widget=forms.Select, required=False,
        choices=YES_NO,
    )
    referred_school = forms.ModelChoiceField(
        queryset=School.objects.all(), widget=forms.Select,
        label=_('Name of the School referred to'),
        empty_label='-------',
        required=False, to_field_name='id',
    )
    receive_needed_material = forms.ChoiceField(
        label=_("Did the child receive all needed materials and resources (Stationery, Books, Learning bundle)?"),
        widget=forms.Select, required=True,
        choices=YES_NO,
    )
    referred_service = forms.ChoiceField(
        label=_("Was the child referred to a service?"),
        widget=forms.Select, required=True,
        choices=Referral.REFERRED_SERVICE,
    )
    referred_service_other = forms.CharField(
        label=_('Please specify'),
        widget=forms.TextInput, required=False
    )
    recommended_learning_path = forms.ChoiceField(
        label=_("Based on the overall score, what is the recommended learning path/outcome?"),
        widget=forms.Select, required=True,
        choices=Referral.LEARNING_PATH,
    )
    dropout_date = forms.DateField(
        label=_("Please Specify dropout date"),
        required=False
    )
    is_cbece = forms.CharField(required=False)
    registration_id = forms.CharField(widget=forms.HiddenInput, required=False)

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        registry = kwargs.pop('registry', None)
        pk = kwargs.pop('pk', None)
        is_cbece = 'Yes' if get_service(registry, 'CB-ECE') else 'No'

        super(ReferralForm, self).__init__(*args, **kwargs)

        form_action = reverse('mscc:referral_add', kwargs={'registry': registry})
        if pk:
            form_action = reverse('mscc:referral_edit',
                                  kwargs={'registry': registry, 'pk': pk})
        if is_cbece == 'Yes':
            self.fields['referred_formal_education'].required = True

        education_program = get_education_service(registry)
        choices = list()
        choices.append(('Transition to Dirasa', _('Transition to Dirasa')))
        choices.append(('Repeat same level in next  school year', _('Repeat same level in next  school year')))
        choices.append(('Progress to FE', _('Progress to FE')))
        choices.append(('Referred to Specialized Education', _('Referred to Specialized Education')))
        choices.append(('Referred to TVET', _('Referred to TVET')))
        choices.append(('Drop out', _('Drop out')))
        choices.append(('Referred to YBLN', _('Referred to YBLN')))
        choices.append(('Progress to  Higher Level  in next school year', _('Progress to  Higher Level  in next school year')))

        if education_program == "CBECE Level 2":
            choices.append(('Referred to CBECE Higher Level in next school year',
                            _('Referred to CBECE Higher Level in next school year')))

        self.fields['recommended_learning_path'].choices = choices

        self.fields['is_cbece'].initial = is_cbece
        self.helper = FormHelper()
        self.helper.form_show_labels = True
        self.helper.form_action = form_action
        if is_cbece == 'Yes':
            self.helper.layout = Layout(
                Div(
                    Div(
                        Div('is_cbece', css_class='col-md-6'),
                        css_class='row card-body d-none'
                    ),
                    Div(
                        HTML('<span class="badge-form badge-pill">1</span>'),
                        Div('referred_formal_education', css_class='col-md-5'),
                        Div('referred_school', css_class='col-md-6'),
                        css_class='row card-body'
                    ),
                    Div(
                        HTML('<span class="badge-form badge-pill">2</span>'),
                        Div('receive_needed_material', css_class='col-md-11'),
                        css_class='row card-body'
                    ),
                    Div(
                        HTML('<span class="badge-form badge-pill">3</span>'),
                        Div('referred_service', css_class='col-md-5'),
                        Div('referred_service_other', css_class='col-md-6'),
                        css_class='row card-body'
                    ),
                    Div(
                        HTML('<span class="badge-form badge-pill">4</span>'),
                        Div('recommended_learning_path', css_class='col-md-5'),
                        Div('dropout_date', css_class='col-md-6'),
                        css_class='row card-body'
                    ),

                    css_id='step-1'
                ),
                FormActions(
                    Submit('save', 'Save',
                           css_class='btn-shadow btn-wide float-right btn-pill mr-3 btn-hover-shine btn btn-success'),
                    Reset('reset', 'Reset',
                          css_class='btn-shadow btn-wide float-right btn-pill mr-3 btn-hover-shine btn btn-warning'),
                ),
        )
        if is_cbece == 'No':
            self.helper.layout = Layout(
                Div(
                    Div(
                        Div('is_cbece', css_class='col-md-6'),
                        css_class='row card-body d-none'
                    ),
                    Div(
                        HTML('<span class="badge-form badge-pill">1</span>'),
                        Div('referred_formal_education', css_class='col-md-5'),
                        Div('referred_school', css_class='col-md-6'),
                        css_class='row card-body d-none'
                    ),
                    Div(
                        HTML('<span class="badge-form badge-pill">1</span>'),
                        Div('receive_needed_material', css_class='col-md-11'),
                        css_class='row card-body'
                    ),
                    Div(
                        HTML('<span class="badge-form badge-pill">2</span>'),
                        Div('referred_service', css_class='col-md-5'),
                        Div('referred_service_other', css_class='col-md-6'),
                        css_class='row card-body'
                    ),
                    Div(
                        HTML('<span class="badge-form badge-pill">3</span>'),
                        Div('recommended_learning_path', css_class='col-md-11'),
                        css_class='row card-body'
                    ),
                    Div(
                        Div('dropout_date', css_class='col-md-5'),
                        css_class='row card-body'
                    ),
                    css_id='step-1'
                ),
                FormActions(
                    Submit('save', 'Save',
                           css_class='btn-shadow btn-wide float-right btn-pill mr-3 btn-hover-shine btn btn-success'),
                    Reset('reset', 'Reset',
                          css_class='btn-shadow btn-wide float-right btn-pill mr-3 btn-hover-shine btn btn-warning'),
                ),
        )

    def save(self, request=None, instance=None, registry=None):
        from datetime import datetime
        validated_data = request.POST

        if not instance:
            instance = Referral.objects.create(registration_id=registry)
        else:
            instance = Referral.objects.get(id=instance)

        instance.referred_formal_education = validated_data.get('referred_formal_education')
        instance.referred_school_id = validated_data.get('referred_school')
        instance.receive_needed_material = validated_data.get('receive_needed_material')
        instance.referred_service = validated_data.get('referred_service')
        instance.referred_service_other = validated_data.get('referred_service_other')
        instance.recommended_learning_path = validated_data.get('recommended_learning_path')
        dropout_date_str = validated_data.get('dropout_date')
        if dropout_date_str:
            dropout_date = datetime.strptime(dropout_date_str, '%Y-%m-%d')
            instance.dropout_date = dropout_date
        instance.save()

        messages.success(request, _('Your data has been sent successfully to the server'))

        return instance

    def clean(self):
        cleaned_data = super(ReferralForm, self).clean()
        is_cbece  = cleaned_data.get("is_cbece")
        referred_formal_education = cleaned_data.get("referred_formal_education")
        referred_school = cleaned_data.get("referred_school")

        if is_cbece and is_cbece == 'Yes':
            if not referred_formal_education:
                self.add_error('referred_formal_education', 'This field is required')

                if referred_formal_education == 'Yes' and not referred_school:
                    self.add_error('referred_school', 'This field is required')

        referred_service = cleaned_data.get("referred_service")
        referred_service_other = cleaned_data.get("referred_service_other")
        if referred_service and referred_service == 'Other' and not referred_service_other:
            self.add_error('referred_service_other', 'This field is required')

        recommended_learning_path = cleaned_data.get("recommended_learning_path")
        dropout_date = cleaned_data.get("dropout_date")
        if recommended_learning_path == 'Drop out' and not dropout_date:
            self.add_error('dropout_date', 'This field is required')

    class Meta:
        model = Referral
        fields = (
            'referred_formal_education',
            'referred_school',
            'receive_needed_material',
            'referred_service',
            'referred_service_other',
            'recommended_learning_path',
            'dropout_date',
        )
