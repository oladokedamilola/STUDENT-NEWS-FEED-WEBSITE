from django.shortcuts import render
from news.models import News
from announcements.models import Announcement
from events.models import Event


def search(request):
    query = request.GET.get('q')
    news_results = News.objects.filter(title__icontains=query)
    announcement_results = Announcement.objects.filter(title__icontains=query)
    event_results = Event.objects.filter(title__icontains=query)
    return render(request, 'search/results.html', {
        'query': query,
        'news_results': news_results,
        'announcement_results': announcement_results,
        'event_results': event_results,
    })
