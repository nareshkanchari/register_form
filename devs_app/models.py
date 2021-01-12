from django.db import models


class UREG(models.Model):
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    address = models.TextField(max_length=100)
    phonenumber = models.BigIntegerField()
    city = models.CharField(max_length=20)
    zip = models.IntegerField()
