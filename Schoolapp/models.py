from django.db import models

# Create your models here.
class Student(models.Model):
    Name=models.CharField(max_length=50 ,unique=True)
    div = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=100)

