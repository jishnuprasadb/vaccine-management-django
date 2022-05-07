from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class Login(AbstractUser):
    is_user=models.BooleanField(default=False)
    is_nurse=models.BooleanField(default=False)

class User(models.Model):
    user=models.ForeignKey(Login,on_delete=models.CASCADE,related_name='user')
    name=models.CharField(max_length=50)
    email=models.EmailField()
    phone_number=models.CharField(max_length=50)
    age=models.IntegerField()
    address=models.TextField()

class Vaccine(models.Model):
    name=models.CharField(max_length=50)
    description=models.TextField()


class Hospital(models.Model):
    name=models.CharField(max_length=100)
    place=models.CharField(max_length=100)
    contact=models.CharField(max_length=100)
    email=models.EmailField()



class Nurse(models.Model):
    user=models.ForeignKey(Login,on_delete=models.CASCADE,related_name='nurse')
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = models.CharField(max_length=50)
    age = models.IntegerField()
    address = models.TextField()
    hospital=models.OneToOneField(Hospital,on_delete=models.CASCADE)








