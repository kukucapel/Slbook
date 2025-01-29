from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponsePermanentRedirect
from django.utils import timezone

def history(request, name_part = "history"):
    all = ["history", "structure", "documents", "partnership", "official", "media"]
    if name_part in all:
        return render(request, 'index_about.html', {"name_part":name_part})
    else:
        return(HttpResponsePermanentRedirect("/"))


"""
def structure(request):
    name_part = "structure"
    return render(request, 'index_about.html', {"name_part":name_part})

def documents(request):
    name_part = "documents"
    return render(request, 'index_about.html', {"name_part":name_part})

def partnership(request):
    name_part = "partnership"
    return render(request, 'index_about.html', {"name_part":name_part})

def official(request):
    name_part = "official"
    return render(request, 'index_about.html', {"name_part":name_part})
def media(request):
    name_part = "media"
    return render(request, 'index_about.html', {"name_part":name_part})
"""