from django.contrib import admin
from models import *

# Register your models here.

class ArticlesAdmin(admin.ModelAdmin):
    list_display = ['title','pk']

admin.site.register(Articles,ArticlesAdmin)

class LiveAdmin(admin.ModelAdmin):
    list_display = ['title','id']

admin.site.register(Life,LiveAdmin)