# Generated by Django 4.2.4 on 2023-12-10 14:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BookingHubApp', '0005_usermessage_alter_passwordresetotp_otp_expire'),
    ]

    operations = [
        migrations.AlterField(
            model_name='passwordresetotp',
            name='OTP_expire',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 10, 14, 15, 9, 934129, tzinfo=datetime.timezone.utc)),
        ),
    ]
