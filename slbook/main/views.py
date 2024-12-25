from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponsePermanentRedirect
from .models import *
from django.utils import timezone


def index(request):
    return(HttpResponsePermanentRedirect("/page/1"))
def main(request, number_page = 1):
    count_news_on_page = Setting.objects.all()[0].count_news_on_page
    articles_all = News.objects.all()
    current_date = timezone.now()
    if articles_all.count() > count_news_on_page:
        pages = []
        if articles_all.count() % count_news_on_page != 0:
            count_page = (articles_all.count() // count_news_on_page) + 1
        else:
            count_page = articles_all.count() // count_news_on_page
        for i in range(1,count_page + 1):
            pages.append(i)
        if articles_all.count() % count_news_on_page == 0:
            articles = articles_all[articles_all.count() - (count_news_on_page * number_page):articles_all.count() - (count_news_on_page * (number_page - 1))]
        else:
            if number_page != count_page:
                articles = articles_all[articles_all.count() - (count_news_on_page * number_page):articles_all.count() - (count_news_on_page * (number_page - 1))]
            else:
                articles = articles_all[0:articles_all.count() - count_news_on_page * (number_page - 1)]
        return render(request, 'index.html', {"articles":articles, "current_date":current_date,"count_page":count_page, "pages":pages})

    return render(request, 'index.html', {"articles":articles_all, "current_date":current_date})

def show_post(request, post_id = None):
    articles = News.objects.get(id = post_id)
    print(articles.date_new)
    current_date = timezone.now()
    return render(request, 'index.html', {"articles":articles, "post_id":post_id, "current_date": current_date})