from django import views
from django.shortcuts import render
from drf.serializers import *
from drf.models import *
from rest_framework import viewsets
from drf.mypaginations import *
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
# Create your views here.

class StudModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class CategoryModelViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = MyCursorPagination
    # filter_backends = [DjangoFilterBackend]
    # filterset_fields = ['name']
    filter_backends = [SearchFilter]
    search_fields = ['name']


class ItemModelViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
