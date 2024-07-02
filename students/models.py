from django.db import models
from django.core.exceptions import ValidationError

import logging

logger = logging.getLogger(__name__)

class PreRegisteredStudent(models.Model):
    matric_number = models.CharField(max_length=20, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=10)
    faculty = models.CharField(max_length=100)
    department = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.matric_number} - {self.first_name} {self.last_name}"


class Student(models.Model):
    FACULTY_CHOICES = [
        ('Management Science', 'Management Science'),
        ('Agriculture', 'Agriculture'),
        ('Social Science', 'Social Science'),
        ('Education', 'Education'),
        ('Science', 'Science'),
        ('Arts', 'Arts'),
        ('Law', 'Law'),
    ]

    matric_number = models.CharField(max_length=11, unique=True)
    full_name = models.CharField(max_length=200)
    faculty = models.CharField(max_length=50, choices=FACULTY_CHOICES)
    department = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    gender = models.CharField(max_length=10)

    def __str__(self):
        return self.matric_number

    def clean(self):
        faculty_matric_prefix = {
            'Management Science': '2001',
            'Agriculture': '2002',
            'Social Science': '2003',
            'Education': '2004',
            'Science': '2005',
            'Arts': '2006',
            'Law': '2007',
        }
        prefix = faculty_matric_prefix.get(self.faculty)
        
        if prefix is None:
            logger.error(f"Faculty {self.faculty} is not valid.")
            raise ValidationError(f"Faculty {self.faculty} is not valid.")
        
        if not self.matric_number.startswith(prefix):
            logger.error(f"Matric number {self.matric_number} does not start with {prefix} for {self.faculty} faculty.")
            raise ValidationError(f"Matric number must start with {prefix} for {self.faculty} faculty.")
 

 
