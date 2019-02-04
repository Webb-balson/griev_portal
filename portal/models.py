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
    published_date = models.DateTimeField(default=timezone.now)


class Parent(models.Model):
    studentName = models.CharField(max_length=50)
    usn = models.CharField(max_length=10)
    semester = models.IntegerField()
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.IntegerField()
    complain = models.TextField()
    published_date = models.DateTimeField(default=timezone.now)


class Staff(models.Model):
    staffid = models.CharField(max_length=10)
    name = models.CharField(max_length=50)
    department = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.IntegerField()
    complain = models.TextField()
    published_date = models.DateTimeField(default=timezone.now)

