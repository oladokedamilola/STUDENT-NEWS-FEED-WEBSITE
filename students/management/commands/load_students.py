# students/management/commands/load_students.py
import json
from django.core.management.base import BaseCommand
from students.models import PreRegisteredStudent

class Command(BaseCommand):
    help = 'Load student data from JSON file'

    def handle(self, *args, **kwargs):
        with open('students/data/students_data.json', 'r') as file:
            data = json.load(file)
            for student in data:
                PreRegisteredStudent.objects.create(
                    matric_number=student['matric_number'],
                    first_name=student['first_name'],
                    last_name=student['last_name'],
                    gender=student['gender'],
                    faculty=student['faculty'],
                    department=student['department']
                )
        self.stdout.write(self.style.SUCCESS('Successfully loaded student data'))
