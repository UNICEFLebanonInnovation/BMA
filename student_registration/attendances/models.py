from __future__ import unicode_literals, absolute_import, division

from django.db import models
#from django.db.models import Index
from django.conf import settings
from django.utils.translation import gettext as _ # Will be fixed in a subsequent step
from django.db.models import JSONField

from model_utils import Choices
from model_utils.models import TimeStampedModel

from student_registration.students.models import (
    Student,
)
from student_registration.schools.models import (
    School,
    Section,
    ClassRoom,
    EducationLevel,
    EducationYear
)
from student_registration.locations.models import Center
from student_registration.child.models import Child
from student_registration.alp.models import ALPRound
from student_registration.mscc.models import Registration
from student_registration.clm.models import Bridging


class Attendance(TimeStampedModel):

    ABSENCE_REASON = Choices(
        ('sick', _('Sick')),
        ('no_transport', _('No transport')),
        ('other', _('Other reason')),
    )

    CLOSE_REASON = Choices(
        ('public_holiday', _('Public Holiday')),
        ('school_holiday', _('School Holiday')),
        ('strike', _('Strike')),
        ('weekly_holiday', _('Weekly Holiday')),
    )

    DEFAULT_ATTENDANCE_RANGE = 10

    student = models.ForeignKey(
        Student,
        blank=True, null=True,
        related_name='attendances',
        on_delete=models.CASCADE,
    )
    school = models.ForeignKey(
        School,
        blank=False, null=True,
        related_name='attendances',
        on_delete=models.CASCADE,
    )
    classroom = models.ForeignKey(
        ClassRoom,
        blank=True, null=True,
        related_name='+',
        on_delete=models.SET_NULL,
    )
    classlevel = models.ForeignKey(
        EducationLevel,
        blank=True, null=True,
        related_name='+',
        on_delete=models.SET_NULL,
    )
    section = models.ForeignKey(
        Section,
        blank=True, null=True,
        related_name='+',
        on_delete=models.SET_NULL,
    )
    status = models.BooleanField(default=False)
    attendance_date = models.DateField(blank=True, null=True)
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        blank=True, null=True,
        related_name='+',
        on_delete=models.SET_NULL,
    )
    validation_status = models.BooleanField(default=False)
    validation_date = models.DateField(blank=True, null=True)
    validation_owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        blank=True, null=True,
        related_name='+',
    )
    absence_reason = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        choices=ABSENCE_REASON
    )
    close_reason = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        choices=CLOSE_REASON
    )

    students = JSONField(default=dict)

    total_enrolled = models.IntegerField(blank=True, null=True)
    total_attended = models.IntegerField(blank=True, null=True)
    total_absences = models.IntegerField(blank=True, null=True)
    total_attended_male = models.IntegerField(blank=True, null=True)
    total_attended_female = models.IntegerField(blank=True, null=True)
    total_absent_male = models.IntegerField(blank=True, null=True)
    total_absent_female = models.IntegerField(blank=True, null=True)
    school_type = models.CharField(max_length=20, blank=True, null=True, default=None)
    education_year = models.ForeignKey(
        EducationYear,
        blank=True, null=True,
        related_name='+',
        on_delete=models.SET_NULL,
    )
    alp_round = models.ForeignKey(
        ALPRound,
        blank=True, null=True,
        related_name='+',
        on_delete=models.SET_NULL,
    )

    class Meta:
        # ordering = ['attendance_date']
        verbose_name = "Attendances by School by Day"

    @property
    def student_fullname(self):
        if self.student:
            return self.student.full_name
        return ''

    @property
    def student_gender(self):
        return self.student.sex

    def __unicode__(self):
        return self.school.__unicode__()

    def save(self, **kwargs):
        """
        """
        if self.students:
            self.total_attended = 0
            self.total_absences = 0
            self.total_attended_male = 0
            self.total_attended_female = 0
            self.total_absent_male = 0
            self.total_absent_female = 0
            for level_section in self.students:
                self.total_attended += self.students[level_section]['total_attended']
                self.total_absences += self.students[level_section]['total_absences']
                self.total_attended_male += self.students[level_section]['total_attended_male']
                self.total_attended_female += self.students[level_section]['total_attended_female']
                self.total_absent_male += self.students[level_section]['total_absent_male']
                self.total_absent_female += self.students[level_section]['total_absent_female']

        if self.close_reason:
            self.students = {}

        super(Attendance, self).save(**kwargs)


class BySchoolByDay(models.Model):

    school = models.ForeignKey(
        School,
        related_name='+',
        on_delete=models.CASCADE,
    )
    attendance_date = models.DateField()
    highest_attendance_rate = models.BooleanField(default=False)
    total_enrolled = models.IntegerField(blank=True, null=True)
    total_attended = models.IntegerField(blank=True, null=True)
    total_absences = models.IntegerField(blank=True, null=True)
    total_attended_male = models.IntegerField(blank=True, null=True)
    total_attended_female = models.IntegerField(blank=True, null=True)
    total_absent_male = models.IntegerField(blank=True, null=True)
    total_absent_female = models.IntegerField(blank=True, null=True)
    validation_date = models.DateField(blank=True, null=True)
    validation_status = models.BooleanField(default=False)


class Absentee(TimeStampedModel):

    school = models.ForeignKey(
        School,
        related_name='+',
        on_delete=models.CASCADE,
    )
    student = models.ForeignKey(
        Student,
        related_name='absents',
        on_delete=models.CASCADE,
    )
    last_attendance_date = models.DateField(blank=True, null=True)
    last_absent_date = models.DateField(blank=True, null=True)
    absent_days = models.IntegerField(blank=True, null=True)
    attended_days = models.IntegerField(blank=True, null=True)

    total_absent_days = models.IntegerField(blank=True, null=True)
    total_attended_days = models.IntegerField(blank=True, null=True)

    reattend_date = models.DateField(blank=True, null=True)
    validation_status = models.BooleanField(default=False)
    last_modification_date = models.DateField(blank=True, null=True)
    dropout_status = models.BooleanField(default=False)
    disabled = models.BooleanField(
        blank=True, default=False,
        verbose_name=_('disabled')
    )
    education_year = models.ForeignKey(
        EducationYear,
        blank=True, null=True,
        related_name='+',
        on_delete=models.SET_NULL,
    )
    alp_round= models.ForeignKey(
        ALPRound,
        blank=True, null=True,
        related_name='+',
        on_delete=models.SET_NULL,
    )
    level = models.CharField(max_length=100, blank=True, null=True)
    level_name = models.CharField(max_length=100, blank=True, null=True)
    section = models.CharField(max_length=100, blank=True, null=True)
    section_name = models.CharField(max_length=100, blank=True, null=True)

    def __unicode__(self):
        return '{} - {}'.format(self.student, self.school)

    def absence_type(self):
        if 10 > self.absent_days >= 5:
            return '5'
        if self.absent_days >= 10:
            return '10'
        return '0'

    def student_number(self):
        return self.student.number


class AttendanceDt(models.Model):
    attendance = models.ForeignKey(
        Attendance,
        blank=True, null=True,
        related_name='attendances',
        on_delete=models.SET_NULL,
    )
    school = models.ForeignKey(
        School,
        blank=False, null=True,
        on_delete=models.CASCADE,
    )
    classroom = models.ForeignKey(
        ClassRoom,
        blank=True, null=True,
        on_delete=models.SET_NULL,
    )
    classlevel = models.ForeignKey(
        EducationLevel,
        blank=True, null=True,
        on_delete=models.SET_NULL,
    )
    section = models.ForeignKey(
        Section,
        blank=True, null=True,
        on_delete=models.SET_NULL,
    )
    student = models.ForeignKey(
        Student,
        blank=False, null=True,
        on_delete=models.SET_NULL,
    )
    is_present = models.BooleanField(default=False)
    attendance_date = models.DateField(blank=True, null=True, db_index=True)
    levelname = models.CharField(max_length=100, blank=True, null=True, default=None)
    #
    # class Meta:
    # indexes = [
    #     Index(fields=['attendance_date', 'school']),
    # ]


class AttendanceSyncLog(models.Model):

    school = models.ForeignKey(School, on_delete=models.CASCADE)
    school_type = models.CharField(
        max_length=50,
        blank=True,
        null=True,
    )
    total_records = models.IntegerField(default=0)
    total_processed = models.IntegerField(default=0)
    successful = models.BooleanField(default=False)
    exception_message = models.TextField(blank=True, null=True)
    response_message = models.TextField(blank=True, null=True)
    processed_date = models.DateTimeField(auto_now=True)
    processed_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        blank=True, null=True,
        related_name='+',
        on_delete=models.SET_NULL,
    )

    def __unicode__(self):
        return str(self.processed_date)

    class Meta:
        ordering = ['processed_date']


class CLMAttendance(TimeStampedModel):
    YES_NO = Choices(
        ('', '----------'),
        ('yes', _("Yes")),
        ('no', _("No")),
    )
    REGISTRATION_LEVEL = (
        ('', '----------'),
        ('level_one', _('Level one')),
        ('level_two', _('Level two')),
        ('level_three', _('Level three')),
        ('level_four', _('Level four')),
        ('level_five', _('Level five')),
        ('level_six', _('Level six'))
    )
    CLOSE_REASON = Choices(
        ('', '----------'),
        ('public_holiday', _('Public Holiday')),
        ('school_holiday', _('School Holiday')),
        ('strike', _('Strike')),
        ('weekly_holiday', _('Weekly Holiday')),
        ('roads_closed', _('Roads Closed')),
    )
    round_id = models.IntegerField(blank=True, null=True)
    school = models.ForeignKey(
        School,
        blank=False, null=True,
        related_name='+',
        on_delete=models.SET_NULL,
    )
    registration_level = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        choices=REGISTRATION_LEVEL,
        verbose_name=_('Registration level')
    )
    attendance_date = models.DateField(
        blank=True,
        null=True,
        verbose_name=_('Attendance date')
    )

    day_off = models.CharField(
        max_length=10,
        blank=True,
        null=True,
        choices=YES_NO,
        verbose_name=_('Day off ?')
    )
    close_reason = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        choices=CLOSE_REASON,
        verbose_name=_('Day off reason')
    )

    class Meta:
        ordering = ['attendance_date']
        verbose_name = "Dirasa Attendance"

    def __unicode__(self):
        return self.school.__unicode__()


class CLMAttendanceStudent(TimeStampedModel):
    readonly_fields = ('student_name')

    ABSENCE_REASON = Choices(
        ('', '----------'),
        ('sick', _('Sick')),
        ('no_transport', _('No transport')),
        ('other', _('Other reason')),
    )

    YES_NO = Choices(
        ('', '----------'),
        ('yes', _("Yes")),
        ('no', _("No")),
    )
    attendance_day = models.ForeignKey(
        CLMAttendance,
        blank=True, null=True,
        related_name='+',
        on_delete=models.SET_NULL,
    )
    registration = models.ForeignKey(
        Bridging,
        blank=False, null=True,
        related_name='+',
        on_delete=models.SET_NULL,
        verbose_name=_('Registration')
    )
    student = models.ForeignKey(
        Student,
        blank=True, null=True,
        related_name='+',
        on_delete=models.SET_NULL,
        verbose_name=_('Student')
    )
    attended = models.CharField(
        max_length=10,
        blank=True,
        null=True,
        choices=YES_NO,
        verbose_name=_('Student Attended?')
    )
    absence_reason = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        choices=ABSENCE_REASON
    )
    absence_reason_other = models.CharField(
        max_length=500,
        blank=True,
        null=True,
        verbose_name=_('specify')
    )

    class Meta:
        ordering = ['id']
        verbose_name = "Dirasa Student Attendance"

    @property
    def student_name(self):
        result = ''
        if self.student:
            result = self.student.full_name
        return result

    @property
    def student_gender(self):
        result = ''
        if self.student:
            result = self.student.student_gender
        return result

    @property
    def student_fullname(self):
        if self.student:
            return self.student.full_name
        return ''


class CLMStudentAbsences(TimeStampedModel):

    student_id = models.IntegerField(blank=True, null=True)
    registration_id = models.IntegerField(blank=True, null=True)
    round_id = models.IntegerField(blank=True, null=True)
    partner_id = models.IntegerField(blank=True, null=True)
    school_id = models.IntegerField(blank=True, null=True)
    student_first_name = models.CharField(
        max_length=100,
        blank=True,
        null=True,
    )
    student_father_name = models.CharField(
        max_length=100,
        blank=True,
        null=True,
    )
    student_last_name = models.CharField(
        max_length=100,
        blank=True,
        null=True,
    )
    school_name = models.CharField(
        max_length=200,
        blank=True,
        null=True,
    )
    registation_level = models.CharField(
        max_length=50,
        blank=True,
        null=True,
    )
    absence_starting_date = models.DateField(blank=True, null=True)
    absence_ending_date = models.DateField(blank=True, null=True)
    absence_dates = JSONField(default=dict)
    consecutive_absence_days = models.IntegerField(blank=True, null=True)

    def update_absence_statisics(self, consecutive_absences, ending_date, consecutive_dates):
        self.consecutive_absence_days= consecutive_absences
        self.absence_dates= consecutive_dates
        self.absence_ending_date= ending_date

    class Meta:
        ordering = ['id']
        verbose_name = "Dirasa Student Absences"


class CLMStudentTotalAttendance(TimeStampedModel):

    student_id = models.IntegerField(blank=True, null=True)
    registration_id = models.IntegerField(blank=True, null=True)
    round_id = models.IntegerField(blank=True, null=True)
    partner_id = models.IntegerField(blank=True, null=True)
    school_id = models.IntegerField(blank=True, null=True)
    student_first_name = models.CharField(
        max_length=100,
        blank=True,
        null=True,
    )
    student_father_name = models.CharField(
        max_length=100,
        blank=True,
        null=True,
    )
    student_last_name = models.CharField(
        max_length=100,
        blank=True,
        null=True,
    )
    school_name = models.CharField(
        max_length=200,
        blank=True,
        null=True,
    )
    registation_level = models.CharField(
        max_length=50,
        blank=True,
        null=True,
    )

    total_attendance_days = models.IntegerField(blank=True, null=True)

    total_absence_days = models.IntegerField(blank=True, null=True)


    def update_attendance_statisics(self, total_absence_days):
        self.total_attendance_days = total_absence_days


    def update_absence_statisics(self, total_absence_days):
        self.total_absence_days = total_absence_days

    class Meta:
        ordering = ['id']
        verbose_name = "Dirasa Student Total Attendance"


class MSCCAttendance(TimeStampedModel):
    YES_NO = Choices(
        ('', '----------'),
        ('yes', _("Yes")),
        ('no', _("No")),
    )
    CLOSE_REASON = Choices(
        ('', '----------'),
        ('Public Holiday', _('Public Holiday')),
        ('School Holiday', _('School Holiday')),
        ('Strike', _('Strike')),
        ('Weekly Holiday', _('Weekly Holiday')),
        ('Roads Closed', _('Roads Closed')),
    )
    EDUCATION_PROGRAM = Choices(
        ('BLN Level 1', _('BLN Level 1')),
        ('BLN Level 2', _('BLN Level 2')),
        ('BLN Level 3', _('BLN Level 3')),
        ('BLN Catch-up', _('BLN Catch-up')),
        ('ABLN Level 1', _('ABLN Level 1')),
        ('ABLN Level 2', _('ABLN Level 2')),
        ('ABLN Catch-up', _('ABLN Catch-up')),
        ('YBLN Level 1', _('YBLN Level 1')),
        ('YBLN Level 2', _('YBLN Level 2')),
        ('YBLN Catch-up', _('YBLN Catch-up')),
        ('YFS Level 1', _('YFS Level 1')),
        ('YFS Level 2', _('YFS Level 2')),
        ('YFS Level 1 - RS Grade 9', _('YFS Level 1 - RS Grade 9')),
        ('YFS Level 2 - RS Grade 9', _('YFS Level 2 - RS Grade 9')),
        ('CBECE Level 1', _('CBECE Level 1')),
        ('CBECE Level 2', _('CBECE Level 2')),
        ('CBECE Level 3', _('CBECE Level 3')),
        ('CBECE Catch-up', _('CBECE Catch-up')),
        ('RS Grade 1', _('RS Grade 1')),
        ('RS Grade 2', _('RS Grade 2')),
        ('RS Grade 3', _('RS Grade 3')),
        ('RS Grade 4', _('RS Grade 4')),
        ('RS Grade 5', _('RS Grade 5')),
        ('RS Grade 6', _('RS Grade 6')),
        ('RS Grade 7', _('RS Grade 7')),
        ('RS Grade 8', _('RS Grade 8')),
        ('RS Grade 9', _('RS Grade 9')),
        ('ECD', _('ECD')),
    )
    CLASS_SECTION = Choices(
        ('', '----------'),
        ('A', _('A')),
        ('B', _('B')),
        ('C', _('C')),
        ('D', _('D')),
        ('E', _('E')),
        ('F', _('F')),
        ('G', _('G')),
        ('H', _('H')),
        ('I', _('I')),
        ('J', _('J')),
        ('K', _('K')),
        ('L', _('L')),
        ('M', _('M')),
        ('N', _('N')),
        ('O', _('O')),
        ('P', _('P')),
        ('Q', _('Q')),
        ('R', _('R')),
        ('S', _('S')),
        ('T', _('T')),
        ('U', _('U')),
        ('V', _('V')),
        ('W', _('W')),
        ('X', _('X')),
        ('Y', _('Y')),
        ('Z', _('Z')),
    )
    round_id = models.IntegerField(blank=True, null=True)
    center = models.ForeignKey(
        Center,
        blank=True, null=True,
        related_name='+',
        on_delete=models.SET_NULL,
        verbose_name=_('Center')
    )
    education_program = models.CharField(
        max_length=200,
        blank=True,
        null=True,
        choices=EDUCATION_PROGRAM,
        verbose_name=_('Education Program')
    )
    class_section = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        choices=CLASS_SECTION,
        verbose_name=_('Class Section')
    )

    attendance_date = models.DateField(
        blank=True,
        null=True,
        verbose_name=_('Attendance date')
    )
    day_off = models.CharField(
        max_length=10,
        blank=True,
        null=True,
        choices=YES_NO,
        verbose_name=_('Day off ?')
    )
    close_reason = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        choices=CLOSE_REASON,
        verbose_name=_('Day off reason')
    )

    class Meta:
        ordering = ['attendance_date']
        verbose_name = "Makani Attendance"

    def __str__(self):
        return '{} - {}'.format(self.center, self.attendance_date)

    def __unicode__(self):
        return '{} - {}'.format(self.center, self.attendance_date)


class MSCCAttendanceChild(TimeStampedModel):
    readonly_fields = ('child_name', )

    ABSENCE_REASON = Choices(
        ('', '----------'),
        ('Sick', _('Sick')),
        ('No transport', _('No transport')),
        ('Other', _('Other')),
        ('Unspecified', _('Unspecified')),
    )
    attendance_day = models.ForeignKey(
        MSCCAttendance,
        blank=True, null=True,
        related_name='attendance_child',
        on_delete=models.SET_NULL,
    )
    registration = models.ForeignKey(
        Registration,
        blank=False, null=True,
        related_name='+',
        on_delete=models.SET_NULL,
        verbose_name=_('Registration')
    )
    child = models.ForeignKey(
        Child,
        blank=False, null=True,
        related_name='+',
        on_delete=models.SET_NULL,
        verbose_name=_('Child')
    )
    attended = models.CharField(
        max_length=10,
        blank=True,
        null=True,
        choices=Child.YES_NO,
        verbose_name=_('Child Attended?')
    )
    absence_reason = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        choices=ABSENCE_REASON
    )
    absence_reason_other = models.CharField(
        max_length=500,
        blank=True,
        null=True,
        verbose_name=_('specify')
    )

    class Meta:
        ordering = ['id']
        verbose_name = "Makani Child Attendance"

    @property
    def attendance_date(self):
        return self.attendance_day.attendance_date.strftime("%d/%m/%Y")

    @property
    def child_name(self):
        result = ''
        if self.child:
            result = self.child.full_name
        return result

    @property
    def child_gender(self):
        result = ''
        if self.child:
            result = self.child.gender
        return result

    @property
    def child_fullname(self):
        if self.child:
            return self.child.full_name
        return ''

    def __str__(self):
        return '{} - {}'.format(self.child, self.attendance_day)

    def __unicode__(self):
        return '{} - {}'.format(self.child, self.attendance_day)

