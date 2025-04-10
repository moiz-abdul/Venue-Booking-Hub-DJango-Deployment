from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('',views.adminlogin,name="adminlogin"),
    path('adminlogout',views.adminlogout,name="adminlogout"),
    path('showuserinfo',views.showuserinfo,name="showuserinfo"),
    path('addhotels',views.addhotels,name="addhotels"),
    path('edituserinfo/<str:pk>',views.edituserinfo,name='edituserinfo'),
    path('deleteuserinfo/<str:pk>',views.deleteuserinfo,name='deleteuserinfo')
]