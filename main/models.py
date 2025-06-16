from django.db import models
from django.contrib.auth.models import User
# so basically here we not create any superuser for OTP calss  we just create an opt field inside OTP model to get otp_code from OTP model and  link this with django defult User model

class OTP(models.Model):
    user =models.ForeignKey(User,on_delete=models.CASCADE)
    otp_code = models.CharField(max_length=6)

