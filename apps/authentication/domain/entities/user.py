from django.contrib.auth.models import AbstractUser
from django.db import models
from datetime import date

class User(AbstractUser):
    fullname = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    photo_url = models.URLField(null=True, blank=True)
    nationality = models.CharField(max_length=100)
    birthdate = models.DateField()
    firebase_uid = models.CharField(max_length=255, null=True, blank=True)

    @property
    def age(self):
        today = date.today()
        return today.year - self.birthdate.year - ((today.month, today.day) < (self.birthdate.month, self.birthdate.day))
    def __str__(self):
        return self.email