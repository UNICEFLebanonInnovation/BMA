# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django.contrib.auth.models import AbstractUser
# from django.urls import reverse
from django.urls import reverse
from django.db import models
# from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import gettext as _


# @python_2_unicode_compatible
class User(AbstractUser):
    # from student_registration.locations.models import Location, Center
    # from student_registration.schools.models import PartnerOrganization, School
    # from student_registration.youth.models import Partner

    # First Name and Last Name do not cover name patterns
    # around the globe.
    partner = models.ForeignKey(
        'schools.PartnerOrganization',
        blank=True, null=True,
        verbose_name=_('Partner'),
        related_name='+',
        on_delete=models.SET_NULL
    )
    phone_number = models.CharField(
        _('Phone number'),
        max_length=20,
        null=True,
        blank=True
    )
    school = models.ForeignKey(
        'schools.School',
        blank=True, null=True,
        related_name='+',
        on_delete=models.SET_NULL
    )
    location = models.ForeignKey(
        'locations.Location',
        blank=True, null=True,
        related_name='+',
        on_delete=models.SET_NULL
    )
    center = models.ForeignKey(
        'locations.Center',
        blank=True, null=True,
        related_name='+',
        on_delete=models.SET_NULL
    )
    locations = models.ManyToManyField('locations.Location', blank=True)
    schools = models.ManyToManyField('schools.School', blank=True)
    regions = models.ManyToManyField('locations.Location', blank=True, related_name='regions')
    staff_password = models.CharField(
        _('staff password'),
        max_length=255,
        null=True,
        blank=True
    )
    # youth_partner = models.ForeignKey(
    #     'youth.Partner',
    #     blank=True, null=True,
    #     verbose_name=_('Youth Partner'),
    #     related_name='+',
    #     on_delete=models.SET_NULL
    # )

    def __str__(self):
        return self.username

    def update_password(self, password):
        self.set_password(password)

    def get_absolute_url(self):
        return reverse('users:detail', kwargs={'username': self.username})


class Login(models.Model):
    # from student_registration.schools.models import EducationYear
    user = models.ForeignKey(
        'User',
        blank=True, null=True,
        verbose_name=_('User'),
        on_delete=models.SET_NULL
    )
    education_year = models.ForeignKey(
        'schools.EducationYear',
        blank=True, null=True,
        related_name='+',
        verbose_name=_('Education year'),
        on_delete=models.SET_NULL
    )
    active = models.BooleanField(default=True)

    def __unicode__(self):

        return u'{} {}'.format(
            self.user,
            self.education_year,
        )

    class Meta:
        verbose_name_plural = "Login"
