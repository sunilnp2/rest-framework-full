from rest_framework import serializers
from drf.models import *
#  normal api drf -----------------------------------------------------------------
# class StudentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Student
#         fields = ['id','name', 'faculty', 'age', 'address']
class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['id', 'name', 'slug', 'price', 'category']

class CategorySerializer(serializers.ModelSerializer):
    # item = serializers.StringRelatedField(many = True, read_only = True, view_name='item-detail')
    item = serializers.SlugRelatedField(many = True, read_only = True, slug_field='name')
    # item = serializers.HyperlinkedRelatedField(many = True, read_only = True, view_name='item-detail')
    # item = serializers.PrimaryKeyRelatedField(many = True, read_only = True, view_name='item-detail')
    # item = ItemSerializer(many = True, read_only = True)
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug', 'item']




# serializer relation start form here -----------------------------------------------------
class StudentSerializer(serializers.HyperlinkedModelSerializer):
    # url = serializers.HyperlinkedRelatedField(many = True, view_name='student-detail', read_only = True)
    class Meta:
        model = Student
        fields = ['id', 'url', 'name', 'faculty', 'age', 'address']
