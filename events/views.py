from django.shortcuts import render, get_object_or_404
from .models import Event
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import *


def event_list(request):
    events = Event.objects.all()
    return render(request, 'events/event_list.html', {'events': events})

def event_detail(request, pk):
    event = get_object_or_404(Event, pk=pk)
    return render(request, 'events/event_detail.html', {'event': event})


@login_required
def create_event(request):
    if not request.user.is_special_user:
        return redirect('home')
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.author = request.user
            event.save()
            return redirect('special_users:dashboard')
    else:
        form = EventForm()
    return render(request, 'events/create_event.html', {'form': form})
