from django.db import models

# Create your models here.

class tbl_district(models.Model):
    district_name = models.CharField(max_length=50)


class tbl_place(models.Model):
    place_name = models.CharField(max_length=50)
    district = models.ForeignKey(tbl_district, on_delete=models.CASCADE)