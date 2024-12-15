from django.shortcuts import render
from django.db.models import Q
from news.models import News
from announcements.models import Announcement
from events.models import Event
from notifications.models import *


def search_results(request):
    unseen_notifications_count = request.user.notifications.filter(is_read=False).count()
    query = request.GET.get('q')
    news_results = News.objects.filter(
        Q(title__icontains=query) | Q(content__icontains=query) | Q(author__username__icontains=query)
    )
    announcement_results = Announcement.objects.filter(
        Q(title__icontains=query) | Q(content__icontains=query) | Q(author__username__icontains=query)
    )
    event_results = Event.objects.filter(
        Q(title__icontains=query) | Q(content__icontains=query) | Q(author__username__icontains=query)
    )

    context = {
        'query': query,
        'news_results': news_results,
        'announcement_results': announcement_results,
        'event_results': event_results,
        'unseen_notifications_count': unseen_notifications_count
    }
    return render(request, 'search/search_results.html', context)
