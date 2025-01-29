from django.contrib.auth.models import AbstractUser
from django.db import models



class CustomUser(models.Model):
    username = models.CharField(max_length=255)
    profile_image = models.URLField(blank=True, null=True)
    ssc_batch = models.CharField(max_length=10, blank=True, null=True)
    designation = models.CharField(max_length=50, blank=True,null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.username
    


class UserMemories(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    image = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)


    def __str__(self):
        return self.user.username
