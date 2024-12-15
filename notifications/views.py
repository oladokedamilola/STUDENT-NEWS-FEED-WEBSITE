from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Notification

@login_required
def notifications_list(request):
    # Mark all notifications as read
    notifications = request.user.notifications.all()
    notifications.update(is_read=True)

    context = {
        'notifications': notifications
    }
    return render(request, 'notifications/notifications_list.html', context)
