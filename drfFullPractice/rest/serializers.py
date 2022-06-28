# from dataclasses import field
from rest.models import *
from rest_framework import serializers
# from rest_framework.serializers import Serializer



class StudSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Stud
        fields = ['id', 'url','name', 'age', 'city']


class SongSerialization(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Song
        fields = ['id','url', 'title', 'duration']

# class SingerSerialization(serializers.ModelSerializer):
#     class Meta:
#         model = Singer
#         fields = ['id','name', 'age', 'song'] 

# for hyperlinked model Serializer---------------------------------------------------------
class SingerSerialization(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Singer
        fields = ['id','name','age'] 
        

    
