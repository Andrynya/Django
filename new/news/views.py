from django.shortcuts import render
from .models import News_post

# Create your views here.
def dom(request):
    news = News_post.objects.all()
    return render(request, 'news/news.html', {'news': news})