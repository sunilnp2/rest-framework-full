from django.contrib import admin
from rest.models import *
# Register your models here.
class DogAdmin(admin.ModelAdmin):
    list_display = ['name', 'age', 'color', 'height']
admin.site.register(Dog, DogAdmin)