from django.contrib import admin
from .models import CreatorApplication

@admin.register(CreatorApplication)
class CreatorApplicationAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'approved', 'created_at', 'reviewed_at', 'reviewed_by')
    list_filter = ('approved', 'reviewed_at')
    search_fields = ('title', 'main_content', 'user__username')
    readonly_fields = ('created_at', 'reviewed_at', 'reviewed_by')
    fields = ('title', 'main_content', 'approved', 'created_at', 'reviewed_at', 'user', 'reviewed_by')
    ordering = ('-created_at',)

    def get_readonly_fields(self, request, obj=None):
        if obj:  # Editing an existing object
            return self.readonly_fields + ('user',)
        return self.readonly_fields

    def save_model(self, request, obj, form, change):
        if not change:  # Creating a new object
            obj.reviewed_by = None  # Make sure reviewed_by is not set on creation
        super().save_model(request, obj, form, change)
