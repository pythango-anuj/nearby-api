from django.urls import path
from .views import Nearbycreateapi,Nearbylistapi,Nearbyupdateapi,Nearbydeleteapi

urlpatterns = [
    path('api',Nearbylistapi.as_view()),
    path('api/create',Nearbycreateapi.as_view()),
    path('api/<int:pk>',Nearbyupdateapi.as_view()),
    path('api/<int:pk>/delete',Nearbydeleteapi.as_view())   
]