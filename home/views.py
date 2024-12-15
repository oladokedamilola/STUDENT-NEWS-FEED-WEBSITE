from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from news.views import *
def index(request):
    if request.user.is_authenticated:
        return redirect('news:news_list')  
    return render(request, 'home/index.html')
