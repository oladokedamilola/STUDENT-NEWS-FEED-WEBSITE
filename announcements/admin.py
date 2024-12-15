from django.contrib import admin
from .models import Announcement

class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_date')
    list_filter = ('created_date', 'author')
    search_fields = ('title', 'content', 'author__username')
    date_hierarchy = 'created_date'
    ordering = ('-created_date',)
    readonly_fields = ('created_date',)

    def save_model(self, request, obj, form, change):
        if not change:  # Custom logic for new announcements
            # You can add custom logic here if needed for new announcements
            pass
        super().save_model(request, obj, form, change)

# Register the model with the admin site
admin.site.register(Announcement, AnnouncementAdmin)
