from django.contrib import admin
from .models import Student

class StudentAdmin(admin.ModelAdmin):
    list_display = ('matric_number', 'full_name', 'faculty', 'department', 'phone_number', 'email', 'gender')
    search_fields = ('matric_number', 'full_name', 'faculty', 'department', 'email')

admin.site.register(Student, StudentAdmin)
