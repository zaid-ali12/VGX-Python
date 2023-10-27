from django.db import models

class Client(models.Model):

    name= models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    cellno=models.CharField(max_length=100)
    info=models.CharField(max_length=400)

   
class Devlopers(models.Model):
    expertise=models.CharField(max_length=100)
    Fname=models.CharField(max_length=100)
    lname=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    pno=models.CharField(max_length=100)
    desc=models.CharField(max_length=300)

