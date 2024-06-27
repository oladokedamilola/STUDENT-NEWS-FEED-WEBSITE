from django.shortcuts import render
from .models import NewsArticle


def news_list(request):
    articles = NewsArticle.objects.all()
    return render(request, 'news/news_list.html', {'articles': articles})
