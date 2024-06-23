from django.db import models

# Create your models here.
from django.contrib.auth.models import User   
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email=models.EmailField()
    addresss=models.TextField()
class Product(models.Model):
    product_id=models.IntegerField(primary_key=True)
    product_name=models.CharField(max_length=100)
    quantity=models.IntegerField()
    price=models.IntegerField()
class Employee(models.Model):
    emp_id=models.IntegerField(primary_key=True)
    emp_name=models.CharField(max_length=100)
    salary=models.IntegerField()
    hire_date=models.DateField()
    role=models.CharField(max_length=100)

