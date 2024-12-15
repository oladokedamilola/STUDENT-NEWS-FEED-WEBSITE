from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group, Permission
from .models import CustomUser, PreRegisteredStudent, Student, Notification

class CustomUserAdmin(BaseUserAdmin):
    model = CustomUser
    list_display = ('username', 'email', 'is_special_user', 'is_superuser', 'is_staff')
    list_filter = ('is_special_user', 'is_superuser', 'is_staff', 'groups')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
        ('Special Info', {'fields': ('is_special_user',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'is_special_user'),
        }),
    )
    search_fields = ('username', 'email')
    ordering = ('username',)
    filter_horizontal = ('groups', 'user_permissions')

class PreRegisteredStudentAdmin(admin.ModelAdmin):
    list_display = ('matric_number', 'first_name', 'last_name', 'gender', 'department')
    search_fields = ('matric_number', 'first_name', 'last_name', 'department')
    list_filter = ('gender', 'department')

class StudentAdmin(admin.ModelAdmin):
    list_display = ('matric_number', 'full_name', 'department', 'phone_number', 'email', 'gender')
    search_fields = ('matric_number', 'full_name', 'department', 'phone_number', 'email')
    list_filter = ('department', 'gender')

class NotificationAdmin(admin.ModelAdmin):
    list_display = ('user', 'notification_type', 'created_at', 'is_read')
    list_filter = ('notification_type', 'is_read', 'created_at')
    search_fields = ('user__username', 'content')

# Register models with the admin site
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(PreRegisteredStudent, PreRegisteredStudentAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Notification, NotificationAdmin)
