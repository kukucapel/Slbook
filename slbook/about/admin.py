from django.contrib import admin
from django.db.models import Count
from .models import *

#admin block history

class HistoryImageInline(admin.TabularInline):
    fk_name = 'id_element'
    model = HistoryImage

class HistoryElementInline(admin.TabularInline):
    fk_name = 'id_block'
    model = HistoryElement

@admin.register(HistoryElement)
class HistoryElementAdmin(admin.ModelAdmin):
    inlines = [HistoryImageInline,]
    list_display = ['id_block','priority', 'title', 'text', 'title_list', 'text_list', 'title_img']

@admin.register(HistoryBlock)
class HistoryBlockAdmin(admin.ModelAdmin):
    list_display = ('id_block', 'priority')



#admin block structure

class StructureImageInline(admin.TabularInline):
    fk_name = 'id_element'
    model = StructureImage

class StructureListInline(admin.TabularInline):
    fk_name = 'id_element'
    model = StructureList

@admin.register(StructureElement)
class StructureElementAdmin(admin.ModelAdmin):
    inlines = [StructureListInline, StructureImageInline,]
    list_display = ['id_block', 'priority', 'title_h', 'title_l', 'text', 'list_title', 'contact_name']

@admin.register(StructureBlock)
class StructureBlockAdmin(admin.ModelAdmin):
    list_display = ('id_block', 'priority', 'type_block')