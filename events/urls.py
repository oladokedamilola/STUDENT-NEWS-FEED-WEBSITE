from django.urls import path
from . import views


app_name="Event"


urlpatterns = [
    path('', views.event_list, name='event'),
]