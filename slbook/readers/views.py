from django.shortcuts import render
from django.http import HttpResponsePermanentRedirect


# Create your views here.
def main(request, name_part = "pastime"):
    all = ["pastime", "services", "rules", "rehabilitation ", "links"]
    if name_part in all:
        return render(request, 'index_readers.html', {"name_part":name_part})
    else:
        return(HttpResponsePermanentRedirect("/"))