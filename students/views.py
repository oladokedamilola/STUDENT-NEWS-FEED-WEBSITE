from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import StudentRegistrationForm
from .models import Student



def register(request):
    if request.method == 'POST':
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = StudentRegistrationForm()
    return render(request, 'students/register.html', {'form': form})
