from django.db import models
from Admin.models import *
# Create your models here.
class tbl_user(models.Model):
    username = models.CharField(max_length=50)
    usercontact = models.CharField(max_length=50)
    useremail = models.CharField(max_length=50)
    userpassword = models.CharField(max_length=50)
    useraddress = models.CharField(max_length=50)
    userphoto=models.FileField(upload_to='Assets/UserPhoto/')


class tbl_shop(models.Model):
    shopname = models.CharField(max_length=50)
    shopcontact = models.CharField(max_length=50)
    shopemail = models.CharField(max_length=50)
    shoppassword = models.CharField(max_length=50)
    shopaddress = models.CharField(max_length=50)
    shopphoto=models.FileField(upload_to='Assets/ShopPhoto/')
    shopproof=models.FileField(upload_to='Assets/ShopProof/')
    place=models.ForeignKey(tbl_place,on_delete=models.CASCADE)