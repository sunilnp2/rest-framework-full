from django.contrib import admin
from rest.models import *
# Register your models here.
class InfoAdmin(admin.ModelAdmin):
    list_display = ['id','name', 'age', 'add', 'qualification']
    
admin.site.register(Information, InfoAdmin)