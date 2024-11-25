from django.shortcuts import render
from .models import *
# Create your views here.
def main(request):
    articles = News.objects.all()
    
    return render(request, 'index.html', {"articles":articles})