from django.urls import path
from . import views


app_name="Announcements"


urlpatterns = [
    path('', views.announcement_list, name='announcements'),
    path('<int:pk>/', views.announcement_detail, name='announcement_detail'),
    path('create/', views.create_announcement, name='create'),
]

