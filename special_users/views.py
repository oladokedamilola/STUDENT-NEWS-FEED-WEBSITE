from django.shortcuts import render, redirect, get_object_or_404, redirect
from django.contrib.auth import login
from .forms import *
from django.contrib.auth.views import LoginView
from django.core.mail import send_mail
from django.urls import reverse
from .models import *
from django.contrib.auth.decorators import login_required


class SpecialUserLoginView(LoginView):
    template_name = 'special_users/login.html'


def register(request):
    if request.method == 'POST':
        form = SpecialUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_verified = False  # Set user as not verified initially
            user.save()

            verification_link = request.build_absolute_uri(
                reverse('special_users:verify', kwargs={'token': user.verification_token})
            )
            send_mail(
                'Verify your email address',
                f'Please verify your email by clicking the following link: {verification_link}',
                'noreply@example.com',
                [user.email],
            )
            
            login(request, user)
            return redirect('home')
    else:
        form = SpecialUserCreationForm()
    return render(request, 'special_users/register.html', {'form': form})


def verify_email(request, token):
    user = get_object_or_404(SpecialUser, verification_token=token)
    user.is_verified = True
    user.verification_token = None  # Clear the token once used
    user.save()
    return redirect('special_users:login')



@login_required
def dashboard(request):
    if not request.user.is_special_user:
        return redirect('home')
    return render(request, 'special_users/dashboard.html')

