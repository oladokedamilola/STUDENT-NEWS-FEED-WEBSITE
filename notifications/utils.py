from django.utils import timezone
from .models import Notification  # Ensure this import is correct

def create_notification(user, content, notification_type, post_url=None):
    Notification.objects.create(
        user=user,
        content=content,
        notification_type=notification_type,
        created_at=timezone.now(),
        is_read=False,
        post_url=post_url
    )
