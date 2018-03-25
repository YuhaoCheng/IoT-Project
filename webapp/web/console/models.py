from django.db import models

# Create your models here.
# class Person(models.Model):
#     name = models.CharField(max_length=30)
#     age = models.IntegerField()
#
#     def __str__(self):
#         return self.name

class Manager(models.Model):
    managerID = models.CharField(max_length=10)
    password = models.CharField(max_length=16)

    def __str__(self):
        return self.managerID

class Data(models.Model):
    deviceID = models.CharField(max_length=10)
    temperature = models.IntegerField()
    humidity = models.IntegerField()
    light = models.IntegerField()
    time = models.CharField(max_length=45)
    day = models.CharField(max_length=45)

class Device(models.Model):
    deviceID = models.CharField(max_length=10)
    location = models.CharField(max_length=45)
    type = models.CharField(max_length=45)
    description = models.CharField(max_length=45)

class Warning(models.Model):
    time = models.CharField(max_length=45)
    day = models.CharField(max_length=45)
    attribute = models.CharField(max_length=45)
    deviceID = models.CharField(max_length=45)