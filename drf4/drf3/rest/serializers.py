from dataclasses import field
from rest.models import Dog
from rest_framework import serializers


class DogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dog
        fields = ['name','age', 'color', 'height']