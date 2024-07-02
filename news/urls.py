from django.urls import path
from . import views

app_name = 'news'

urlpatterns = [
    path('', views.news_list, name='news_list'),
    path('<int:pk>/', views.news_detail, name='news_detail'),
    path('category/<int:category_id>/', views.category_news_list, name='category_news_list'),
    path('create/', views.create_news, name='create'),
]



