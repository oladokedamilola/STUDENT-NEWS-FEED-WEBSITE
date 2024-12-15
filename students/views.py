from django.shortcuts import render, redirect,  get_object_or_404
from .forms import StudentRegistrationForm
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import *
from .models import *
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test
from notifications.models import *



CustomUser = get_user_model()

def register(request, matric_number):
    try:
        student_data = PreRegisteredStudent.objects.get(matric_number=matric_number)
    except PreRegisteredStudent.DoesNotExist:
        messages.error(request, 'Invalid matriculation number.')
        return redirect('home')

    if request.method == 'POST':
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            phone_number = form.cleaned_data['phone_number']
            email = form.cleaned_data['email']

            if CustomUser.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists. Please choose a different username.')
            else:
                # Create a new CustomUser instance
                user = CustomUser.objects.create_user(username=username, password=password, email=email)
                print(f"Created user: {user}")

                # Create a new Student instance
                new_student = Student(
                    user=user,
                    matric_number=matric_number,
                    full_name=f"{student_data.first_name} {student_data.last_name}",
                    department=student_data.department,
                    phone_number=phone_number,
                    email=email,
                    gender=student_data.gender,
                )
                new_student.save()
                print(f"Created student: {new_student}")

                messages.success(request, 'Registration successful. Please log in.')
                return redirect('student:login')
        else:
            messages.error(request, 'Registration failed. Please check the form.')
    else:
        form = StudentRegistrationForm()

    return render(request, 'students/register.html', {'form': form, 'student_data': student_data})


@user_passes_test(lambda u: u.is_staff)
def update_user_profile(request, user_id):
    unseen_notifications_count = request.user.notifications.filter(is_read=False).count()
    user = get_object_or_404(CustomUser, id=user_id)
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('profile', user_id=user.id)
    else:
        form = UserProfileForm(instance=user)
    return render(request, 'students/update_user_profile.html', {'form': form, 'unseen_notifications_count': unseen_notifications_count})



def verify_matric_number(request):
    if request.method == 'POST':
        form = MatricNumberForm(request.POST)
        if form.is_valid():
            matric_number = form.cleaned_data['matric_number']
            try:
                # Check if the student is already registered
                if Student.objects.filter(matric_number=matric_number).exists():
                    form.add_error('matric_number', 'This matric number has already been registered')
                else:
                    # Check if the student is pre-registered
                    student = PreRegisteredStudent.objects.get(matric_number=matric_number)
                    return redirect('student:register', matric_number=matric_number)
            except PreRegisteredStudent.DoesNotExist:
                form.add_error('matric_number', 'Matric number not found')
    else:
        form = MatricNumberForm()
    return render(request, 'students/verify_matric_number.html', {'form': form})





def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            print(f"Username: {username}, Password: {password}")  # Debug statement
            
            # Authenticate user
            user = authenticate(request, username=username, password=password)
            print(user)  # Debug statement
            
            if user is not None:
                login(request, user)
                print("User logged in successfully.")  # Debug statement
                return redirect('student:profile')  # Replace with your actual dashboard URL
            else:
                messages.error(request, 'Invalid login credentials.')
                print("Authentication failed.")  # Debug statement
        else:
            messages.error(request, 'Invalid login credentials.')
            print("Form is not valid.")  # Debug statement
    else:
        form = LoginForm()

    return render(request, 'students/login.html', {'form': form})


@login_required
def profile(request):
    unseen_notifications_count = request.user.notifications.filter(is_read=False).count()
    return render(request, 'students/profile.html', {'unseen_notifications_count': unseen_notifications_count})

def logout_view(request):
    logout(request)
    return redirect('student:login')



@login_required
def edit_profile(request):
    unseen_notifications_count = request.user.notifications.filter(is_read=False).count()
    if request.method == 'POST':
        user_form = UserProfileForm(request.POST, instance=request.user)
        student_form = StudentProfileForm(request.POST, request.FILES, instance=request.user.student)

        if user_form.is_valid() and student_form.is_valid():
            user_form.save()
            student_form.save()
            return redirect('student:profile')
    else:
        user_form = UserProfileForm(instance=request.user)
        student_form = StudentProfileForm(instance=request.user.student)

    return render(request, 'students/edit_profile.html', {
        'user_form': user_form,
        'student_form': student_form,
        'unseen_notifications_count': unseen_notifications_count
    })
