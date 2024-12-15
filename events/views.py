from django.shortcuts import render, get_object_or_404
from .models import Event
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import *
from news.models import *
from notifications.models import *
import calendar
from datetime import datetime


@login_required
def event_list(request):
    events = Event.objects.all()
    categories = Category.objects.all()
    unseen_notifications_count = request.user.notifications.filter(is_read=False).count()

    # Prepare calendar data
    today = datetime.today()
    cal = calendar.HTMLCalendar(calendar.SUNDAY)
    month_calendar = cal.formatmonth(today.year, today.month, withyear=True)

    return render(request, 'events/event_list.html', {
        'events': events,
        'categories': categories,
        'unseen_notifications_count': unseen_notifications_count,
        'calendar': month_calendar
    })

@login_required
def event_detail(request, pk):
    event = get_object_or_404(Event, pk=pk)
    categories = Category.objects.all()
    unseen_notifications_count = request.user.notifications.filter(is_read=False).count()

    return render(request, 'events/event_detail.html', {
        'event': event,
        'categories': categories,
        'unseen_notifications_count': unseen_notifications_count
    })

def create_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            event = form.save(commit=False)
            event.author = request.user
            event.save()
            return redirect('Event:event')
    else:
        form = EventForm()
    return render(request, 'events/create_event.html', {'form': form})

from django.http import JsonResponse
from .models import Event

def event_calendar(request):
    events = Event.objects.all()
    return render(request, 'events/event_calendar.html', {'events': events})

def event_details(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    event_data = {
        'title': event.title,
        'description': event.description,
        'date': event.date,
        'location': event.location,
        'image': event.image.url if event.image else None,
        'video': event.video if event.video else None
    }
    return JsonResponse(event_data)
