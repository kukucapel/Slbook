from django.shortcuts import render
from django.http import HttpResponsePermanentRedirect
from .models import *
from abc import ABC
import re

ALL_NAME_PART = ["pastime", "services", "rules", "facilities", "links"]

class ElementClass(ABC): # основные поля
    el_type = None
    el_value = None
    el_list = None
    
    def view_all_field(self):
        print("Type: ", self.el_type)
        if self.el_value != None:
            print("Value: ", self.el_value)
        if self.el_list != None:
            print("List: ", self.el_list)
    
    def check_any_children(self, elementParent, elentChildren): # проверка, есть ли у родительского элемента элементы в другой таблице
        if elentChildren.objects.filter(id_element = elementParent.id):
            return True
        else:
            return False


class ElementServiceClass(ElementClass):

    tags_in_text = ["$a:","$b", "$c", "$bc"] # a - ссылка, b - болд, c - курсив, bc - болд курсив

    def __init__(self, elementService):
        self.ident_type(elementService)

    def ident_type(self, elementService):
        if elementService.title != None:
            self.el_type = "title"
            self.el_value = elementService.title
        elif elementService.text != '':
            self.el_type = "text"
            self.text_conversion(elementService.text)
        elif self.check_contact(elementService):
            self.el_type = "contact"
            self.el_list = [None, None, None, None, None]
            if elementService.contact_title != None:
                self.el_list[0] = elementService.contact_title
            if elementService.contact_phone != None:
                self.el_list[1] = elementService.contact_phone
            if elementService.contact_form != None:
                self.el_list[2] = elementService.contact_form
            if elementService.contact_form_href != None:
                self.el_list[3] = elementService.contact_form_href
            if elementService.contact_email != None:
                self.el_list[4] = elementService.contact_email
        elif elementService.list_title != None or self.check_any_children(elementService, ServiceList):
            self.el_type = 'list'
            if elementService.list_title != None:
                self.el_value = elementService.list_title
            self.el_list = ServiceList.objects.filter(id_element = elementService.id)
    
    def text_conversion(self, serviceText):
        #self.el_value = serviceText.replace(r"%a:", "FUCK")
        #print(re.sub(r"!a:(.)*!", "FUCK", serviceText))
        #print(re.sub(r"!bc:(.)*!", "FUCK", serviceText))
        #print(self.el_value)
        self.el_value = serviceText
        while "!a:" in self.el_value:
            temp = re.search(r'!a:(.)*\s(.)*\s!', self.el_value)
            
            temp = temp.group(0)
            temp = re.split(' ', temp, 2)
            temp = "<a href = '" + temp[1] + " ' target = '_blank' + class = 'a_info'>" + temp[2][0:-2] + "</a>"
            #print(temp)
            self.el_value = (re.sub(r'!a:(.)*\s(.)*\s!', temp, self.el_value))
            #print(self.el_value)

    def check_contact(self, elementService):
        if elementService.contact_title != None or elementService.contact_phone != None or elementService.contact_form != None or elementService.contact_form_href != None or elementService.contact_email != None:
            return True
        else:
            return False


def main(request, name_part = "pastime"):
    print(name_part)
    if name_part in ALL_NAME_PART:
        if name_part == "services":
            
            return render(request, 'index_readers.html', {"name_part":name_part, 
                                                          "number_part":0, 
                                                          "main_sevice_content":MainPageService.objects.all()[0], 
                                                          "main_service_list":MainPageServiceList.objects.filter(main_page_fk = 1)})
        else:
            return render(request, 'index_readers.html', {"name_part":name_part})
    else:
        return(HttpResponsePermanentRedirect("/"))

def services(request, number_part = 1):
    print(number_part)
    elem = []
    if number_part >= 1 and number_part <= 10:
        for element in ServiceElement.objects.filter(main_page_service_list_fk = number_part).order_by('priority'):
            elem.append(ElementServiceClass(element))
        for el in elem:
            if el.el_type == "contact":
                for l in el.el_list:
                    print(l)
        return render(request, 'index_readers.html', 
                      {"name_part":"services",
                       "number_part":number_part, 
                       "name_service":MainPageServiceList.objects.filter(id = number_part)[0].service,
                       "element":elem,
                       "test":"<a href='/'>FUCK</a> Your mom",
                       "main_sevice_content":MainPageService.objects.all()[0]},
                       )
    else:
        return(HttpResponsePermanentRedirect("/"))