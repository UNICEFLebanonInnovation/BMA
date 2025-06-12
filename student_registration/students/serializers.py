
from rest_framework import serializers
from .models import (
    Student,
    Teacher
)


class StudentSerializer(serializers.ModelSerializer):
    from student_registration.alp.serializers import OutreachSerializer
    from student_registration.enrollments.serializers import EnrollmentSerializer

    id = serializers.IntegerField(read_only=True)
    number = serializers.CharField(read_only=True)
    birthday = serializers.CharField(read_only=True)
    place_of_birth = serializers.CharField(required=False)
    registration = OutreachSerializer(source='last_alp_registration', read_only=True)
    enrollment = EnrollmentSerializer(source='last_enrollment', read_only=True)
    have_children = serializers.CharField(required=False)
    p_code = serializers.CharField(required=False)

    alp_registrations = OutreachSerializer(read_only=True, many=True)
    secondshift_registrations = EnrollmentSerializer(read_only=True, many=True)

    current_alp_registration = OutreachSerializer(read_only=True, many=True)
    current_secondshift_registration = EnrollmentSerializer(read_only=True, many=True)

    def create(self, validated_data):

        try:
            instance = Student.objects.create(**validated_data)
            instance.save()

        except Exception as ex:
            raise serializers.ValidationError({'Student instance': ex})

        return instance

    class Meta:
        model = Student
        fields = (
            'id',
            'first_name',
            'father_name',
            'last_name',
            'full_name',
            'mother_fullname',
            'sex',
            'age',
            'birthday_year',
            'birthday_month',
            'birthday_day',
            'place_of_birth',
            'recordnumber',
            'birthday',
            'phone',
            'phone_prefix',
            'id_number',
            'id_type',
            'registered_in_unhcr',
            'nationality',
            'mother_nationality',
            'family_status',
            'address',
            'number',
            'hh_barcode',
            'registration',
            'enrollment',
            'alp_registrations',
            'secondshift_registrations',
            'current_alp_registration',
            'current_secondshift_registration',
            'have_children',
            'is_specialneeds',
            'specialneeds',
            'specialneedsdt',
            'is_financialsupport',
            'Financialsupport_number',
            'financialsupport',
            'unhcr_family',
            'unhcr_personal',
            'p_code',
        )


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = (
            'id',
            'round',
            'first_name',
            'father_name',
            'last_name',
            'full_name',
            'sex',
            'primary_phone_number',
            'school',
            'email',
            'subjects_provided',
            'registration_level',
            'teacher_assignment',
            'teaching_hours_private_school',
            'teaching_hours_dirasa',
            'trainings',
            'training_sessions_attended',
            'extra_coaching',
            'extra_coaching_specify',
            'attach_short_description_1',
            'attach_type_1',
            'attach_short_description_2',
            'attach_type_2',
            'attach_short_description_3',
            'attach_type_3',
            'attach_short_description_4',
            'attach_type_4',
            'attach_short_description_5',
            'attach_type_5',
        )
