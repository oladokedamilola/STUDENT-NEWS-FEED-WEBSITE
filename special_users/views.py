from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.utils import timezone
from django.contrib.auth.models import Group
from .forms import CreatorApplicationForm
from .models import CreatorApplication

@login_required
def apply_creator(request):
    if request.method == 'POST':
        form = CreatorApplicationForm(request.POST)
        if form.is_valid():
            application = form.save(commit=False)
            application.user = request.user
            application.save()
            return redirect('news:news_list')
    else:
        form = CreatorApplicationForm()
    return render(request, 'special_users/apply_creator.html', {'form': form})

@user_passes_test(lambda u: u.is_superuser)
def review_applications(request):
    applications = CreatorApplication.objects.filter(approved=False)
    return render(request, 'special_users/review_applications.html', {'applications': applications})

@user_passes_test(lambda u: u.is_superuser)
def approve_application(request, application_id):
    application = get_object_or_404(CreatorApplication, id=application_id)
    application.approved = True
    application.reviewed_at = timezone.now()
    application.reviewed_by = request.user
    application.save()
    
    user = application.user
    # Add user to creator group or update permissions
    creator_group, created = Group.objects.get_or_create(name='Content Creator')
    user.groups.add(creator_group)
    
    return redirect('review_applications')
