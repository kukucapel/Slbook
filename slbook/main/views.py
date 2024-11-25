from django.shortcuts import render
from django.http import HttpResponse
from .models import *

def main(request):
    articles = News.objects.all()
    
    return render(request, 'index.html', {"articles":articles})
def show_post(request, post_id = None):
    articles = News.objects.get(id = post_id)

    return render(request, 'index.html', {"articles":articles, "post_id":post_id})