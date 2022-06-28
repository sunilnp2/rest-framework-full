from functools import partial
from django.shortcuts import render
from rest.serializers import StudSerializer
from rest.models import Stud
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView

# Create your views here.

# start code from here seperately --------------------------------------------

class StudList(ListAPIView):
    queryset = Stud.objects.all()
    serializer_class = StudSerializer

class StudCreate(CreateAPIView):
    queryset = Stud.objects.all()
    serializer_class  = StudSerializer
    

class StudRetrive(RetrieveAPIView):
    queryset = Stud.objects.all()
    serializer_class = StudSerializer

class StudUpdate(UpdateAPIView):
    queryset = Stud.objects.all()
    serializer_class = StudSerializer


class StudDestroy(DestroyAPIView):
    queryset = Stud.objects.all()
    serializer_class = StudSerializer


# mixed List&CreateAPI View which don't required pk-----------------------------------------
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView

class StudListCreate(ListCreateAPIView):
    queryset = Stud.objects.all()
    serializer_class = StudSerializer

class StudRUD(RetrieveUpdateDestroyAPIView):
    queryset = Stud.objects.all()
    serializer_class = StudSerializer


# api using class method
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class StudAPI(APIView):
    def get(self, request, pk = None, format = None):
        # id = pk
        # if id is not None:
        #     stu = Stud.objects.get(id = id)
        #     serializer = StudSerializer(stu)
        #     return Response(serializer.data)

        # stu = Stud.objects.all()
        # serializer = StudSerializer(stu)
        # return Response(serializer.data)
        try:
            id = pk
            stu = Stud.objects.get(id = id)

        except :
            return Response(status= status.HTTP_404_NOT_FOUND)
        serializer = StudSerializer(stu)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request,format = None):
        data = request.data
        serializer = StudSerializer(data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Created'}, status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    # def update

        
        



