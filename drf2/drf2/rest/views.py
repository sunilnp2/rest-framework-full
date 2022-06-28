from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return HttpResponse("hello World")



# drf start with api view
from rest.serializers import *
from rest.models import *
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView



class StudList(ListAPIView):
    queryset = Information.objects.all()
    serializer_class = InfoSerializer

class StudListCreate(ListCreateAPIView):
    queryset = Information.objects.all()
    serializer_class = InfoSerializer

class InfoRUD(RetrieveUpdateDestroyAPIView):
    queryset = Information.objects.all()
    serializer_class = InfoSerializer
