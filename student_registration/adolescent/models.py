# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import, division
import datetime

from django.db import models
from model_utils import Choices
from model_utils.models import TimeStampedModel
from django.utils.translation import gettext as _

from student_registration.students.models import Nationality, IDType
from student_registration.clm.models import Disability, EducationalLevel
from student_registration.locations.models import Location
from student_registration.students.utils import generate_id, generate_one_unique_id


class Adolescent(TimeStampedModel):

    CURRENT_YEAR = datetime.datetime.now().year
    MONTHS = Choices(
        ('', '---------'),
        ('1', _('January')),
        ('2', _('February')),
        ('3', _('March')),
        ('4', _('April')),
        ('5', _('May')),
        ('6', _('June')),
        ('7', _('July')),
        ('8', _('August')),
        ('9', _('September')),
        ('10', _('October')),
        ('11', _('November')),
        ('12', _('December')),
    )
    YES_NO = Choices(
        ('', '----------'),
        ('Yes', _("Yes")),
        ('No', _("No"))
    )
    GENDER = Choices(
        ('', '----------'),
        ('Male', _('Male')),
        ('Female', _('Female')),
    )
    MAIN_CAREGIVER = Choices(
        ('', '----------'),
        ('Mother', _('Mother')),
        ('Father', _('Father')),
        ('Other', _('Other')),
    )
    first_name = models.CharField(

        max_length=64,
        db_index=True,
        blank=True, null=True,
        verbose_name=_('First name')
    )
    last_name = models.CharField(
        max_length=64,
        db_index=True,
        blank=True, null=True,
        verbose_name=_('Last name')
    )
    father_name = models.CharField(
        max_length=64,
        db_index=True,
        blank=True, null=True,
        verbose_name=_('Father name')
    )
    mother_fullname = models.CharField(
        max_length=64,
        db_index=True,
        blank=True, null=True,
        verbose_name=_('Mother fullname')
    )
    gender = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        choices=GENDER,
        verbose_name=_('Gender')
    )
    nationality = models.ForeignKey(
        Nationality,
        blank=True, null=True,
        related_name='+',
        verbose_name=_('Nationality'),
        on_delete=models.SET_NULL
    )
    nationality_other = models.TextField(
        blank=True, null=True,
        verbose_name=_('Please specify')
    )
    birthday_year = models.CharField(
        max_length=4,
        blank=True,
        null=True,
        default=0,
        choices=((str(x), x) for x in range(1990, 2050)),
        verbose_name=_('Birthday year')
    )
    birthday_month = models.CharField(
        max_length=2,
        blank=True,
        null=True,
        default=0,
        choices=MONTHS,
        verbose_name=_('Birthday month')
    )
    birthday_day = models.CharField(
        max_length=2,
        blank=True,
        null=True,
        default=0,
        choices=((str(x), x) for x in range(1, 32)),
        verbose_name=_('Birthday day')
    )
    governorate = models.ForeignKey(
        Location,
        blank=True, null=True,
        related_name='+',
        verbose_name=_('Governorate'),
        on_delete=models.SET_NULL
    )
    district = models.ForeignKey(
        Location,
        blank=True, null=True,
        related_name='+',
        on_delete=models.SET_NULL,
        verbose_name=_('District')
    )
    cadaster = models.ForeignKey(
        Location,
        blank=True, null=True,
        related_name='+',
        on_delete=models.SET_NULL,
        verbose_name=_('Cadaster')
    )
    address = models.TextField(
        blank=True,
        null=True,
        verbose_name=_('Registered youth Home Address')
    )
    disability = models.ForeignKey(
        Disability,
        blank=True, null=True,
        related_name='+',
        on_delete=models.SET_NULL,
        verbose_name=_('Does the youth have any disability or special need?')
    )
    number = models.CharField(max_length=45, blank=True, null=True)
    unicef_id = models.CharField(max_length=45, blank=True, null=True)
    id_type = models.ForeignKey(
        IDType,
        blank=False, null=True,
        related_name='+',
        on_delete=models.SET_NULL,
        verbose_name=_('Youth ID type')
    )
    case_number = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        verbose_name=_('UNHCR Case number')
    )
    case_number_confirm = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        verbose_name=_('UNHCR Case number confirm')
    )
    parent_individual_case_number = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        verbose_name=_('Parent individual ID')
    )
    parent_individual_case_number_confirm = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        verbose_name=_('Parent individual ID confirm')
    )
    individual_case_number = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        verbose_name=_('Youth individual ID')
    )
    individual_case_number_confirm = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        verbose_name=_('Youth individual ID confirm')
    )
    recorded_number = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        verbose_name=_('UNHCR recorded barcode')
    )
    recorded_number_confirm = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        verbose_name=_('UNHCR recorded barcode confirm')
    )
    parent_national_number = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        verbose_name=_('Parent Lebanese ID number')
    )
    parent_national_number_confirm = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        verbose_name=_('Parent Lebanese ID number')
    )
    national_number = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        verbose_name=_('Youth Lebanese ID number')
    )
    national_number_confirm = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        verbose_name=_('Youth Lebanese ID number')
    )
    parent_extract_record = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        verbose_name=_('Parent Lebanese Extract of Record')
    )
    parent_extract_record_confirm = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        verbose_name=_('Parent Lebanese Extract of Record confirm')
    )
    parent_syrian_national_number = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        verbose_name=_('Parent Syrian ID number ')
    )
    parent_syrian_national_number_confirm = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        verbose_name=_('Parent Syrian ID number confirm')
    )
    syrian_national_number = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        verbose_name=_('Youth Syrian ID number')
    )
    syrian_national_number_confirm = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        verbose_name=_('Youth Syrian ID number confirm')
    )
    parent_sop_national_number = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        verbose_name=_('Parent Palestinian ID number ')
    )
    parent_sop_national_number_confirm = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        verbose_name=_('Parent Palestinian ID number')
    )
    sop_national_number = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        verbose_name=_('Youth Palestinian ID number')
    )
    sop_national_number_confirm = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        verbose_name=_('Youth Palestinian ID number confirm')
    )
    parent_other_number = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        verbose_name=_('ID number of the Caregiver confirm')
    )
    parent_other_number_confirm = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        verbose_name=_('ID number of the Caregiver')
    )
    other_number = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        verbose_name=_('ID number of the youth')
    )
    other_number_confirm = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        verbose_name=_('ID number of the youth confirm')
    )
    unrwa_number = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        verbose_name=_('UNRWA Case number')
    )
    father_educational_level = models.ForeignKey(
        EducationalLevel,
        blank=True, null=True,
        related_name='+',
        on_delete=models.SET_NULL,
        verbose_name=_('What is the father\'s educational level?')
    )
    mother_educational_level = models.ForeignKey(
        EducationalLevel,
        blank=True, null=True,
        related_name='+',
        on_delete=models.SET_NULL,
        verbose_name=_('What is the father\'s educational level?')
    )
    first_phone_number = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        verbose_name=_('Primary phone number')
    )
    first_phone_number_confirm = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        verbose_name=_('Confirm primary phone number')
    )
    second_phone_number = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        verbose_name=_('Secondary phone number if available')
    )
    second_phone_number_confirm = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        verbose_name=_('Confirm Secondary phone number if available')
    )
    main_caregiver = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        choices=MAIN_CAREGIVER,
        verbose_name=_('who is the youth primary caregiver?')
    )
    main_caregiver_other = models.TextField(
        blank=True, null=True,
        verbose_name=_('Please specify')
    )
    caregiver_first_name = models.CharField(
        max_length=500,
        blank=False,
        null=True,
        verbose_name=_('Caregiver First Name')
    )
    caregiver_middle_name = models.CharField(
        max_length=500,
        blank=False,
        null=True,
        verbose_name=_('Caregiver Middle Name')
    )
    caregiver_last_name = models.CharField(
        max_length=500,
        blank=False,
        null=True,
        verbose_name=_('Caregiver Last Name')
    )
    caregiver_mother_name = models.CharField(
        max_length=500,
        blank=False,
        null=True,
        verbose_name=_('Caregiver  Mother Full Name')
    )
    main_caregiver_nationality = models.ForeignKey(
        Nationality,
        blank=True, null=True,
        related_name='+',
        on_delete=models.SET_NULL,
        verbose_name=_('Caregiver Nationality')
    )
    main_caregiver_nationality_other = models.TextField(
        blank=True, null=True,
        verbose_name=_('Please specify')
    )

    def __str__(self):
        if not self.first_name:
            return 'No name'

        return u'{} {} {}'.format(
            self.first_name,
            self.father_name,
            self.last_name,
        )

    def __unicode__(self):
        if not self.first_name:
            return 'No name'

        return u'{} {} {}'.format(
            self.first_name,
            self.father_name,
            self.last_name,
        )

    @property
    def full_name(self):
        return u'{} {} {}'.format(
            self.first_name,
            self.father_name,
            self.last_name,
        )

    @property
    def caregiver_full_name(self):
        return u'{} {} {}'.format(
            self.caregiver_first_name,
            self.caregiver_middle_name,
            self.caregiver_last_name,
        )

    @property
    def id_number(self):
        # 1	"UNHCR Registered"
        if self.id_type.id == 1:
            return  self.individual_case_number
        # 2	"UNHCR Recorded"
        elif self.id_type.id == 2:
            return  ''
        # 3	"Syrian national ID"
        elif self.id_type.id == 3:
            return  self.syrian_national_number
        # 4	"Palestinian national ID"
        elif self.id_type.id == 4:
            return  self.sop_national_number
        # 5	"Lebanese national ID"
        elif self.id_type.id == 5:
            return  self.national_number
        # 6	"Other nationality"
        elif self.id_type.id == 6:
            return  self.other_number
        # 7 "Caregiver has no ID"
        else:
            return ""

    @property
    def caregiver_id_number(self):
        # 1	"UNHCR Registered"
        if self.id_type.id == 1:
            return self.parent_individual_case_number
        # 2	"UNHCR Recorded"
        elif self.id_type.id == 2:
            return self.recorded_number
        # 3	"Syrian national ID"
        elif self.id_type.id == 3:
            return self.parent_syrian_national_number
        # 4	"Palestinian national ID"
        elif self.id_type.id == 4:
            return self.parent_sop_national_number
        # 5	"Lebanese national ID"
        elif self.id_type.id == 5:
            return self.parent_national_number
        # 6	"Other nationality"
        elif self.id_type.id == 6:
            return self.parent_other_number
        # 9	"Lebanese Extract of Record "
        elif self.id_type.id == 9:
            return self.parent_extract_record
        # 7 "Caregiver has no ID"
        else:
            return ""

    def nationality_name(self):
        if self.nationality:
            return self.nationality.name
        return ''

    @property
    def nationality_name_en(self):
        if self.nationality:
            return self.nationality.name_en

        return ''

    @property
    def birthday(self):
        return u'{}/{}/{}'.format(
            self.birthday_day,
            self.birthday_month,
            self.birthday_year,
        )

    @property
    def birthdate(self):
        return u'{}-{}-{}'.format(
            self.birthday_year,
            self.birthday_month,
            self.birthday_day,
        )
    @property
    def age(self):
        return self.get_age(self.birthday_year, self.birthday_month, self.birthday_day)

    @property
    def age_month(self):
        full_age = self.calculate_age
        months = full_age[1]
        if full_age[0]:
            months = full_age[0]*12 + months
        return months

    @property
    def age_year_month(self):
        full_age = self.calculate_age
        if full_age[0]:
            return str(full_age[0]) + " years - " + str(full_age[1]) + " months"
        else:
            return str(full_age[1]) + " months"

    @staticmethod
    def get_age(birthday_year, birthday_month, birthday_day):
        if birthday_year and birthday_month and birthday_day:
            today = datetime.datetime.now()
            return today.year - int(birthday_year) - (
                    (today.month, today.day) < (int(birthday_month), int(birthday_day)))
        # if self.birthday_year:
        #     return int(self.CURRENT_YEAR)-int(self.birthday_year)
        return 0

    @property
    def calculate_age(self):

        today = datetime.datetime.today()

        age = today - datetime.datetime(int(self.birthday_year), int(self.birthday_month), int(self.birthday_day))
        years = age.days // 365
        months = (age.days - years * 365) // 30
        days = age.days - years * 365 - months * 30

        return years, months, days

    def save(self, **kwargs):
        # if self.phone:
        #     self.std_phone = self.phone_prefix + self.phone
        """
        Generate unique IDs for every person
        :param kwargs:
        :return:
        """
        # if self.pk is None:
        self.number = generate_id(
            self.first_name,
            self.father_name,
            self.last_name,
            self.mother_fullname,
            self.gender,
            self.birthday_day,
            self.birthday_month,
            self.birthday_year
        )

        # self.unicef_id = generate_one_unique_id(
        #     str(self.pk),
        #     self.first_name,
        #     self.father_name,
        #     self.last_name,
        #     self.mother_fullname,
        #     self.birthdate,
        #     self.nationality_name_en(),
        #     self.gender
        # )

        super(Adolescent, self).save(**kwargs)
