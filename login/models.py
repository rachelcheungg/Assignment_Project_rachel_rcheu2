from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(primary_key=True, max_length=20)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(unique=True, max_length=11, blank=True, null=True)

    def __str__(self):
        return f"{self.username}"
