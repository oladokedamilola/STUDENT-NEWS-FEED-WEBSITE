
from django.db import models
from django.core.exceptions import ValidationError

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
        if not self.matric_number.startswith(prefix):
            raise ValidationError(f"Matric number must start with {prefix} for {self.faculty} faculty.")
        
 

 
