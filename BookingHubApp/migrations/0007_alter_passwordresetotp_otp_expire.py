# Generated by Django 4.2.4 on 2023-12-10 14:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BookingHubApp', '0006_alter_passwordresetotp_otp_expire'),
    ]

    operations = [
        migrations.AlterField(
            model_name='passwordresetotp',
            name='OTP_expire',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 10, 14, 27, 39, 565097, tzinfo=datetime.timezone.utc)),
        ),
    ]
