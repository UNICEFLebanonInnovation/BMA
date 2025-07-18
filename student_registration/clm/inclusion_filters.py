from django.utils.translation import gettext as _

from django_filters import FilterSet, ModelChoiceFilter

from student_registration.locations.models import Location
from student_registration.schools.models import CLMRound
from student_registration.students.models import Nationality
from .models import Inclusion, Disability


class CommonFilter(FilterSet):
    round = ModelChoiceFilter(queryset=CLMRound.objects.filter(current_year_inclusion=True).all(), empty_label=_('Round'))
    governorate = ModelChoiceFilter(queryset=Location.objects.filter(parent__isnull=True), empty_label=_('Governorate'))
    district = ModelChoiceFilter(queryset=Location.objects.filter(parent__isnull=False), empty_label=_('District'))
    student__nationality = ModelChoiceFilter(queryset=Nationality.objects.exclude(id=9), empty_label=_('Nationality'))
    disability = ModelChoiceFilter(queryset=Disability.objects.filter(active=True), empty_label=_('Disability'))


class InclusionFilter(CommonFilter):

    class Meta:
        model = Inclusion
        fields = {
            'student__id_number': ['contains'],
            'student__number': ['contains'],
            'internal_number': ['contains'],
            'student__first_name': ['contains'],
            'student__father_name': ['contains'],
            'student__last_name': ['contains'],
            'student__mother_fullname': ['contains'],
            'student__nationality': ['exact'],
            'governorate': ['exact'],
            'district': ['exact'],
            'participation': ['exact'],
            'learning_result': ['exact'],
            'owner__username': ['contains'],
            'disability': ['exact'],
        }
