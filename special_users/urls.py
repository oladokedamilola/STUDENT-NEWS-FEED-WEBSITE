from django.urls import path
from . import views

app_name="special_users"


urlpatterns = [
    path('apply/', views.apply_creator, name='apply_creator'),
    path('applications/', views.review_applications, name='review_applications'),
    path('applications/approve/<int:application_id>/', views.approve_application, name='approve_application'),
]
