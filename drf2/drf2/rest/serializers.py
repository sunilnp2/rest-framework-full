from dataclasses import fields
from rest_framework import serializers
from rest.models import *

class InfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Information
        fields = ['name', 'age', 'add', 'qualification']