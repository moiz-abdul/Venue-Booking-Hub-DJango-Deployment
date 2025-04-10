from django.shortcuts import render,redirect
from BookingHubApp.models import Uzerlogin,PasswordResetOTP,UserMessage,filterdata,user_information
#from Myapp.forms import CreateUserForm
#from django.contrib.auth.hashers import make_password,check_password
#from django.contrib.auth.password_validation import validate_password,CommonPasswordValidator
#from django.core.exceptions import ValidationError
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages 
from django.forms import ModelForm
#from django.contrib.auth import authenticate,login,logout
#from django.forms import inlineformset_factory
from django.core.exceptions import ObjectDoesNotExist
#from datetime import timedelta
#from django.utils import timezone
#from BookingHubApp import settings
from django.shortcuts import render
from django.db import connection

import time

# Create your views here.

# HOME  FUNCTION 

def home(request):
    return render(request,"BookingHubApp/index.html")

# HOME  FUNCTION END

# VenueFIlter PAGE FUNCTION

def venuefilter(request):
    hotels = None
    if request.method == 'POST':
        venue_type = request.POST.get('venue_type')
        location = request.POST.get('location')
        guests = request.POST.get('guests')
        
        sql_query = """
            SELECT * FROM filterdata 
            WHERE Name LIKE %s AND Location = %s AND Capacity_of_Guests = %s
        """

        with connection.cursor() as cursor:
            cursor.execute(sql_query, ('%' + venue_type + '%', location, guests))
            hotels = cursor.fetchall()
    else:
        hotels = filterdata.objects.all()

    return render(request, "BookingHubApp/Venuefilter.html", {'hotelsId': hotels})

# VenueFIlter PAGE FUNCTION END


# ADD INFORMATION FUNCTION 


def Addinformation(request):
        if request.method == "POST":
            information = user_information()
            information.First_name = request.POST['Fname']
            information.Last_name = request.POST['Lname']
            information.Phone_number = request.POST['PhoneNo']
            information.Email_address = request.POST['Email']
            information.Event_date = request.POST['Eventdate']
            information.Event_time = request.POST['Eventtime']
            information.No_of_Guests = request.POST['No-of-guests']
            information.Message = request.POST['Message']

            information.save()
            return redirect('successmessage')
            #messages.success(request, " Information Successfully Added ")

 
        return render(request, 'BookingHubApp/Addinformation.html')
    

# ADD INFORMATION FUNCTION  END


# SUCCESS MESSAGE FUNCTION

def successmessage(request):
     return render(request, 'BookingHubApp/successmessage.html')

# SUCCESS MESSAGE FUNCTION END
'''

# User Message FUNCTION 

def usermessage(request):
    if request.method == "POST":
        Name = request.POST['name']
        email = request.POST['email']
        PoNumber = request.POST['phonenumber']
        message = request.POST['Message']

        NewMessage = UserMessage.objects.create(PersonName = Name , Email = email , PhoneNumber = PoNumber , Message = message)
        NewMessage.save()

    return render(request, "BookingHubApp/Usermessage.html")

# User Message FUNCTION END 


'''

