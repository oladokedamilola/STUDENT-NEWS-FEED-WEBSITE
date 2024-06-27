import json
from django.core.management.base import BaseCommand
from students.models import Student

class Command(BaseCommand):
    help = 'Import students from a JSON file'

    def add_arguments(self, parser):
        parser.add_argument('json_file', type=str, help='Path to the JSON file containing student data')

    def handle(self, *args, **kwargs):
        json_file = kwargs['json_file']

        with open(json_file, 'r') as file:
            students_data = json.load(file)

        for student_data in students_data:
            Student.objects.create(
                matric_number=student_data['matric_number'],
                full_name=student_data['full_name'],
                faculty=student_data['faculty'],
                department=student_data['department'],
                phone_number=student_data['phone_number'],
                email=student_data['email'],
                gender=student_data['gender']
            )

        self.stdout.write(self.style.SUCCESS('Successfully imported student data'))
