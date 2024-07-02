from django.shortcuts import render, redirect
from .forms import StudentRegistrationForm
from django.contrib.auth import logout, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserChangeForm
from .forms import *
from .models import *
from django.contrib.auth import authenticate, login



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



def register(request, matric_number):
    try:
        student_data = PreRegisteredStudent.objects.get(matric_number=matric_number)
    except PreRegisteredStudent.DoesNotExist:
        return redirect('student:verify_matric_number')

    if request.method == 'POST':
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.full_name = f"{student_data.first_name} {student_data.last_name}"
            user.matric_number = matric_number
            user.faculty = student_data.faculty
            user.department = student_data.department
            user.gender = student_data.gender

            # Debugging: Print faculty to console
            print(f"Faculty: {user.faculty}")

            # Check if faculty is valid
            valid_faculties = [choice[0] for choice in Student.FACULTY_CHOICES]
            if user.faculty not in valid_faculties:
                form.add_error('faculty', 'Faculty is not valid')
                context = {
                    'form': form,
                    'student_data': student_data,
                }
                return render(request, 'students/register.html', context)

            user.save()
            login(request, user)
            return redirect('home')
    else:
        form = StudentRegistrationForm()

    context = {
        'form': form,
        'student_data': student_data,
    }
    return render(request, 'students/register.html', context)



def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                form.add_error(None, 'Invalid username or password')
    else:
        form = LoginForm()
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
