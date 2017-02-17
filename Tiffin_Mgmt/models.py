from django.db import models
from django.db.models.fields import AutoField
from django.forms.fields import CharField
from django.utils.dateformat import DateFormat

# Create your models here.
class User_Mgmt(models.Model):
    user_id = models.AutoField(primary_key = True)
    u_name = models.CharField(max_length=20)
    u_pass = models.CharField(max_length=20)

class Tiffin_Mgmt(models.Model):    
    t_id = models.AutoField(primary_key = True)
    t_date = models.DateField(auto_now_add=False)
    t_price = models.CharField(max_length = 10)
    
class launch_Mgmt(models.Model):    
    t_id = models.AutoField(primary_key = True)
    t_date = models.DateField(auto_now_add=False)
    t_price = models.CharField(max_length = 10)

class dinner_Mgmt(models.Model):    
    t_id = models.AutoField(primary_key = True)
    t_date = models.DateField(auto_now_add=False)
    t_price = models.CharField(max_length = 10)    