from django.shortcuts import render, get_object_or_404
from .models import Announcement
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import *


def announcement_list(request):
    announcements = Announcement.objects.all()
    return render(request, 'announcements/announcement_list.html', {'announcements': announcements})

def announcement_detail(request, pk):
    announcement = get_object_or_404(Announcement, pk=pk)
    return render(request, 'announcements/announcement_detail.html', {'announcement': announcement})


@login_required
def create_announcement(request):
    if not request.user.is_special_user:
        return redirect('home')
    if request.method == 'POST':
        form = AnnouncementForm(request.POST)
        if form.is_valid():
            announcement = form.save(commit=False)
            announcement.author = request.user
            announcement.save()
            return redirect('special_users:dashboard')
    else:
        form = AnnouncementForm()
    return render(request, 'announcements/create_announcement.html', {'form': form})
