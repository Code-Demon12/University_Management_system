from django.db import models

class Branch(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)

class Student(models.Model):
    user = models.OneToOneField('accounts.User', on_delete=models.CASCADE)
    roll_no = models.CharField(max_length=50)

class Faculty(models.Model):
    user = models.OneToOneField('accounts.User', on_delete=models.CASCADE)
    department = models.CharField(max_length=100)

class Staff(models.Model):
    user = models.OneToOneField('accounts.User', on_delete=models.CASCADE)
    designation = models.CharField(max_length=100)
