from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    #path('usermessage',views.usermessage,name="usermessage"),  
    path('venuefilter',views.venuefilter,name="venuefilter"),
    #path('addhotels',views.addhotels,name="addhotels"),
    path('Addinformation',views.Addinformation,name="Addinformation"),
    path('successmessage',views.successmessage,name="successmessage")
    #path('showuserinfo',views.showuserinfo,name="showuserinfo"),
    #path('edituserinfo/<str:pk>',views.edituserinfo,name='edituserinfo'),
    #path('deleteuserinfo/<str:pk>',views.deleteuserinfo,name='deleteuserinfo')
]