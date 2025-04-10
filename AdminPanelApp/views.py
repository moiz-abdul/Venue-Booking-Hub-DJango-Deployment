from django.shortcuts import render,redirect
from BookingHubApp.models import UserMessage,filterdata,user_information
#from django.core.exceptions import ValidationError
from django.http import HttpResponse
from django.contrib.auth.models import User
#from django.contrib.auth.decorators import login_required
from django.contrib import messages 
from django.contrib.auth import logout
from django.core.exceptions import ObjectDoesNotExist
from django.db import connection
import time
# Create your views here.




# ADMIN LOGIN

def adminlogin(request):
     if request.method == "POST":
          username = request.POST['username']
          password = request.POST['password']

          if username == "admin":
            if password == "#admin123":
                 return render (request,"AdminPanelApp/showuserinfo.html")
            else:
                 messages.error(request,"Invalid Credentials ! ")
                 return redirect('adminlogin')
                 
     
     return render(request,"AdminPanelApp/adminlogin.html")


def adminlogout(request):
     logout(request)
     return redirect('adminlogin')
# ADD HOTELS FUNC 


def addhotels(request):
    if request.method == "POST":
        hotel = filterdata()
        hotel.Name = request.POST['Name']
        hotel.Location = request.POST['Location']
        hotel.Capacity_of_Guests = request.POST['Guests']
        hotel.Rate = request.POST['Rate']
        hotel.Address = request.POST['Address']
        hotel.Contact = request.POST['Contact']
        hotel.Event_Space = request.POST['Eventspace']

        if 'Image' in request.FILES:
            hotel.Image = request.FILES['Image']
        
        hotel.save()
        messages.success(request, " Hotel Added Successfully ! ")
        return redirect('/')
        
    return render(request,"AdminPanelApp/AddHotels.html")



# SHOW USER INFORMATION 

def showuserinfo(request):
    userinfo = user_information.objects.all()

    return render(request, "AdminPanelApp/showuserinfo.html", {'userinfo':userinfo})




# EDIT USER INFORMATION 


def edituserinfo(request,pk):
    
        edituser = user_information.objects.get(id=pk)

        if request.method == "POST":
             edituser.First_name = request.POST['Fname']
             edituser.Last_name = request.POST['Lname']
             edituser.Phone_number = request.POST['PhoneNo']
             edituser.Email_address = request.POST['Email']
             edituser.Event_date = request.POST['Eventdate']
             edituser.Event_time = request.POST['Eventtime']
             edituser.No_of_Guests = request.POST['No-of-guests']
             edituser.Message = request.POST['Message']

             edituser.save()
             messages.success(request, " Update Information Successfully ")
             return redirect('/')
        
        return render(request,"AdminPanelApp/edituserinfo.html",{'edituser':edituser})
    


# DELETE USER INFORMATION 


def deleteuserinfo(request,pk):
     deleteinfo = user_information.objects.get(id=pk)
     deleteinfo.delete()
     messages.success(request," Delete Information Successfully ")
     
     return render(request,"AdminPanelApp/showuserinfo.html")


     