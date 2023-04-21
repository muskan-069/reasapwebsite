from django.db import models

# Create your models here.
class Exam(models.Model):
    Question = models.CharField(max_length=500,default="true")
    Option1 = models.CharField(max_length=100,default="true")
    Option2 = models.CharField(max_length=100,default="true")
    Option3 = models.CharField(max_length=100,default="true")
    Option4 = models.CharField(max_length=100,default="true")
    Corrans = models.CharField(max_length=100,default="true")
class alphabetseries(models.Model):
    Ques = models.CharField(max_length=500,default="true")
    Op1 = models.CharField(max_length=100,default="true")
    Op2 = models.CharField(max_length=100,default="true")
    Op3 = models.CharField(max_length=100,default="true")
    Op4 = models.CharField(max_length=100,default="true")
    Corans = models.CharField(max_length=100,default="true")
class seatar(models.Model):
    Ques1 = models.CharField(max_length=500,default="true")
    Op11 = models.CharField(max_length=100,default="true")
    Op12 = models.CharField(max_length=100,default="true")
    Op13 = models.CharField(max_length=100,default="true")
    Op14 = models.CharField(max_length=100,default="true")
    Corans1 = models.CharField(max_length=100,default="true")
class ordrank(models.Model):
    Ques2 = models.CharField(max_length=500,default="true")
    Op21 = models.CharField(max_length=100,default="true")
    Op22 = models.CharField(max_length=100,default="true")
    Op23 = models.CharField(max_length=100,default="true")
    Op24 = models.CharField(max_length=100,default="true")
    Corans2 = models.CharField(max_length=100,default="true")
class bloodrel(models.Model):
    Ques3 = models.CharField(max_length=500,default="true")
    Op31 = models.CharField(max_length=100,default="true")
    Op32 = models.CharField(max_length=100,default="true")
    Op33 = models.CharField(max_length=100,default="true")
    Op34 = models.CharField(max_length=100,default="true")
    Corans3 = models.CharField(max_length=100,default="true")