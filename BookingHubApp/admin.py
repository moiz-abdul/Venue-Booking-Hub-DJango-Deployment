from django.contrib import admin
from .models import Uzerlogin,PasswordResetOTP,UserMessage,filterdata,user_information

# Register your models here.

admin.site.register(Uzerlogin)
admin.site.register(PasswordResetOTP)
admin.site.register(UserMessage)
admin.site.register(filterdata)
admin.site.register(user_information)
