from functools import partial
import queue
from rest.models import *
from django.shortcuts import render
from django.shortcuts import HttpResponse
from rest.serializers import *
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin,CreateModelMixin, RetrieveModelMixin, DestroyModelMixin, UpdateModelMixin


import rest_framework
# Create your views here.

# for renter home page
def home(request):
    return HttpResponse("Hello world")


# start rest_framework 
class GetPostAPI(GeneratorExit,ListModelMixin, CreateModelMixin):
    queryset = Stud.objects.all()
    serializers_class = StudSerializer

    def get(self, request, *args,**kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args,**kwargs):
        return self.create(request, *args, **kwargs)

class RUDAPI(GenericAPIView, RetrieveModelMixin, DestroyModelMixin, UpdateModelMixin):
    queryset = Stud.objects.all()
    serializer_class = Stud

    def retrive(self, request, pk = None, *args,**kwargs):
        return self.retrive(request, *args, **kwargs)

    def update(self,request, pk = None, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request,pk = None, *args, **kwargs):
        return self.delete(request,*args, **kwargs)



# start concrete view from here------------------------------------------------------
# concrete view extend the GenetricView and ModelMixin
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView



# start class from here
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
from rest_framework.generics import ListCreateAPIView

class StudListCreate(ListCreateAPIView):
    queryset = Stud.objects.all()
    serializer_class = StudSerializer

#mixed RetriveUpdateDestroyAPIView which required pk------------------------------------
from rest_framework.generics import RetrieveUpdateDestroyAPIView

class StudRUD(RetrieveUpdateDestroyAPIView):
    queryset = Stud.objects.all()
    serializer_class = StudSerializer


# api using class method----------------------------------------------------------------
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
    
    def update(self, request, pk = None,format = None):
        id = pk
        stu = Stud.objects.get(id = id)
        data = request.data
        serializer = StudSerializer(stu,data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Created'}, status= status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk = None,format = None):
        id = pk
        stu = Stud.objects.get(id = id)
        stu.delete()
        return Response({'msg':'Data Deleted'}, status= status.HTTP_200_OK)



# viewset start from here---------------------------------------------------------
# Note every views models is same here 
from rest_framework import viewsets

class StudViewSet(viewsets.ViewSet):
    # list() is for get all records
    # retrive() = for get single records
    # create = for create insert record
    # update = update data fully
    # partial_update = update data partially
    # distory = delete data

    def list(self,request):
        stu = Stud.objects.all()
        serializers = StudSerializer(stu, many = True)
        data = serializers.data
        return Response(data, status= status.HTTP_200_OK)

    def retrive(self,request,pk):
        id = pk
        stu = Stud.objects.get(id = id)
        serializers = StudSerializer(stu)
        return Response(serializers.data, status = status.HTTP_200_OK)

    def create(self,request):
        serializers = StudSerializer(data = request.data)
        if serializers.is_valid():
            serializers.save()
            return Response({'msg':'Data Created'}, status= status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self,request,pk):
        id = pk
        stu = Stud.objects.get(id = id)
        serializers = StudSerializer(stu, data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response({'msg':'Updated'}, status = status.HTTP_426_UPGRADE_REQUIRED)
        return Response(serializers.errors, status = status.HTTP_400_BAD_REQUEST)

    def partial_update(self,request,pk):
        id = pk
        stu = Stud.objects.get(id = id)
        serializers = StudSerializer(stu,data=request.data, partial = True)
        if serializers.is_valid():
            serializers.save()
            return Response({'msg':'Updated'}, status = status.HTTP_426_UPGRADE_REQUIRED)
        return Response(serializers.errors, status = status.HTTP_400_BAD_REQUEST)

    def destroy(self,request,pk):
        id = pk
        stu = Stud.objects.get(id = id)
        stu.delete()
        return Response({'msg':'Delet'}, status= status.HTTP_508_LOOP_DETECTED)

# model viewset start from here-------------------------------------------------
# modelViewSet Viewset inside nai hunxa
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from django_filters.rest_framework import DjangoFilterBackend
# from rest_framework.filters import 
# class StudModelVievSet(viewsets.ModelViewSet):
#     queryset = Stud.objects.all()
#     serializer_class = StudSerializer
#     authentication_classes = [SessionAuthentication]
#     permission_classes = [IsAuthenticated]
#     filter_backends = [DjangoFilterBackend]
#     filterset_fields = ['name']

# for throttleing in DRF-------------------------------------------------------------------------------
# from rest_framework.throttling import UserRateThrottle, AnonRateThrottle, ScopedRateThrottle
# class StudModelVievSet(viewsets.ModelViewSet):
#     queryset = Stud.objects.all()
#     serializer_class = StudSerializer
#     authentication_classes = [SessionAuthentication]
#     permission_classes = [AllowAny]
#     filter_backends = [DjangoFilterBackend]
#     filterset_fields = ['city']
#     throttle_classes = [AnonRateThrottle, UserRateThrottle]


# -------------------------------search filter  in drf-----------------------------------

from rest_framework.filters import SearchFilter

# class StudModelVievSet(viewsets.ModelViewSet):
#     queryset = Stud.objects.all()
#     serializer_class = StudSerializer
#     authentication_classes = [SessionAuthentication]
#     permission_classes = [AllowAny]
#     filter_backends = [SearchFilter]
    # search_fields = ['name']

    # '^' this symbol says that  start with search
    # search_fields = ['^name']  
    # --------------search s xa vney s bata suru vako sabai name show hunxa------------
    

    # '=' this symbol says that equal to search
    # search_fields = ['=name']
# exact search sanga name milyo vney matra show hunxa------------


#------------------------- ordering filter im drf-----------------------------

from rest_framework.filters import OrderingFilter
# class StudModelVievSet(viewsets.ModelViewSet):
#     queryset = Stud.objects.all()
#     serializer_class = StudSerializer
#     authentication_classes = [SessionAuthentication]
#     permission_classes = [AllowAny]
#     filter_backends = [SearchFilter, OrderingFilter]
#     search_fields = ['name']
#     ordering_fields = ['name']

# OrderingFilter and SearchFilter and DjangoFilterBackend in same ----------------
from rest_framework.filters import OrderingFilter
# class StudModelVievSet(viewsets.ModelViewSet):
#     queryset = Stud.objects.all()
#     serializer_class = StudSerializer
#     authentication_classes = [SessionAuthentication]
#     permission_classes = [AllowAny]
#     filter_backends = [SearchFilter, OrderingFilter, DjangoFilterBackend]
#     filterset_fields = ['name']
#     search_fields = ['name']
#     ordering_fields = ['name']



# page number pagination in DRF---------------------------------------------------------
from rest_framework.pagination import PageNumberPagination
from .mypaginations import MyPagination, MyCursorPagination
class StudModelVievSet(viewsets.ModelViewSet):
    queryset = Stud.objects.all()
    serializer_class = StudSerializer
    # authentication_classes = [SessionAuthentication]
    # permission_classes = [AllowAny]
    # pagination_class = MyPagination
    # pagination_class = MyCursorPagination



# modelviewset Getonly Get and retrive 
# which helps to get users only
#  list and retrive data not update delete

class StudReadOnlyModelViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Stud.objects.all()
    serializer_class = StudSerializer


# serializer relations DRF--------------------------------------------------------------
class SingerModelViewSet(viewsets.ModelViewSet):
    queryset = Singer.objects.all()
    serializer_class = SingerSerialization

class SongModelViewSet(viewsets.ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerialization



# function based api view start from here
from rest_framework.decorators import api_view
# @api_view(['GET','POST','PUT','PATCH', 'DELETE'])

