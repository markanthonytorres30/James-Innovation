from django.db import models

# Create your models here.
from inventory.models import Location

class UserType(models.Model):
    userType_code = models.IntegerField(default=1)
    userType_name = models.CharField(max_length=10)
    userType_description = models.CharField(max_length=150)

class Privelege(models.Model):
    privelege_code = models.CharField(max_length=5)
    privelege_name = models.CharField(max_length=10)
    privelege_description = models.CharField(max_length=150)

class Users(models.Model):
    user_code = models.CharField(max_length = 10)
    user_name = models.CharField(max_length = 50)
    user_phone = models.IntegerField(default=123456789)
    user_email = models.EmailField()
    user_password = models.CharField(max_length = 10)
    user_privelege = models.ForeignKey(Privelege,on_delete=models.CASCADE)
    user_type = models.ForeignKey(UserType,on_delete=models.CASCADE)
    user_branch = models.ForeignKey(Location,on_delete=models.CASCADE)


