__author__ = 'achamseddine'

from django.core.management.base import BaseCommand

from student_registration.students.tasks import generate_2ndshift_unique_number


class Command(BaseCommand):
    help = 'Generate unique number for 2ndshift'

    def add_arguments(self, parser):
        parser.add_argument('offset', nargs='+', type=int)

    def handle(self, *args, **options):
        for offset in options['offset']:
            generate_2ndshift_unique_number(offset)
