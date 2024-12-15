from django.shortcuts import render, get_object_or_404
from .models import Announcement
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import *
from news.models import *
from notifications.models import *

def announcement_list(request):
    announcements = Announcement.objects.all()
    categories = Category.objects.all()
    unseen_notifications_count = request.user.notifications.filter(is_read=False).count()
    return render(request, 'announcements/announcement_list.html', {'announcements': announcements, 'categories': categories, 'unseen_notifications_count': unseen_notifications_count})

def announcement_detail(request, pk):
    announcement = get_object_or_404(Announcement, pk=pk)
    categories = Category.objects.all()
    unseen_notifications_count = request.user.notifications.filter(is_read=False).count()
    return render(request, 'announcements/announcement_detail.html', {'announcement': announcement, 'categories': categories, 'unseen_notifications_count': unseen_notifications_count})


def create_announcement(request):
    if request.method == 'POST':
        form = AnnouncementForm(request.POST, request.FILES)
        if form.is_valid():
            announcement = form.save(commit=False)
            announcement.author = request.user
            announcement.save()
            return redirect('Announcements:announcements')
    else:
        form = AnnouncementForm()
    return render(request, 'announcements/create_announcement.html', {'form': form})
