from django.db import models
from django.utils import timezone
import datetime
import os

# Create your models here.

class Uzerlogin(models.Model):
    Username = models.CharField(max_length=100,blank=False,null=False)
    Email = models.EmailField(max_length=100,blank=False,null=False)
    password = models.CharField(max_length=100,blank=False,null=False)
    is_active = models.BooleanField(default=True)
    def __str__(self):
        return self.Username


class PasswordResetOTP(models.Model):
    User_login = models.ForeignKey(Uzerlogin,on_delete=models.CASCADE, null=True)
    OTP = models.IntegerField()
    OTP_create = models.DateTimeField(default=timezone.now)
    OTP_expire = models.DateTimeField(default=timezone.now() + timezone.timedelta(minutes=5))

    def is_expired(self):
        return timezone.now() > self.OTP_expire


class UserMessage(models.Model):
    PersonName = models.CharField(max_length=100,blank=False,null=False)
    Email = models.EmailField(max_length=100,blank=False,null=False)
    PhoneNumber = models.CharField(max_length=20)
    Message = models.TextField()

    def __str__(self):
        return f"{self.PersonName}'s message" 
    
def filepath(request,filename):
    old_filename = filename
    timenow = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    filename = "%s%s" % (timenow, old_filename)
    return os.path.join('upload/', filename)
    
class filterdata(models.Model):
    Name = models.CharField(max_length=150)
    Location = models.TextField(max_length=50)
    Capacity_of_Guests = models.IntegerField()
    Rate = models.CharField(max_length=50)
    Address = models.TextField(max_length=200)
    Contact = models.CharField(max_length=15)
    Event_Space = models.IntegerField()
    Image = models.ImageField(upload_to=filepath, null=True, blank=True)


class user_information(models.Model):
    First_name = models.CharField(max_length=100)
    Last_name = models.CharField(max_length=100)
    Phone_number = models.CharField(max_length=15)
    Email_address = models.CharField(max_length=50)
    Event_date = models.CharField(max_length=30)
    Event_time = models.CharField(max_length=30)
    No_of_Guests = models.IntegerField()
    Message = models.TextField(max_length=300)
    








