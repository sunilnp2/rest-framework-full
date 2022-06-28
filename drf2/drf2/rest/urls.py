
from django.urls import path
from rest.views import *
# from django improt 
urlpatterns = [
    path('', home, name = "home" ),
    path('infoapi', StudList.as_view(), name= 'infoapi'),
    path('informapi', StudListCreate.as_view(), name= 'infoapi'),
    path('infoapi/<int:pk>', InfoRUD.as_view(), name= 'infoapi'),
]
