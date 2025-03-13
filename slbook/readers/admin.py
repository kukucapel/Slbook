from django.contrib import admin
from .models import *

class MainPageServiceListInline(admin.TabularInline):
    fk_name = 'main_page_fk'
    model = MainPageServiceList

@admin.register(MainPageService)
class MainPageServiceAdmin(admin.ModelAdmin):
    inlines = [MainPageServiceListInline,]
    list_display = ['main_title', 'top_title', 'main_text', 'list_title']