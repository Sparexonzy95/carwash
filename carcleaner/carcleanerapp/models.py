from django.db import models
from datetime  import date
from django.db import models
from django.contrib.auth.models import User
# Create your models here.


sub_choices = [("BP","BASIC PACKAGE"),
               ("PP","PRESIDENTIAL PACKAGE"),
               ("EP","EXECUTIVE PACKAGE"),
               ("EDP","EXPRESS DETAILING PACKAGE"),]

pub_choices = [("1MNT","1-MONTH"),
               ("2MNT","3-MONTH"),
               ("6MNT","6-MONTH"),
               ("12MNT","12-MONTH"),]

class CarWash(models.Model):
    Customer = models.ForeignKey(User, on_delete=models.CASCADE,related_name="carwash")
    plate_number=models.CharField(max_length=20)
    subcription_packages=models.CharField(max_length=100,choices=sub_choices)
    subcription_duration_in_month=models.CharField(max_length=1000,choices=pub_choices)
    timestamp=models.DateTimeField(auto_now_add=True)      
    number_0f_cars=models.IntegerField()
    times_of_wash=models.IntegerField()
    number_0f_cars=models.IntegerField()
    package_price=models.IntegerField()
    reward_points=models.IntegerField()
    DisplayFields = ['Customer','plate_number','subcription_packages','subcription_duration_in_month','timestamp','package_price','reward_points','times_of_wash',]
    FilterFields = [ 'Customer', 'plate_number',]
    
    

    def __str__(self):
        return self.plate_number
