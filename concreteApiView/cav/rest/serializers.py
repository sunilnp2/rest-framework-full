from rest_framework import serializers
from rest.models import Stud

class StudSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stud
        fields = ['name', 'age', 'city']