from django.urls import path
from . import views

app_name = 'special_users'

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('register/', views.register, name='register'),
    path('login/', views.SpecialUserLoginView.as_view(), name='login'),
    path('verify/<uuid:token>/', views.verify_email, name='verify'),
]
