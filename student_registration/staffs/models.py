from __future__ import unicode_literals, absolute_import, division
import datetime
from django.conf import settings
from django.db import models
from django.utils.translation import gettext as _
from model_utils import Choices
from student_registration.students.models import Nationality
# Create your models here.
import django.utils.timezone
from PIL import Image
from django.core.exceptions import ValidationError


def validate_file_size(value):
    filesize = value.size
    if filesize > 250000:
        raise ValidationError("The maximum file size that can be uploaded is 250K")
    else:
        return value


class Bank(models.Model):
    code = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=45, unique=True)

    class Meta:
        ordering = ['code']
        verbose_name_plural = "Bank"

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name


class Certificate(models.Model):
    name = models.CharField(max_length=60, unique=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name


class University(models.Model):
    name = models.CharField(max_length=60, unique=True)

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'Universities'

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name


class Staffs(models.Model):
    from student_registration.locations.models import Location
    EDUCATION_YEARS = list((str(x - 1) + '/' + str(x), str(x - 1) + '/' + str(x)) for x in range(2001, 2050))
    EDUCATION_YEARS.append(('na', 'N/A'))
    TYPEOFEMP = Choices(
        ('Cadre', _('Cadre')),
        ('Contractual', _('Contractual')),
        ('Supporter', _('Supporter')),
    )
    MinisAppr = Choices(
        ('Exceptional', _('Exceptional Approved')),
        ('AccordingToCond', _('Consent According to Conditions')),
        ('CadreOrCont', _('Cadre / Contractual')),
    )

    CURRENT_YEAR = datetime.datetime.now().year

    MONTHS = Choices(
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

    GENDER = Choices(
        ('Male', _('Male')),
        ('Female', _('Female')),
    )
    FAMILY_STATUS = Choices(
        ('married', _('Married')),
        ('engaged', _('Engaged')),
        ('divorced', _('Divorced')),
        ('widower', _('Widower')),
        ('single', _('Single')),
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
    id_number = models.CharField(max_length=30, blank=False)
    ministerapproval = models.CharField(
        max_length=150,
        blank=True,
        null=True,
        choices=MinisAppr,
        verbose_name=_('Minister Approved')
    )
    image = models.ImageField(
        upload_to="profiles",
        null=True,
        blank=True,
        help_text=_('Profile Picture'),
        verbose_name=_('Profile Picture'),
        validators=[validate_file_size]
    )
    mother_fullname = models.CharField(
        max_length=64,
        db_index=True,
        blank=True, null=True,
        verbose_name=_('Mother fullname')
    )
    sex = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        choices=GENDER,
        verbose_name=_('Sex')
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
    place_of_birth = models.CharField(
        max_length=200,
        blank=True,
        null=True,
        verbose_name=_('Place of birth')
    )
    family_status = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        choices=FAMILY_STATUS,
        verbose_name=_('Family status')
    )
    phone = models.CharField(max_length=24, blank=True, null=True, verbose_name=_('Phone number'))
    nationality = models.ForeignKey(
        Nationality,
        blank=True, null=True,
        on_delete=models.SET_NULL,
        verbose_name=_('Nationality')
    )
    address = models.TextField(
        blank=True,
        null=True,
        verbose_name=_('Address')
    )
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        blank=False, null=True,
        verbose_name=_('Created by'),
        related_name='+',
        on_delete=models.SET_NULL,
    )
    created = models.DateTimeField(default=django.utils.timezone.now)
    bank_base1 = models.ForeignKey(
        Bank,
        blank=True, null=True,
        related_name='+',
        on_delete=models.SET_NULL,
        verbose_name=_('Bank'),
    )
    branch_base1 = models.CharField(
        max_length=60,
        blank=True,
        null=True,
        verbose_name=_('Branch')
    )
    iban_base1 = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name=_('IBAN LL')
    )
    bank_base2 = models.ForeignKey(
        Bank,
        related_name='+',
        blank=True, null=True,
        on_delete=models.SET_NULL,
        verbose_name=_('Bank'),
    )
    branch_base2 = models.CharField(
        max_length=60,
        blank=True,
        null=True,
        verbose_name=_('Branch')
    )
    iban_base2 = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name=_('IBAN $')
    )
    type_of_employment = models.CharField(
        max_length=80,
        blank=True,
        null=True,
        choices=TYPEOFEMP,
        verbose_name=_('Type on Employment')
    )
    certificate = models.ForeignKey(
        Certificate,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        verbose_name=_('Certificate')
    )
    university = models.ForeignKey(
        University,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        verbose_name=_('University Name')
    )
    automated_nb = models.CharField(
        max_length=15,
        blank=True, null=True,
        verbose_name=_('Automated Nb')
    )
    financial_nb = models.CharField(
        max_length=20,
        blank=True, null=True,
        verbose_name=_('Financial Nb')
    )
    governorate = models.ForeignKey(
        Location,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        verbose_name=_('Governorate'),
        related_name='staff_governorate'
    )
    caza = models.ForeignKey(
        Location,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        verbose_name=_('Caza'),
        related_name='staff_caza'
    )
    staff_seq = models.IntegerField(blank=True, null=True)
    email = models.EmailField(blank=True, max_length=254, verbose_name='email address')
    first_education_year = models.CharField(
        max_length=10,
        blank=True,
        null=True,
        choices=EDUCATION_YEARS,
        verbose_name=_('Last Education year')
    )
    speciality = models.CharField(
        max_length=70,
        blank=True, null=True,
        verbose_name=_('Speciality')
    )
    cert_origin = models.CharField(
        max_length=70,
        blank=True, null=True,
        verbose_name=_('Speciality')
    )
    pic_identification = models.CharField(
        max_length=200,
        blank=True, null=True,
        verbose_name=_('Picture of Identy')
    )
    pic_commitment = models.CharField(
        max_length=200,
        blank=True, null=True,
        verbose_name=_('Picture of the commitment')
    )
    pic_2ndshiftcertificate = models.CharField(
        max_length=200,
        blank=True, null=True,
        verbose_name=_('Picture of the second shift certificate')
    )
    pic_iban = models.CharField(
        max_length=200,
        blank=True, null=True,
        verbose_name=_('Picture of the iban')
    )
    pic_certificate = models.CharField(
        max_length=200,
        blank=True, null=True,
        verbose_name=_('Picture of the certificate')
    )
    disabled = models.BooleanField(
        blank=True, default=False,
        verbose_name=_('Disabled?')
    )
    pic_iban2 = models.CharField(
        max_length=200,
        blank=True, null=True,
        verbose_name=_('Picture of the iban')
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

    class Meta:
        verbose_name_plural = "Staff"


class ParticipantYear(models.Model):
    SELECTYEAR = Choices(
        ('2013/2014', '2013/2014'),
        ('2014/2015', '2014/2015'),
        ('2015/2016', '2015/2016'),
        ('2016/2017', '2016/2017'),
        ('2017/2018', '2017/2018'),
        ('2018/2019', '2018/2019'),
        ('2019/2020', '2019/2020'),
        ('2020/2021', '2020/2021'),
    )
    participantyear = models.CharField(
        max_length=9,
        blank=True,
        null=True,
        choices=SELECTYEAR
    )
    notes = models.CharField(
        max_length=150,
        blank=True, null=True
    ),

    staff = models.ForeignKey(
        Staffs,
        blank=True, null=True,
        related_name='+',
        on_delete=models.SET_NULL,
        verbose_name=_('Staff')
    )
