from django.shortcuts import render
from django.http import HttpResponsePermanentRedirect
from .models import *

# Create your views here.
def main(request, name_part = "pastime"):
    print(name_part)
    all_name_part = ["pastime", "services", "rules", "facilities", "links"]
    if name_part in all_name_part:
        if name_part == "services":
            
            return render(request, 'index_readers.html', {"name_part":name_part, "number_part":0, "main_sevice_content":MainPageService.objects.all()[0], "main_service_list":MainPageServiceList.objects.filter(main_page_fk = 1)})
        else:
            return render(request, 'index_readers.html', {"name_part":name_part})
    else:
        return(HttpResponsePermanentRedirect("/"))

def services(request, number_part = 1):
    print(number_part)
    if number_part >= 1 and number_part <= 10:
        return render(request, 'index_readers.html', {"name_part":"services","number_part":number_part, "name_service":MainPageServiceList.objects.filter(id = number_part)[0].service, "test":"<a href='/'>FUCK</a> Your mom"})
    else:
        return(HttpResponsePermanentRedirect("/"))