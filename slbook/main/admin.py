from django.contrib import admin
from .models import *

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_new')

@admin.register(Setting)
class SettingAdmin(admin.ModelAdmin):
    list_display = ('title', 'value')

@admin.register(RightMenuLinks)
class RightMenuLinksAdmin(admin.ModelAdmin):
    list_display = ('title', 'priority')
