from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponsePermanentRedirect
from django.utils import timezone
from .models import *
from abc import ABC

# Идея заключается в создании массива объектов класса
# Нужного раздела и последующей отправке оного в шаблон
#
# Изначально класс имеет три поля:
#                     1) Поле с типом элемента (el_type)
#                     2) Поле с единичным значением (el_value)
#                     3) Поле со списком (el_list)
# 



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
        if elentChildren.objects.filter(id_element = elementParent.id_element):
            return True
        else:
            return False

class ElementHistoryClass(ElementClass): # для истории
 
    def ident_type(self, elementHistory):
        if elementHistory.title != None:
            self.el_type = "title"
            self.el_value = elementHistory.title
        
        elif elementHistory.text != '':
            self.el_type = "text"
            self.el_value = elementHistory.text 
        
        elif elementHistory.title_list != None or elementHistory.text_list != '':
            self.el_type = "list"
            if elementHistory.title_list != None:
                self.el_value = elementHistory.title_list
            self.el_list = elementHistory.text_list
        
        elif elementHistory.title_img != None or self.check_any_children(elementHistory, HistoryImage):
            self.el_type = "img"
            if elementHistory.title_img != None:
                self.el_value = elementHistory.title_img
            self.el_list = HistoryImage.objects.filter(id_element = elementHistory.id_element)

    
    def __init__(self, elementHistory):
        self.ident_type(elementHistory)
    

class ElementStructureClass(ElementClass): # для структуры

    el_type_block = None

    def ident_type(self, elementStructure):
        if elementStructure.title_h != None:
            self.el_type = 'title_h'
            self.el_value = elementStructure.title_h
        
        elif elementStructure.title_l != None:
            self.el_type = 'title_l'
            self.el_value = elementStructure.title_l
        
        elif elementStructure.text != '':
            self.el_type = 'text'
            self.el_value = elementStructure.text

        elif elementStructure.list_title != None or self.check_any_children(elementStructure, StructureList):
            self.el_type = 'list'
            if elementStructure.list_title != None:
                self.el_value = elementStructure.list_title
            self.el_list = StructureList.objects.filter(id_element = elementStructure.id_element)

        elif elementStructure.quote != None or elementStructure.quote_author != None:
            self.el_type = 'quote'
            self.el_value = elementStructure.quote
            self.el_list = elementStructure.quote_author

        elif elementStructure.contact_post != None or elementStructure.contact_name != None or elementStructure.contact_phone != None or elementStructure.contact_email != None:
            self.el_type = 'contact'
            self.el_list = [None, None, None, None]
            if elementStructure.contact_post != None:
                self.el_list[0] = (elementStructure.contact_post)
            if elementStructure.contact_name != None:
                self.el_list[1] = (elementStructure.contact_name)
            if elementStructure.contact_phone != None:
                self.el_list[2] = (elementStructure.contact_phone)
            if elementStructure.contact_email != None:
                self.el_list[3] = (elementStructure.contact_email)

        else:
            self.el_type = 'img'
            if elementStructure.img_title != None:
                self.el_value = elementStructure.img_title
            self.el_list = StructureImage.objects.filter(id_element = elementStructure.id_element)

    
    def __init__(self, elementStructure):
        self.ident_type(elementStructure)
        

    def view_all_field(self):
        print("Type: ", self.el_type)
        
        if self.el_value != None:
            print("Value: ", self.el_value)
        if self.el_list != None:
            print("List: ", self.el_list)

class ElementPartnershipClass(ElementClass):

    def ident_type(self, elementPartnership):
        if elementPartnership.title != None:
            self.el_type = "title"
            self.el_value = elementPartnership.title
        
        elif elementPartnership.text != '':
            self.el_type = "text"
            self.el_value = elementPartnership.text 
        elif self.check_any_children(elementPartnership, PartnershipList):
            self.el_type = "list"
            self.el_list = PartnershipList.objects.filter(id_element = elementPartnership.id_element)
        elif self.check_any_children(elementPartnership, PartnershipAuthor):
            self.el_type = "author"
            self.el_list = PartnershipAuthor.objects.filter(id_element = elementPartnership.id_element)
        else:
            self.el_type = "img"
            if elementPartnership.img_title != None:
                self.el_value = elementPartnership.img_title
            self.el_list = PartnershipImage.objects.filter(id_element = elementPartnership.id_element)
    
    def __init__(self, elementPartnership):
        self.ident_type(elementPartnership)
        

class FileBlockClass(ElementClass):
    
    def __init__(self, elementFile):
        self.el_list = FileElement.objects.filter(id_block = elementFile.id_block)


def history(request, name_part = "history"):
    all_name_part = ["history", "structure", "documents", "partnership", "official", "media"]

    
    # array with all elements in block
    elem = []
    temp = []
    if name_part == "history":
        for block in HistoryBlock.objects.all().order_by('priority'):
            for element in HistoryElement.objects.filter(id_block = block.id_block).order_by('priority'):
                temp.append(ElementHistoryClass(element))
            elem.append(temp)
            temp = []
    elif name_part == "structure":
        for block in StructureBlock.objects.all().order_by('priority'):
            temp.append(block.type_block)
            for element in StructureElement.objects.filter(id_block = block.id_block).order_by('priority'):
                temp.append(ElementStructureClass(element))
            elem.append(temp)
            temp = []
    elif name_part == "partnership":
        for block in PartnershipBlock.objects.all().order_by('priority'):
            for element in PartnershipElement.objects.filter(id_block = block.id_block).order_by('priority'):
                temp.append(ElementPartnershipClass(element))
            elem.append(temp)
            temp = []
    elif name_part == "official":
        for block in FileBlock.objects.all().order_by('priority'):
            elem.append(FileBlockClass(block))
    elif name_part == "media":
        elem = BiblioMassMedia.objects.all().order_by('priority')
    
    
    

    


    if name_part in all_name_part:
        return render(request, 'index_about.html', {"name_part":name_part, "element":elem})
    else:
        return(HttpResponsePermanentRedirect("/"))