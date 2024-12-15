from django.shortcuts import render, get_object_or_404
from .models import *
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import *
from django.core.paginator import Paginator
from students.models import *
from notifications.utils import create_notification
from notifications.models import *
from django.contrib.sites.shortcuts import get_current_site


@login_required
def news_list(request):
    news_items = News.objects.all()
    categories = Category.objects.all()
    unseen_notifications_count = request.user.notifications.filter(is_read=False).count()
    
    paginator = Paginator(news_items, 5)  # Show 5 news items per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'news/news_list.html', {
        'page_obj': page_obj, 
        'categories': categories,
        'unseen_notifications_count': unseen_notifications_count
    })


@login_required
def category_news_list(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    news_items = News.objects.filter(category=category)
    categories = Category.objects.all()
    unseen_notifications_count = request.user.notifications.filter(is_read=False).count()
    return render(request, 'news/category_news_list.html', {'news_items': news_items, 'categories': categories, 'category': category, 'unseen_notifications_count': unseen_notifications_count})

@login_required
def create_news(request):
    if request.method == 'POST':
        form = NewsForm(request.POST, request.FILES)
        if form.is_valid():
            news_item = form.save(commit=False)
            news_item.author = request.user
            news_item.save()
            return redirect('news:news_list')
    else:
        form = NewsForm()
    return render(request, 'news/create_news.html', {'form': form})



@login_required
def news_detail(request, pk):
    news = get_object_or_404(News, pk=pk)
    comments = news.comments.all()
    unseen_notifications_count = request.user.notifications.filter(is_read=False).count()

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.user = request.user
            comment.news = news
            comment.save()

            # Notify the author of the post about the new comment
            if news.author != request.user:
                post_url = request.build_absolute_uri(reverse('news:news_detail', kwargs={'pk': news.pk}))
                create_notification(news.author, f"You have a new comment on your post: '{news.title}'", 'comment', post_url)

            return redirect('news:news_detail', pk=news.id)
    else:
        comment_form = CommentForm()
    
    context = {
        'news_item': news,
        'comments': comments,
        'comment_form': comment_form,
        'categories': Category.objects.all(),
        'unseen_notifications_count': unseen_notifications_count
    }
    return render(request, 'news/news_detail.html', context)


@login_required
def like_news(request, news_id):
    news = get_object_or_404(News, id=news_id)
    like, created = Like.objects.get_or_create(user=request.user, news=news)
    
    if not created:
        like.delete()
    
    # Notify the author of the post about the new like
    if news.author != request.user:
        if created:
            create_notification(news.author, f"Your post: '{news.title}' has a new like!", 'like', post_url=request.build_absolute_uri(news.get_absolute_url()))
    
    return redirect('news:news_detail', pk=news_id)


