from django.shortcuts import render, get_object_or_404
from .models import News, Category
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import NewsForm


def news_list(request):
    news_items = News.objects.all()
    categories = Category.objects.all()
    return render(request, 'news/news_list.html', {'news_items': news_items, 'categories': categories})

def news_detail(request, pk):
    news_item = get_object_or_404(News, pk=pk)
    return render(request, 'news/news_detail.html', {'news_item': news_item})

def category_news_list(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    news_items = News.objects.filter(category=category)
    categories = Category.objects.all()
    return render(request, 'news/category_news_list.html', {'news_items': news_items, 'categories': categories, 'category': category})

@login_required
def create_news(request):
    if not request.user.is_special_user:
        return redirect('home')
    if request.method == 'POST':
        form = NewsForm(request.POST)
        if form.is_valid():
            news = form.save(commit=False)
            news.author = request.user
            news.save()
            return redirect('special_users:dashboard')
    else:
        form = NewsForm()
    return render(request, 'news/create_news.html', {'form': form})
