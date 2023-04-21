from django.db import models

class reasap1(models.Model):
    name = models.CharField(max_length=60,default="true")
    mob = models.CharField(max_length=200,default="true")
class servicesec(models.Model):
    head = models.CharField(max_length=60,default="true")
    content = models.CharField(max_length=300,default="true")
    image = models.FileField(upload_to = "reasap/",max_length=250,null=True,default=None)
class coursesec(models.Model):
    top = models.CharField(max_length=60,default="true")
    sec1 = models.CharField(max_length=50,default="true")
    sec2 = models.CharField(max_length=50,default="true")
    sec3 = models.CharField(max_length=50,default="true")
    sec4 = models.CharField(max_length=50,default="true")
    sec5 = models.CharField(max_length=50,default="true")
    image1 = models.FileField(upload_to="ClassName/",max_length=250,null=True,default=None)
class aboutsec(models.Model):
    top = models.CharField(max_length=20,default="true")
    disc = models.CharField(max_length=100,default="true")
# Create your models here.
