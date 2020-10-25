from django.db import models
from django.contrib.auth.models import User
from phone_field import PhoneField
from datetime import datetime

# Create your models here.

class fullUser(models.Model):

    college_name = models.CharField(max_length=100)
    phone_number = PhoneField(blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class events(models.Model):
    
    name = models.CharField(max_length=100)
    img = models.ImageField()
    des = models.TextField()
    price = models.IntegerField()
    start_date = models.DateField()
    url = models.URLField(max_length = 200,blank=True)
    duration_days = models.PositiveIntegerField()

class query(models.Model):

    name = models.CharField(max_length=100)
    email = models.EmailField(max_length = 254)
    subject = models.TextField()
    message = models.TextField() 

class collegeName(models.Model):
    name = models.CharField(max_length=100)

class campusAmbassador(models.Model):
    name = models.CharField(max_length=100)
    user_id = models.PositiveIntegerField()
    event_id = models.PositiveIntegerField()
    previous_experience = models.TextField()
    approval = models.BooleanField(default=False)

class ticket(models.Model):
    
    id_ticket = models.ForeignKey(fullUser,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    user_id = models.PositiveIntegerField()
    event_name = models.CharField(max_length=100)
    event_id = models.PositiveIntegerField()
    college_name = models.CharField(max_length=100)
    date_of_purchase = models.DateTimeField(auto_now_add=True)


