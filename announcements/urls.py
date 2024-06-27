from django.urls import path
from . import views


app_name="Announcements"


urlpatterns = [
    path('', views.announcement_list, name='announcements'),
]
