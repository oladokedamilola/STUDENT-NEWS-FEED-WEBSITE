from django.urls import path
from .views import *

app_name="student"


urlpatterns = [
    path('login/', login_view, name='login'),
    path('profile/', profile, name='profile'),
    path('logout/', logout_view, name='logout'),
    path('edit_profile/', edit_profile, name='edit_profile'),
    path('verify/', verify_matric_number, name='verify_matric_number'),
    path('register/<str:matric_number>/', register, name='register'),
]
