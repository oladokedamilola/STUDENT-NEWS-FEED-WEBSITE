from django.contrib import admin
from .models import Notification

class NotificationAdmin(admin.ModelAdmin):
    list_display = ('user', 'notification_type', 'is_read', 'created_at', 'content')
    list_filter = ('notification_type', 'is_read', 'created_at', 'user')
    search_fields = ('user__username', 'content')
    date_hierarchy = 'created_at'
    ordering = ('-created_at',)
    readonly_fields = ('created_at',)

    def save_model(self, request, obj, form, change):
        if not change:  # Custom logic for new notifications
            obj.is_read = False
        super().save_model(request, obj, form, change)

# Register the model with the admin site
admin.site.register(Notification, NotificationAdmin)
