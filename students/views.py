from django.shortcuts import render, redirect
from .forms import StudentRegistrationForm
from django.contrib.auth import logout, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserChangeForm



def register(request):
    if request.method == 'POST':
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            student = form.save(commit=False)
            student.set_password(form.cleaned_data['password'])
            student.save()
            return redirect('success_url')  # replace 'success_url' with your success URL
    else:
        form = StudentRegistrationForm()
    return render(request, 'students/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('Student:profile')
    else:
        form = AuthenticationForm()
    return render(request, 'students/login.html', {'form': form})


@login_required
def profile(request):
    return render(request, 'students/profile.html')

def logout_view(request):
    logout(request)
    return redirect('Student:login')



@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = UserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('Student:profile')
    else:
        form = UserChangeForm(instance=request.user)
    
    return render(request, 'students/edit_profile.html', {'form': form})
