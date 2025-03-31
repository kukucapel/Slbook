from django.contrib import admin
from .models import *

class MainPageServiceListInline(admin.TabularInline):
    fk_name = 'main_page_fk'
    model = MainPageServiceList

@admin.register(MainPageService)
class MainPageServiceAdmin(admin.ModelAdmin):
    inlines = [MainPageServiceListInline,]
    list_display = ['main_title', 'top_title', 'main_text', 'list_title']

class ServiceListInline(admin.TabularInline):
    fk_name = "id_element"
    model = ServiceList

@admin.register(ServiceElement)
class ServiceElementAdmin(admin.ModelAdmin):
    inlines = [ServiceListInline,]
    list_display = ['main_page_service_list_fk', 'priority', 'title', 'text', 'list_title', 'contact_title']