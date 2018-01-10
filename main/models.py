from django.db import models
# Create your models here.

class Farmers(models.Model):
    
    fname = models.CharField(max_length=255, default=None)
    lname = models.CharField(max_length=255, default=None)
    email = models.CharField(max_length=255, default=None, unique= True)
    password = models.CharField(max_length=255, default=None)
    status = models.IntegerField(default=0)
    phone = models.IntegerField(default=0)
    created_at = models.DateField(default=None)
    updated_at = models.DateField(default=None)

class Farms(models.Model):
    farmer_id =  models.IntegerField()
    farm_name =  models.CharField(default=None, max_length=255)
    farm_avatar =  models.CharField(max_length=255, default=None)

class Temperatures(models.Model):
    farm_id =  models.CharField(max_length=255, default=None)
    year =  models.IntegerField(default=0)
    month =  models.IntegerField(default=0)
    day = models.IntegerField(default=0)
    hour = models.IntegerField(default=0)
    minute = models.IntegerField(default=0)
    second = models.IntegerField(default=0)
    microsecond = models.IntegerField(default=0)
    value = models.IntegerField(default=0)

class Chats(models.Model):
    chat_id =   models.CharField(max_length=255, default=None)
    member_1 =  models.CharField(max_length=20, default=None)
    member_2 =  models.CharField(max_length=20, default=None)
    created_at = models.DateField(default=None)
    updated_at = models.DateField(default=None)
    
class Messages(models.Model):
    chat_id =   models.CharField(max_length=255, default=None)
    sender =  models.CharField(max_length=20, default=None)
    receiver =  models.CharField(max_length=20, default=None)
    message =  models.CharField(max_length=20, default=None)
    created_at = models.DateField(default=None)
    updated_at = models.DateField(default=None)
    
    
    
       

    
