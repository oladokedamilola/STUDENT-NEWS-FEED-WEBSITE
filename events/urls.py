from django.urls import path
from . import views


app_name="Event"


urlpatterns = [
    path('', views.event_list, name='event'),
    path('<int:pk>/', views.event_detail, name='event_detail'),
    path('create/', views.create_event, name='create'),
]
