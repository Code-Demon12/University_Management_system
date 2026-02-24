from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

class User(AbstractBaseUser, PermissionsMixin):
    ROLE_CHOICES = [
        ('student','Student'),
        ('faculty','Faculty'),
        ('staff','Staff'),
        ('admin','Admin'),
        ('super-admin','Super Admin'),
    ]

    email = models.EmailField(unique=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    branch = models.ForeignKey('university.Branch', on_delete=models.SET_NULL, null=True)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'

class EmailOTP(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    otp = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)
    is_verified = models.BooleanField(default=False)

class Role(models.Model):
    name = models.CharField(max_length=50, unique=True)

class Permission(models.Model):
    code = models.CharField(max_length=100, unique=True)
    description = models.TextField()

class RolePermission(models.Model):
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    permission = models.ForeignKey(Permission, on_delete=models.CASCADE)
