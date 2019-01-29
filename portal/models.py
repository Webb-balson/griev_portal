from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.

class Student(models.Model):
    usn = models.CharField(max_length=10)
    name = models.CharField(max_length=50)
    semester = models.IntegerField()
    parentName = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.IntegerField()
    complain = models.TextField()

