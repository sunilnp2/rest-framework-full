from multiprocessing import AuthenticationError
from django.shortcuts import render
from rest.models import *
from rest.serializers import *
from rest_framework.response import Response
from rest_framework import serializers
# Create your views here.
from rest_framework import viewsets
from rest_framework import status

class DogViewSet(viewsets.ViewSet):
    def list(self,request):
        stu = Dog.objects.all()
        serializers = DogSerializer(stu, many = True)
        return Response(data = serializers.data, status=status.HTTP_200_OK)

    def retrive(self, request, pk):
        id = pk
        if id is not None:
            stu = Dog.objects.get(id = id)
            serializers = DogSerializer(stu)
            return Response(data = serializers.data, status=status.HTTP_200_OK)

    def create(self, request):
            serializers = DogSerializer(request.data)
            if serializers.is_valid():
                serializers.save()
                return Response({'msg':'Data Created'})
            return Response(serializers.errors)

    def update(self, request, pk):
        id = pk
        stu = Dog.objects.get(id = id)
        serializers = DogSerializer(stu, request.data)
        if serializers.is_valid():
            serializers.save()
            return Response({'msg':'Data Updated'})
        return Response(serializers.errors)

    def delete(self, request, pk):
        id = pk
        stu = Dog.objects.get(id = id)
        stu.delete()

# note---------------------------------------------------------------------------
# -----hamile Authentication ra Permission use garna pahile import chai garna perx----------
# Model ViewSet Start From here
from rest_framework.authentication import BasicAuthentication,SessionAuthentication,TokenAuthentication,RemoteUserAuthentication
from rest_framework.permissions import IsAdminUser, AllowAny, IsAuthenticated, DjangoModelPermissions, DjangoModelPermissionsOrAnonReadOnly, DjangoObjectPermissions

class DogModelViewSet(viewsets.ModelViewSet):
    queryset = Dog.objects.all()
    serializer_class = DogSerializer
    # authentication_classes = [BasicAuthentication]
    authentication_classes = [SessionAuthentication]

    # permission_classes = [AllowAny]-  sabai le herna pauxa
    # permission_classes = [IsAuthenticated] - authenticated user login gareko le matra herna pauxa 
    # permission_classes = [IsAdminUser] -- admin ra staff le matra herna pauxa 
    # permission_classes = [DjangoModelPermissions]
    # -- DjangoModelPermissions ma backend ma admin le kk permission deko xa tahi matra garna pauxa
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
    # esma login user lai kk garna oermission chayenxa ra login na vako user le data herna pauxa
    # permission_classes = [DjangoObjectPermissions] - yo model ahile develop vako xaina



# class DogReadOnlyViewSet(viewsets.ReadOnlyModelViewSet):
#     queryset = Dog.objects.all()
#     serializer_class = DogSerializer
#     authentication_classes = [BasicAuthentication]
#     permission_classes = [IsAuthenticated]

    
        