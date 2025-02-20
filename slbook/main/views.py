from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponsePermanentRedirect
from .models import *
from news.models import News
from django.utils import timezone

def showRightPanel():
    rightNews_array = RightMenuLinks.objects.all()
    return rightNews_array

def index(request):
    current_date = timezone.now()
    articles_all = News.objects.all()
    article_preview = []
    count_articles = 0
    for i in reversed(articles_all):
        if i.date_new <= current_date and count_articles != 3:
            article_preview.append(i)
            count_articles += 1
    
    return render(request, 'index_main.html', {"rightNews": showRightPanel(), "article_preview":article_preview})