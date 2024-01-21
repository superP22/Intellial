from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=100)
    sem = models.IntegerField()
    branch= models.CharField(max_length=100)