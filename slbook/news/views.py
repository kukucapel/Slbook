from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponsePermanentRedirect
from .models import *
from main.models import *
from django.utils import timezone

def showRightPanel():
    rightNews_array = RightMenuLinks.objects.all()
    return rightNews_array


def main(request, number_page = 1):
    count_news_on_page = Setting.objects.all()[0].value
    count_numbers_of_list = Setting.objects.all()[1].value
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

        minus = 0
        plus = 0

        if number_page != 1:
            minus = number_page - 1

        if number_page != (count_page):
            plus = number_page + 1 
        if count_page >= 7:

            if number_page <= 3:
                pages_section = pages[0:count_numbers_of_list]
            elif number_page >= count_page - 3:
                pages_section = pages[count_page-7:count_page]
            else:
                pages_section = pages[number_page-4:number_page+3]
        else:
            pages_section = pages

        if articles_all.count() % count_news_on_page == 0 or articles_all.count() > count_news_on_page:

            articles = articles_all[articles_all.count() - (count_news_on_page * number_page):articles_all.count() - (count_news_on_page * (number_page - 1))]

        else:
            if number_page != count_page:
                articles = articles_all[articles_all.count() - (count_news_on_page * number_page):articles_all.count() - (count_news_on_page * (number_page - 1))]
            else:
                articles = articles_all[0:articles_all.count() - count_news_on_page * (number_page - 1)]
        return render(request, 'index_news.html', {"articles":articles, "current_date":current_date,"count_page":count_page, "pages":pages_section, "rightNews": showRightPanel(), "minus": minus, "plus":plus, "last":count_page, "current_page":number_page})

    return render(request, 'index_news.html', {"articles":articles_all, "current_date":current_date, "rightNews": showRightPanel()})

def show_post(request, post_id = None):
    articles = News.objects.get(id = post_id)
    print(articles.date_new)
    print(articles.article_text)
    current_date = timezone.now()
    return render(request, 'index_news.html', {"articles":articles, "post_id":post_id, "current_date": current_date, "rightNews": showRightPanel()})