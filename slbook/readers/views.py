from django.shortcuts import render
from django.http import HttpResponsePermanentRedirect


# Create your views here.
def main(request, name_part = "pastime"):
    print(name_part)
    all = ["pastime", "services", "rules", "facilities", "links"]
    if name_part in all:
        return render(request, 'index_readers.html', {"name_part":name_part, "number_part":0})
    else:
        return(HttpResponsePermanentRedirect("/"))

def services(request, number_part = 1):
    print(number_part)
    if number_part >= 1 and number_part <= 10:
        return render(request, 'index_readers.html', {"name_part":"services","number_part":number_part})
    else:
        return(HttpResponsePermanentRedirect("/"))