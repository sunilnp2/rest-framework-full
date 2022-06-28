from django.contrib import admin
from .models import *
# Register your models here.

class StudAdmin(admin.ModelAdmin):
    list_display = ['id','name', 'age', 'city']
    ordering = ['id']
admin.site.register(Stud, StudAdmin)
