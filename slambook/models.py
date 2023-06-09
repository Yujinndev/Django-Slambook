from django.db import models
# from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# PERSON MODEL
class Person(models.Model):
  id = models.AutoField(primary_key=True)
  name = models.CharField(max_length=100)
  email = models.EmailField()
  age = models.IntegerField(blank=True, null=True)
  gender = models.CharField(max_length=10, blank=True, null=True)
  course = models.CharField(max_length=100, blank=True, null=True)
  phoneNumber = models.CharField(max_length=15)
  address = models.CharField(max_length=200)
  motto = models.CharField(max_length=500, blank=True, null=True)

  class Meta:
    db_table = "persons"