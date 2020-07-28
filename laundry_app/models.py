from django.db import models

from django.contrib.auth.models import User
# Create your models here.

class Catogary_name(models.Model):
    catg_name = models.CharField(max_length=265, unique=True)

    def __str__(self):
        return self.catg_name


class Item_detail(models.Model):
    Catogary   = models.CharField(max_length=50, default=" ")
    Item_name = models.CharField(max_length=50, default=" ")
    Washing_price = models.CharField(max_length=50, default="")
    Dryclean_price =  models.CharField(max_length=50, default="")

    def __str__(self):
        return self.Item_name

class Branch(models.Model):
    Name = models.CharField(max_length=50, default=" ")
    Service_Available = models.CharField(max_length=50, default=" ")

    def __str__(self):
        return self.Name

class ClientDetail(models.Model):
    Client_Id = models.AutoField(primary_key=True) 
    First_Name = models.CharField(max_length=50, default="")
    Last_Name = models.CharField(max_length=50, default="")
    Address = models.CharField(max_length=80, default="")
    Subscription_Package = models.CharField(max_length=30, default="")
    Phone = models.CharField(max_length=50, default=" ")
    Email = models.EmailField(max_length=255)
    Password = models.CharField(max_length=50, default="")
    Conform_Password = models.CharField(max_length=50, default=" ")

    def __str__(self):
        return str(self.Client_Id) +" : " + self.First_Name +"   "+self.Last_Name +"  "+ str(self.Phone)

