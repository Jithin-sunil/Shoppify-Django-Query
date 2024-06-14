from django.db import models

# Create your models here.
class tbl_user(models.Model):
    username = models.CharField(max_length=50)
    usercontact = models.CharField(max_length=50)
    useremail = models.CharField(max_length=50)
    userpassword = models.CharField(max_length=50)
    useraddress = models.CharField(max_length=50)
    userphoto=models.FileField(upload_to='Assets/UserPhoto/')
    